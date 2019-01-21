"""Base compiler classes, whicn aother system is based on."""
from abc import ABCMeta
from abc import abstractmethod
import hashlib

from types import MethodType

import typing as ty
import typing_extensions as te

T = ty.TypeVar('T')
# OutputGot = ty.NewType('OutputGot', ty.List[ty.Union['AstNull', str]])


class OutputGot(ty.List['OutputLine']):
    pass


class OutputLine:
    """Handle line content and indent level."""

    __slots__ = 'line', 'indent'

    def __init__(self, line: ty.Union['AstNull', str],
                 indent: int) -> None:
        """Initialize."""
        self.line = line
        self.indent = indent


class KSPBaseMeta(ABCMeta):
    """Abstract base metaclass for all KSP objects.

    for being under united ABCMeta parent
    """

    pass


class KSP(metaclass=KSPBaseMeta):
    """Base class for all compiler objects.

    Takes part of singletone object durin compilicng.
    Has to be refreshed by script at the start of compilation.
    """

    __slots__ = '__dict__'

    __script: ty.Optional['ScriptBase'] = None
    __output: ty.Optional['Output'] = None
    __outputs: ty.List['Output'] = list()
    __listener: ty.Optional['EventListener'] = None
    __is_compiled: bool = False
    __callback: ty.Optional['CallbackBase'] = None
    __is_bool: bool = False
    __inits: ty.List['HasInit'] = list()
    docs: bool = False
    indents: int = 4
    compacted_names: bool = False

    @staticmethod
    def refresh() -> None:
        """Set KSP variables to defaults."""
        KSP.__script = None
        KSP.__output = None
        KSP.__listener = None
        KSP.__is_compiled = False
        KSP.__callback = None
        KSP.__is_bool = False
        KSP.__inits = list()
        KSP.__outputs = list()
        KSP.docs = False
        KSP.indents = 4

    class NoBaseError(Exception):
        """NoBaseError."""

        def __init__(self) -> None:
            """Raise if new output is requested not under script."""
            super().__init__('Script is not initialized')

    @staticmethod
    def append_init(init: 'HasInit') -> None:
        """Append object, able to generate init lines."""
        KSP.__inits.append(init)

    @staticmethod
    def get_inits() -> ty.List['HasInit']:
        """Return all objects with inits."""
        return KSP.__inits

    @staticmethod
    def new_out() -> 'Output':
        """Return new Output object.

        normally, should be used by any class wants to produce
        block of lines"""
        # think of point to use
        # if KSP.__script is None:
        #     raise KSP.NoBaseError
        if KSP.__outputs:
            il = KSP.__outputs[-1].indent_level
        else:
            il = 0
        otpt = Output(il)
        KSP.__outputs.append(otpt)
        return otpt

    @staticmethod
    def get_out() -> 'Output':
        """Return current Output object."""
        # if not KSP.__is_compiled:
        #     return Output(0)
        if not KSP.__outputs:
            raise RuntimeError('No Output availble')
        return KSP.__outputs[-1]

    @staticmethod
    def pop_out() -> 'OutputGot':
        """Return lines from the current Output and delete it."""
        out: 'OutputGot' = KSP.__outputs[-1].get()
        KSP.__outputs.pop()
        return out

    @staticmethod
    def merge_out() -> None:
        """Put lines from the current Output to the next and delete it."""
        out = KSP.pop_out()
        KSP.__outputs[-1].put_lines(out)

    @staticmethod
    def event(event: 'ListenerEventBase') -> None:
        """Produce event to the current EventListener object.

        or do nothing"""
        if KSP.__listener is not None:
            KSP.__listener.put_event(event)

    @staticmethod
    def set_listener(listener: 'EventListener') -> None:
        """Attach listener to KSP class."""
        KSP.__listener = listener

    @staticmethod
    def is_compiled() -> bool:
        """Check state (changes returns of KSP objects)."""
        return KSP.__is_compiled

    @staticmethod
    def set_compiled(val: bool) -> None:
        """Set state (changes returns of KSP objects)."""
        KSP.__is_compiled = val

    @staticmethod
    def set_callback(obj: 'CallbackBase') -> None:
        """Set callback to be counted by built-ins."""
        if obj is None:
            KSP.__callback = obj
            return
        if KSP.__callback is not None:
            raise RuntimeError(
                f'callback {KSP.__callback} is opened yet')
        KSP.__callback = obj

    @staticmethod
    def callback() -> ty.Optional[object]:
        """Retrieve current callback.

        Return CallbackBase object or None"""
        return KSP.__callback

    @staticmethod
    def is_bool() -> bool:
        """Check state (for usage in if/else select/case blocks)."""
        return KSP.__is_bool

    @staticmethod
    def set_bool(val: bool) -> None:
        """Set bool state (for usage in if/else select/case blocks)."""
        if not isinstance(val, bool):
            raise TypeError('has to be bool')
        KSP.__is_bool = val

    @staticmethod
    def in_init() -> bool:
        """Check if compiler is in init callback."""
        return KSP.__callback is None


class ScriptBase(KSP):
    """Abstract base class for script."""

    @abstractmethod
    def main(self) -> None:
        """Has to be overloaded by the main compilation function."""
        pass

    @abstractmethod
    def compile(self) -> None:
        """Compile the script."""
        pass


class Output(KSP):
    """Handles generation of code lines."""

    __slots__ = '_queue', '_blocks', '_lines', '_block_in_queue', \
        '_start_indent', 'indent_level', '_blocked'

    def __init__(self, indent_level: int) -> None:
        """Initialize.

        indent level has to be 0 or been taken from the last used Output"""
        if not isinstance(indent_level, int) or indent_level < 0:
            raise TypeError(
                f'ident_level has to be int >= 0, pasted {indent_level}')
        self._queue: ty.List['AstRoot'] = list()
        self._blocks: ty.List['OutputBlock'] = list()
        self._lines: ty.List[OutputLine] = list()
        self._block_in_queue: \
            ty.Optional[ty.Tuple['OutputBlock', 'OutputBlock', int]] = None
        self._start_indent = indent_level
        self.indent_level = indent_level
        self._blocked = False

    def block(self) -> None:
        """Block any addition to Output.

        Raises AssertionError if has been blocked earlier"""
        if self._blocked is True:
            raise RuntimeError('blocked yet')
        self._blocked = True

    def release(self) -> None:
        """Allow to add things to code.

        Raises AssertionError if has not been blocked earlier"""
        if self._blocked is False:
            raise RuntimeError('has not been blocked')
        self._blocked = False

    def put_to_queue(self, ast: 'AstRoot') -> None:
        """Put AstRoot to queue.

        leaving empty line to be replaced by Ast, if it is not expanded"""
        if self._blocked:
            return
        ast.queue_line = len(self._lines)
        self._queue.append(ast)
        self.put_line(AstNull())

    def put_immediatly(self, ast: 'AstRoot') -> None:
        """Expand AstRoot immediately.

        Checks block queue and close it at nesessary.
        Checks queue for expanded during current Ast and removes them
        from queue."""
        if self._blocked:
            return
        if self._block_in_queue:
            block = self._block_in_queue[0]
            block_line = self._block_in_queue[2]
            self._lines[block_line].line = block.close.expand()
            self.indent_level -= 1
            self._block_in_queue = None
            self._blocks.pop()
        if not isinstance(ast, AstRoot):
            raise TypeError(
                f'ast arg has to be of type AstRoot, passed: {ast}')
        line = ast.expand()
        for idx, ast in enumerate(self._queue):
            if ast.expanded is True:
                del self._queue[idx]
        self.put_line(line)

    def put_line(self, line: ty.Union['AstNull', str],
                 idx: ty.Optional[int]=None,
                 indent: int=0) -> None:
        """Put expanded line or AstNull to list with correct indent."""
        if self._blocked:
            return
        if isinstance(line, AstNull):
            if not idx:
                self._lines.append(OutputLine(line,
                                              self.indent_level + indent))
            else:
                self._lines[idx].line = line
            return
        # newline: str = ' ' * KSP.indents * self.indent_level + line
        self._lines.append(OutputLine(line, self.indent_level + indent))

    def put_lines(self, lines: OutputGot) -> None:
        """Put lines from another Output object to list."""
        for line in lines:
            self.put_line(line.line, indent=line.indent)

    def open_block(self, block: 'OutputBlock') -> None:
        """Open block, increase indent level.

        ignores closing of waiting block if any.

        Raises AssertionError if waiting block, and it is not
        the same block is recieved"""
        if self._blocked:
            return
        if self._block_in_queue:
            opened = self._block_in_queue[0]
            nextb = self._block_in_queue[1]
            if block != nextb:
                raise RuntimeError(f'block {nextb} is waited by {opened}')
            block_line = self._block_in_queue[2]
            self._block_in_queue = None
            self.indent_level -= 1
            self._blocks.pop()
        self.put_immediatly(block.open)
        self.indent_level += 1
        self._blocks.append(block)

    def close_block(self, block: 'OutputBlock') -> None:
        """Close block and decrease indent level."""
        if self._blocked:
            return
        if not self._blocks:
            raise RuntimeError('all blocks are closed')
        if self._blocks[-1] != block:
            raise RuntimeError(f'block {self._blocks[-1]} on the top of stack')
        # if self._block_in_queue and self._block_in_queue[0] == block:
        #     self._block_in_queue = None
        if self.indent_level < self._start_indent:
            raise RuntimeError(
                f'indent level below stert. line: {block.close.expand()}')
        self.indent_level -= 1
        self.put_immediatly(block.close)
        self._blocks.pop()

    def wait_for_block(self, opened: 'OutputBlock',
                       next_block: 'OutputBlock') -> None:
        """Put block to block_queue for closing with next event."""
        if self._blocked:
            return
        self._block_in_queue = (opened, next_block, len(self._lines))
        self._lines.append(OutputLine(AstNull(), self.indent_level - 1))
        return

    def get(self) -> OutputGot:
        """Expand all queued AstRoot and return lines.

        Ast's are expanded in the descending order"""
        for idx in range(len(self._queue) - 1, -1, -1):
            i = self._queue[idx]
            if i.expanded:
                del self._queue[idx]
            else:
                self._lines[i.queue_line].line = i.expand()
        return OutputGot(self._lines)

    def get_str(self) -> str:
        out = ''
        for line in self.get():
            if isinstance(line.line, AstNull):
                continue
            out += '\n' + ' ' * (line.indent * KSP.indents) + line.line
        return out[1:]

    def __str__(self) -> str:
        """Return header line and all lines in readable format."""
        out = f'----------Output from {self.__repr__()}----------'
        out += self.get_str()
        out += '\n----------END----------'
        return out


class OutputBlock:
    """Handle indented blocks of code.

    blocks are equal if their open and close strings are equal"""

    __slots__ = 'open_str', 'close_str', 'open', 'close'

    def __init__(self, open_str: str, close_str: str) -> None:
        """Initialize."""
        for string in (open_str, close_str):
            if not isinstance(string, str):
                raise TypeError(
                    'arguments have to be strings, pasted:%s' % (open_str,
                                                                 close_str))
        self.open_str = open_str
        self.close_str = close_str
        self.open = AstString(open_str)
        self.close = AstString(close_str)

    def __eq__(self, other: ty.Any) -> bool:
        """Return True if both strings of blocks are equal."""
        if not isinstance(other, OutputBlock):
            return False
        if self.open_str == other.open_str and\
                self.close_str == other.close_str:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f'OutputBlock ({self.open_str}, {self.close_str})'


class AstBase(KSP, ty.Generic[T]):
    """Abstract base class for all Ast objects."""

    @abstractmethod
    def expand(self) -> str:
        """Recursively expand ast and return summary string."""
        pass

    @abstractmethod
    def get_value(self) -> T:
        """Recursively get runtime value of ast."""
        pass


class AstRootMeta(KSPBaseMeta, ABCMeta):
    """AstRoot metaclass.

    wraps expand() method for setting expanded property to True
    at invocation"""

    def __new__(mcls, name: str,
                bases: ty.Tuple[type, ...],
                namespace: ty.Dict[str, ty.Any]) -> ty.Type['AstRoot']:
        """Wrap expand() method for setting expanded to True."""
        cls = super().__new__(mcls, name, bases, namespace)

        old_expand = getattr(cls, 'expand')

        def expanded_wrapper(self: 'AstRoot') -> str:
            self._expanded = True
            return old_expand(self)

        setattr(cls, 'expand', expanded_wrapper)

        return cls

    def __call__(cls, *args: ty.Any, **kwargs: ty.Any) -> 'AstRoot':
        obj = super().__call__(*args, **kwargs)
        obj._expanded = False
        return obj


class AstRoot(AstBase[T], ty.Generic[T], metaclass=AstRootMeta):
    """Base class for AstRoot (e.g. potential starting of line)."""

    _queue_line: int
    _expanded: bool

    class NullError(Exception):
        """Raise if line is empty."""

        def __init__(self) -> None:
            """Initialize."""
            super().__init__('line is null')

    @property
    def queue_line(self) -> int:
        """Return line of pasting to queue."""
        return self._queue_line

    @queue_line.setter
    def queue_line(self, line: int) -> None:
        """Set line of pasting to queue."""
        if not isinstance(line, int):
            raise TypeError(f'line argument has to be int, pasted: {line}')
        self._queue_line = line

    @property
    def expanded(self) -> bool:
        """Return true, if expand() has been invocated."""
        return self._expanded

    @abstractmethod
    def get_value(self) -> T:
        """Recursively get runtime value of ast."""
        pass


class AstString(AstRoot[str]):
    """Basic string is put to Output."""

    def __init__(self, string: str) -> None:
        """Initialize."""
        if not isinstance(string, str):
            raise TypeError(f'accepts only strings, pasted: {string}')
        self.string = string

    def expand(self) -> str:
        """Return stored string."""
        return self.string

    def get_value(self) -> ty.NoReturn:
        """Raise NullError."""
        raise self.NullError


class AstNull(AstRoot):
    """Placeholder for queued Ast's."""

    def expand(self) -> ty.NoReturn:
        """Raise NullError."""
        raise self.NullError

    def get_value(self) -> ty.NoReturn:
        """Raise NullError."""
        raise self.NullError


class NameBase(KSP):
    """Simple name handler."""

    __slots__ = 'name', 'prefix', 'postfix'

    def __init__(self,
                 name: str,
                 prefix: str='',
                 postfix: str='') -> None:
        """Make separate parts, van be modifyed independently."""
        self.name = name
        self.prefix = prefix
        self.postfix = postfix

    def __call__(self) -> str:
        """Return concatenated prefix, name and postfix."""
        return self.prefix + self.name + self.postfix


class NameVar(NameBase):
    """Variable name, can be hashed."""

    __scope: ty.List[str] = ['']
    __names_full: ty.List[str] = list()
    __names_comp: ty.List[str] = list()

    def __init__(self,
                 name: str,
                 prefix: str='',
                 postfix: str='',
                 preserve: bool=False) -> None:
        """Compacted if flag is set on KSP.

        Full othercase or if preserve is True."""
        name = NameVar.__scope[-1] + name
        if name in NameVar.__names_full:
            raise NameError(f'name "{name}" exists')
        NameVar.__names_full.append(name)
        self._full = name
        if self.compacted_names and not preserve:
            name = self._hash_name(name)
            if name in NameVar.__names_comp:
                raise NameError(
                    f'name "{name}" hashe exists, try to rename')
            NameVar.__names_comp.append(name)
        super().__init__(name, prefix, postfix)

    @property
    def full(self) -> str:
        """Return full name even if it was compacted."""
        return self._full

    @staticmethod
    def _hash_name(name: str) -> str:
        """Hashing function."""
        symbols = 'abcdefghijklmnopqrstuvwxyz012345'
        hname = hashlib.new('sha1')
        hname.update(name.encode('utf-8'))
        compact = ''.join((symbols[ch & 0x1F] for ch
                           in hname.digest()[:5]))
        return compact

    @staticmethod
    def scope(name: str='') -> ty.Optional[str]:
        """Wrap all new declarations within the last put scope.

        if name is not passed, the last scope is removed from list"""
        if not name:
            return NameVar.__scope.pop()
        NameVar.__scope.append(f'{name}_')
        return None

    @staticmethod
    def refresh() -> None:
        """Set all class variables to defaults."""
        NameVar.__names_full = list()
        NameVar.__names_comp = list()


class HasInit(metaclass=KSPBaseMeta):
    """Has method generate_init."""

    @abstractmethod
    def generate_init(self) -> ty.List[str]:
        """Return init lines in lint."""
        pass


class KspObject(KSP):
    """Base class for all objects may appear in code."""

    __slots__ = 'name'

    def __init__(self,
                 name: NameBase,
                 *, has_init: bool) -> None:
        """Excluding Ast's."""
        if isinstance(self, HasInit) and has_init:
            self.append_init(self)
        self.name = name

    @staticmethod
    def generate_inits() -> ty.List[str]:
        """Return all init lines of declared instances."""
        inits = KSP.get_inits()
        lines: ty.List[str] = list()
        for init in inits:
            lines.extend(init.generate_init())
        return lines


class CallbackBase(KSP):
    """Abstract base class for Callbacks."""

    __callbacks: ty.List['CallbackBase']
    __current: 'CallbackBase'
    __id: int

    @abstractmethod
    def add_function(self, function: ty.Callable[[], None]) -> None:
        """Add function to calling queue."""
        pass

    @abstractmethod
    def open(self) -> None:
        """Open callback block and set NI variables to it's values."""
        pass

    @abstractmethod
    def close(self, keep_type: bool=None) -> None:
        """Close callback block and make it init again."""
        pass

    @abstractmethod
    def generate_body(self) -> ty.List[OutputGot]:
        """Return Output lines of invocated functions."""
        pass

    @staticmethod
    @abstractmethod
    def get_all_bodies() -> ty.List[OutputGot]:
        """Collect all bodies of all instantiated callbacks."""
        pass

    @staticmethod
    @abstractmethod
    def refresh() -> None:
        """Set class variables to defaults."""
        pass


ListenerEventType = ty.TypeVar('ListenerEventType', bound='ListenerEventBase')


class EventListener(KSP):
    """Handle events and invocates functions at them."""

    _event_funcs: \
        ty.Dict[ty.Type['ListenerEventBase'],
                ty.Callable[[ListenerEventType], None]]

    def __init__(self) -> None:
        """Initialize."""
        self._event_funcs: \
            ty.Dict[ty.Type['ListenerEventBase'],
                    ty.Callable[[ListenerEventType], None]] = dict()

    def bind_to_event(self,
                      func: ty.Callable[[ListenerEventType], None],
                      event: ty.Type['ListenerEventBase']) -> None:
        """Bind function to event type.

        function will be invocated at every event of the type."""
        self._event_funcs[event] = func

    def put_event(self, event: 'ListenerEventBase') -> None:
        """Invocate event function if any."""
        for event_type in self._event_funcs:
            if isinstance(event, event_type):
                self._event_funcs[event_type](event)
                return


class ListenerEventBase:
    """Placeholder."""

    pass
