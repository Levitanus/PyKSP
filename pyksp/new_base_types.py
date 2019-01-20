from typing import TypeVar
from typing import Type
from typing import List
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import Any
from typing import NoReturn
from typing import Callable
from typing import ClassVar
from typing import Set
from typing import Sequence
from typing import cast
from typing import Union
from typing import NewType
from typing import Generic
from typing import overload
# from typing import Protocol
# from typing import runtime
from abc import ABCMeta
from abc import abstractmethod

if __name__ == '__main__':
    __name__ = 'pyksp.new_base_types'

from .new_abstract import KspObject
from .new_abstract import NameBase
from .new_abstract import NameVar
from .new_abstract import AstRoot
from .new_abstract import AstString
from .new_abstract import AstBase
from .new_abstract import HasInit

from .new_abstract import KSP


T = TypeVar('T')
KT = TypeVar('KT', int, float, str)
KVT = TypeVar('KVT', bound='KspVar')
NT = TypeVar('NT', int, float)
# AT = TypeVar('AT', bound='KspVar[KT]')

ATU = Union['KspVar[KT]', 'AstBase[KT]', 'Magic[KT]', KT]
STU = Union['KspVar[KT]', 'AstBase[KT]', 'Magic[KT]', str]
NTU = Union['KspVar[NT]', 'AstBase[NT]', 'ProcessNum[NT]', NT]
NotVarNTU = Union['AstBase[NT]', 'ProcessNum[NT]', NT]


@overload
def get_value(value: ATU[int]) -> int:
    ...


@overload
def get_value(value: ATU[str]) -> str:
    ...


@overload
def get_value(value: ATU[float]) -> float:
    ...


def get_value(value: ATU[KT]) -> KT:
    if isinstance(value, (int, str, float)):
        return value
    if isinstance(value, KspVar):
        return value._value
    if isinstance(value, AstBase):
        return value.get_value()
    raise TypeError(f"Can't infer type of {value}")


@overload
def get_compiled(value: ATU[int]) -> str:
    ...


@overload
def get_compiled(value: ATU[str]) -> str:
    ...


@overload
def get_compiled(value: ATU[float]) -> str:
    ...


def get_compiled(value: ATU[KT]) -> str:
    if isinstance(value, (int, float)):
        return f'{value}'
    if isinstance(value, str):
        return f'"{value}"'
    if isinstance(value, KspVar):
        return value.name()
    if isinstance(value, AstBase):
        return value.expand()
    raise TypeError(f"Can't infer type of {value}")


def get_value_type(value: ATU[KT]) -> Type[KT]:
    checked = get_value(value)
    c_type = type(checked)
    assert c_type in (int, str, float), f'can not infer type of {value}'
    return c_type


class Magic(KSP, Generic[KT]):
    ...


class ConcatsStrings(Magic[str]):

    def __add__(self, other: STU) -> 'AstConcatString':
        return AstConcatString(self, other)

    def __radd__(self, other: STU) -> 'AstConcatString':
        return AstConcatString(self, other)


class AstConcatString(AstBase[str], ConcatsStrings):

    def __init__(self, arg1: STU, arg2: STU) -> None:
        self._ref_type = str
        self.arg1 = arg1
        self.arg2 = arg2

    def expand(self) -> str:
        return f'{get_compiled(self.arg1)} & {get_compiled(self.arg2)}'

    def get_value(self) -> str:
        return str(get_value(self.arg1)) + str(get_value(self.arg2))


FT = TypeVar('FT', bound=Callable[..., Any])


def ducktype_num_magic(method: FT) -> FT:

    def wrpapper(self: 'ProcessNum[NT]', other: NTU[NT]) -> Any:
        other = self._check_for_int(other)  # type: ignore
        value = get_value(other)
        if not isinstance(value, self._ref_type):
            raise TypeError(
                f'incompatible type: {type(other)}' +
                f'-> {NTU[self._ref_type]}')   # type: ignore
        return method(self, other)
    return cast(FT, wrpapper)


class ProcessNum(Magic[NT], Generic[NT]):
    _ref_type: Type[NT]

    def _check_for_int(self, other: NTU[NT]) -> Union[NTU[NT], float]:
        if isinstance(other, int) and issubclass(self._ref_type, float):
            return float(other)
        return other

    def __neg__(self) -> 'AstNeg[NT]':
        return AstNeg(self)

    def __invert__(self) -> 'AstNot':
        if not issubclass(self._ref_type, int):
            raise TypeError('can only be apllied to int expression' +
                            f'pasted {self} ({type(self)})')
        return AstNot(self)

    @ducktype_num_magic
    def __add__(self, other: NTU[NT]) -> 'AstAdd[NT]':
        return AstAdd(self, other)

    @ducktype_num_magic
    def __radd__(self, other: NTU[NT]) -> 'AstAdd[NT]':
        return AstAdd(other, self)

    @ducktype_num_magic
    def __sub__(self, other: NTU[NT]) -> 'AstSub[NT]':
        return AstSub(self, other)

    @ducktype_num_magic
    def __rsub__(self, other: NTU[NT]) -> 'AstSub[NT]':
        return AstSub(other, self)

    @ducktype_num_magic
    def __mul__(self, other: NTU[NT]) -> 'AstMul[NT]':
        return AstMul(self, other)

    @ducktype_num_magic
    def __rmul__(self, other: NTU[NT]) -> 'AstMul[NT]':
        return AstMul(other, self)

    @ducktype_num_magic
    def __truediv__(self, other: NTU[NT]) -> 'AstDiv[NT]':
        return AstDiv(self, other)

    @ducktype_num_magic
    def __rtruediv__(self, other: NTU[NT]) -> 'AstDiv[NT]':
        return AstDiv(other, self)

    def __mod__(self, other: NTU[int]) -> 'AstMod':
        if not issubclass(self._ref_type, int):
            raise TypeError('can only be apllied to int expression' +
                            f'pasted {other} ({type(other)})')
        return AstMod(self, other)

    def __rmod__(self, other: NTU[int]) -> 'AstMod':
        if not issubclass(self._ref_type, int):
            raise TypeError('can only be apllied to int expression' +
                            f'pasted {other} ({type(other)})')
        return AstMod(other, self)

    def __pow__(self, other: NTU[float]) -> 'AstPow':
        if not issubclass(self._ref_type, float):
            raise TypeError('can only be apllied to float expression' +
                            f'pasted {other} ({type(other)})')
        return AstPow(self, other)  # type: ignore

    def __rpow__(self, other: NTU[float]) -> 'AstPow':
        if not issubclass(self._ref_type, float):
            raise TypeError('can only be apllied to float expression' +
                            f'pasted {other} ({type(other)})')
        return AstPow(other, self)  # type: ignore

    def __and__(self, other: NTU[NT]) -> 'AstAnd[NT]':
        return AstAnd(self, other)

    def __rand__(self, other: NTU[NT]) -> 'AstAnd[NT]':
        return AstAnd(other, self)

    def __or__(self, other: NTU[NT]) -> 'AstOr[NT]':
        return AstOr(self, other)

    def __ror__(self, other: NTU[NT]) -> 'AstOr[NT]':
        return AstOr(other, self)

    @ducktype_num_magic
    def __eq__(self, other: NTU[NT]) -> 'AstEq[NT]':  # type: ignore
        return AstEq(self, other)

    @ducktype_num_magic
    def __ne__(self, other: NTU[NT]) -> 'AstNe[NT]':  # type: ignore
        return AstNe(self, other)

    @ducktype_num_magic
    def __lt__(self, other: NTU[NT]) -> 'AstLt[NT]':
        return AstLt(self, other)

    @ducktype_num_magic
    def __gt__(self, other: NTU[NT]) -> 'AstGt[NT]':
        return AstGt(self, other)

    @ducktype_num_magic
    def __le__(self, other: NTU[NT]) -> 'AstLe[NT]':
        return AstLe(self, other)

    @ducktype_num_magic
    def __ge__(self, other: NTU[NT]) -> 'AstGe[NT]':
        return AstGe(self, other)

    def __abs__(self) -> 'AstAbs[NT]':
        return AstAbs(self)

    def __int__(self) -> 'AstInt':
        if not issubclass(self._ref_type, float):
            raise TypeError('availble only for KSP float expression')
        return AstInt(self)  # type: ignore

    def __float__(self) -> 'AstFloat':
        if not issubclass(self._ref_type, int):
            raise TypeError('availble only for KSP int expression')
        return AstFloat(self)

    def __lshift__(self, other: NTU[int]) -> 'AstLshift':
        if not issubclass(self._ref_type, int):
            raise TypeError('availble only for KSP int expression')
        return AstLshift(self, other)

    def __rlshift__(self, other: NTU[int]) -> 'AstLshift':
        if not issubclass(self._ref_type, int):
            raise TypeError('availble only for KSP int expression')
        return AstLshift(other, self)

    def __rshift__(self, other: NTU[int]) -> 'AstRshift':
        if not issubclass(self._ref_type, int):
            raise TypeError('availble only for KSP int expression')
        return AstRshift(self, other)

    def __rrshift__(self, other: NTU[int]) -> 'AstRshift':
        if not issubclass(self._ref_type, int):
            raise TypeError('availble only for KSP int expression')
        return AstRshift(other, self)


class AstOperatorUnary(AstBase[NT], ProcessNum[NT]):
    arg1: NTU[NT]
    string: ClassVar[str]
    priority: ClassVar[int]

    def __init__(self, arg1: NTU[NT]) -> None:
        self._ref_type = get_value_type(arg1)
        self.arg1: NTU[NT] = arg1
        self.arg1_pure: NT = get_value(arg1)
        self.arg1_str: str = get_compiled(arg1)


class AstOperatorUnaryStandart(AstOperatorUnary[NT]):

    def expand(self) -> str:
        return f'{self.string}{self.arg1_str}'


class AstOperatorDouble(AstOperatorUnary[NT]):
    arg2: NTU[NT]

    def __init__(self, arg1: NTU[NT], arg2: NTU[NT]) -> None:
        super().__init__(arg1)  # type: ignore
        self.arg2 = arg2
        self.arg2_pure: NT = get_value(arg2)
        self.arg2_str: str = get_compiled(arg2)


class AstOperatorDoubleStandart(AstOperatorDouble[NT]):

    def _expand_with_string(self, string: str) -> str:
        pr: List[int] = list()
        for arg in (self.arg1, self.arg2):
            if isinstance(arg, AstOperatorUnary):
                pr.append(arg.priority)
                continue
            pr.append(0)
        if self.priority <= pr[1]:
            self.arg2_str = f'({self.arg2_str})'
        if self.priority < pr[0]:
            self.arg1_str = f'({self.arg1_str})'
        return f'{self.arg1_str} {string} {self.arg2_str}'

    def expand(self) -> str:
        return self._expand_with_string(self.string)


class AstOperatorUnaryBracket(AstOperatorUnary[NT]):

    def expand(self) -> str:
        return f'{self.string}({self.arg1_str})'


class AstOperatorDoubleBracket(AstOperatorDouble[NT]):

    def expand(self) -> str:
        return f'{self.string}({self.arg1_str}, {self.arg2_str})'


class AstBool(AstBase[NT]):

    @abstractmethod
    def __bool__(self) -> bool:
        ...


class AstCanBeBool(AstOperatorDoubleStandart[NT], AstBool[NT]):
    string_bool: ClassVar[str]

    def expand_bool(self) -> str:
        return self._expand_with_string(self.string_bool)


class AstNeg(AstOperatorUnaryStandart[NT]):
    priority = 2
    string = '-'

    def get_value(self) -> NT:
        return -self.arg1_pure


class AstNot(AstOperatorUnaryStandart[int]):
    priority = 2
    string = '.not.'

    def get_value(self) -> int:
        assert issubclass(self._ref_type, int)
        return ~self.arg1_pure


class AstAbs(AstOperatorUnaryBracket[NT]):
    priority = 2
    string = 'abs'

    def get_value(self) -> NT:
        return abs(self.arg1_pure)


class AstInt(AstOperatorUnaryBracket[float]):
    priority = 2
    string = 'int_to_real'

    def get_value(self) -> int:  # type: ignore
        return int(self.arg1_pure)


class AstFloat(AstOperatorUnaryBracket[int]):
    priority = 2
    string = 'real_to_int'

    def get_value(self) -> float:  # type: ignore
        return float(self.arg1_pure)


class AstAdd(AstOperatorDoubleStandart[NT]):
    priority = 4
    string = '+'

    def get_value(self) -> NT:
        return self.arg1_pure + self.arg2_pure


class AstSub(AstOperatorDoubleStandart[NT]):
    priority = 4
    string = '-'

    def get_value(self) -> NT:
        return self.arg1_pure - self.arg2_pure


class AstDiv(AstOperatorDoubleStandart[NT]):
    priority = 3
    string = '/'

    def get_value(self) -> NT:
        try:
            if isinstance(self.arg1_pure, int):
                return self.arg1_pure // self.arg2_pure
            else:
                return self.arg1_pure / self.arg2_pure
        except ZeroDivisionError:
            return 0


class AstMul(AstOperatorDoubleStandart[NT]):
    priority = 3
    string = '*'

    def get_value(self) -> NT:
        return self.arg1_pure * self.arg2_pure


class AstMod(AstOperatorDoubleStandart[int]):
    priority = 3
    string = 'mod'

    def get_value(self) -> int:
        return self.arg1_pure % self.arg2_pure


class AstPow(AstOperatorDoubleBracket[float]):
    priority = 1
    string = 'pow'

    def get_value(self) -> float:
        return self.arg1_pure ** self.arg2_pure


class AstLshift(AstOperatorDoubleBracket[int]):
    priority = 5
    string = 'sh_left'

    def get_value(self) -> int:
        return self.arg1_pure << self.arg2_pure


class AstRshift(AstOperatorDoubleBracket[int]):
    priority = 5
    string = 'sh_right'

    def get_value(self) -> int:
        return self.arg1_pure >> self.arg2_pure


class AstAnd(AstCanBeBool[NT]):
    priority = 8
    string = '.and.'
    string_bool = 'and'

    def get_value(self) -> NT:
        assert issubclass(self._ref_type, int)
        return self.arg1_pure & self.arg2_pure

    def __bool__(self) -> bool:
        if self.arg1 and self.arg2:
            return True
        return False


class AstOr(AstCanBeBool[NT]):
    priority = 8
    string = '.or.'
    string_bool = 'or'

    def get_value(self) -> NT:
        assert issubclass(self._ref_type, int)
        return self.arg1_pure | self.arg2_pure

    def __bool__(self) -> bool:
        if self.arg1 or self.arg2:
            return True
        return False


class OperatorComparisson(AstOperatorDoubleStandart[NT], AstBool[NT]):

    def get_value(self) -> NoReturn:
        raise NotImplementedError


class AstEq(OperatorComparisson[NT]):
    priority = 7
    string = '='

    def __bool__(self) -> bool:
        if self.arg1_pure == self.arg2_pure:
            return True
        return False


class AstNe(OperatorComparisson[NT]):
    priority = 7
    string = '#'

    def __bool__(self) -> bool:
        if self.arg1_pure != self.arg2_pure:
            return True
        return False


class AstLt(OperatorComparisson[NT]):
    priority = 7
    string = '<'

    def __bool__(self) -> bool:
        if self.arg1_pure < self.arg2_pure:
            return True
        return False


class AstGt(OperatorComparisson[NT]):
    priority = 7
    string = '>'

    def __bool__(self) -> bool:
        if self.arg1_pure > self.arg2_pure:
            return True
        return False


class AstLe(OperatorComparisson[NT]):
    priority = 7
    string = '<='

    def __bool__(self) -> bool:
        if self.arg1_pure <= self.arg2_pure:
            return True
        return False


class AstGe(OperatorComparisson[NT]):
    priority = 7
    string = '>='

    def __bool__(self) -> bool:
        if self.arg1_pure >= self.arg2_pure:
            return True
        return False


class KspVar(KspObject, HasInit, Generic[KT]):
    names_count: int = 0

    class Persist:
        """Class for mark persistence of variable.

        can be:
        KspVar.not_persistent
        KspVar.persistent
        KspVar.inst_persistent
        KspVar.read_persistent"""

        def __init__(self, line: str='') -> None:
            self.line = line

    not_persistent: ClassVar[Persist] = Persist()
    persistent: ClassVar[Persist] = Persist('make_persistent')
    inst_persistent: ClassVar[Persist] = Persist('make_instr_persistent')
    read_persistent: ClassVar[Persist] = Persist('make_persistent')

    def __init__(self,
                 value: KT,
                 name: str='',
                 persist: Persist=not_persistent,
                 preserve_name: bool=False,
                 *, local: bool=False) -> None:
        if local:
            assert name
            sup_name = NameBase(name)
            has_init = False
        else:
            if not name:
                name = f'Var{KspVar.names_count}'
                KspVar.names_count += 1
            sup_name = NameVar(name, preserve=preserve_name)
            has_init = True
        super().__init__(sup_name, has_init=has_init)
        self._value: KT = value
        if isinstance(value, int):
            self.name.prefix = '$'
        elif isinstance(value, str):
            self.name.prefix = '@'
        elif isinstance(value, float):
            self.name.prefix = '~'
        else:
            raise TypeError(f"Can't infer type of value {value}")
        self._ref_type: Type[KT] = type(value)
        self._init_val: KT = value
        self._persist: KspVar.Persist = persist

    @abstractmethod
    def get_decl_line(self) -> List[str]:
        ...

    def generate_init(self) -> List[str]:
        out = self.get_decl_line()
        if self._persist is not self.not_persistent:
            out.append(f'{self._persist.line}({self.name()})')
        if self._persist is self.read_persistent:
            out.append(f'read_persistent_var({self.name()})')

        return out

    @property
    def val(self) -> KT:
        return self._value

    def read(self) -> None:
        self._persist = self.persistent
        out = self.get_out()
        out.put_immediatly(AstString(f'read_persistent_var({self.name()})'))

    @abstractmethod
    def __ilshift__(self: KVT, other: ATU) -> KVT:
        ...

    def copy(self: KVT, name: str, prefix: str, postfix: str) -> KVT:
        obj = self.__class__(self._value, name=name, local=True)
        obj.name.prefix = prefix
        obj.name.postfix = postfix
        return obj


class Str(KspVar[str], ConcatsStrings):

    def __ilshift__(self, other: STU) -> 'Str':
        if not isinstance(other, (KspVar, AstBase, str)):
            raise TypeError('incompatible type for assignement: ' +
                            f'{type(other)} -> {STU}')  # type: ignore
        value = get_value(other)
        if not isinstance(value, str):
            value = f'{value}'
        name = self.name.name
        prefix = self.name.prefix
        postfix = self.name.postfix
        if isinstance(other, Str):
            ret_obj = other.copy(name, prefix, postfix)
            ret_obj._value = value
        else:
            ret_obj = Str(value, name, local=True)
            ret_obj.name.prefix = prefix
            ret_obj.name.postfix = postfix

        otpt = self.get_out()
        otpt.put_immediatly(AstAssign(self, other))

        return ret_obj

    def get_decl_line(self) -> List[str]:
        out = [f'declare {self.name()}']
        if self._init_val:
            out.append(f'{self.name()} := {self._init_val}')
        return out

    def __iadd__(self, other: STU) -> 'Str':  # type: ignore
        return self.__ilshift__(AstConcatString(self, other))


class Num(KspVar[NT], ProcessNum[NT]):

    def __ilshift__(self, other: ATU[NT]) -> 'Num[NT]':
        other = self._check_for_int(other)  # type: ignore
        value = get_value(other)
        assert isinstance(value, self._ref_type), \
            f'assigned to a value of wrong type: {value}'
        name = self.name.name
        prefix = self.name.prefix
        postfix = self.name.postfix
        if isinstance(other, Num):
            ret_obj = other.copy(name, prefix, postfix)
            ret_obj._value = value
        else:
            ret_obj = Num(value, name, local=True)
            ret_obj.name.prefix = prefix
            ret_obj.name.postfix = postfix

        otpt = self.get_out()
        otpt.put_immediatly(AstAssign(self, other))

        return ret_obj

    def get_decl_line(self) -> List[str]:
        value = ''
        if self._init_val:
            value = f' := {self._init_val}'
        out = [f'declare {self.name()}{value}']
        return out

    @ducktype_num_magic
    def __iadd__(self, other: NTU[NT]) -> 'Num[NT]':  # type: ignore
        return self.__ilshift__(AstAdd(self, other))

    @ducktype_num_magic
    def __isub__(self, other: NTU[NT]) -> 'Num[NT]':  # type: ignore
        return self.__ilshift__(AstSub(self, other))

    @ducktype_num_magic
    def __imul__(self, other: NTU[NT]) -> 'Num[NT]':  # type: ignore
        return self.__ilshift__(AstMul(self, other))

    @ducktype_num_magic
    def __itruediv__(self, other: NTU[NT]) -> 'Num[NT]':  # type: ignore
        return self.__ilshift__(AstDiv(self, other))

    @ducktype_num_magic
    def __imod__(self, other: NTU[int]) -> 'Num[int]':  # type: ignore
        if not issubclass(self._ref_type, int):
            raise TypeError('availble only for KSP int expression')
        return self.__ilshift__(AstMod(self, other))

    @ducktype_num_magic
    def __ipow__(self, other: NTU[float]) -> 'Num[float]':  # type: ignore
        if not issubclass(self._ref_type, float):
            raise TypeError('availble only for KSP float expression')
        return self.__ilshift__(AstPow(self, other))  # type: ignore

    def __iand__(self, other: NTU[NT]) -> NoReturn:
        raise NotImplementedError

    def __ior__(self, other: NTU[NT]) -> NoReturn:
        raise NotImplementedError


def inc(var: Num[int]) -> None:
    if not isinstance(var, Num):
        raise TypeError(f'can only be used with {Num[int]}')
    if not issubclass(get_value_type(var), int):
        raise TypeError(f'can only be used with {Num[int]}')
    out = var.get_out()
    out.put_immediatly(AstBuiltInBase(None, 'inc', var))
    var._value += 1


def dec(var: Num[int]) -> None:
    if not isinstance(var, Num):
        raise TypeError(f'can only be used with {Num[int]}')
    if not issubclass(get_value_type(var), int):
        raise TypeError(f'can only be used with {Num[int]}')
    out = var.get_out()
    out.put_immediatly(AstBuiltInBase(None, 'dec', var))
    var._value -= 1


class AstAssign(AstRoot):

    def __init__(self, to_arg: 'KspVar', from_arg: ATU) -> None:
        self.to_arg: 'KspVar' = to_arg
        self.from_arg: ATU = from_arg

    def expand(self) -> str:
        to = self.to_arg.name()
        if isinstance(self.from_arg, (int, float)):
            from_str = f'{self.from_arg}'
        elif isinstance(self.from_arg, str):
            from_str = f'"{self.from_arg}"'
        elif isinstance(self.from_arg, KspVar):
            from_str = self.from_arg.name()
        elif isinstance(self.from_arg, AstBase):
            from_str = self.from_arg.expand()
        else:
            raise TypeError(f"Can't infer type of value {self.from_arg}")
        return f'{to} := {from_str}'

    def get_value(self) -> NoReturn:
        raise self.NullError


class AstBuiltInBase(AstRoot, AstBase[KT]):
    _ref_type: Optional[Type[KT]]
    _value: Optional[KT]
    args: List[str]
    string: str

    def __init__(self, ret_val: Optional[KT], string: str, *args: ATU) -> None:
        if ret_val is not None:
            self._ref_type = get_value_type(ret_val)
        else:
            self._ref_type = None
        self._value: Optional[KT] = ret_val
        self.args: List[str] = list(map(get_compiled, args))
        self.string = string

    def expand(self) -> str:
        return f'{self.string}({", ".join(self.args)})'

    def get_value(self) -> KT:
        if self._value is None:
            raise self.NullError
        return self._value


out = KSP.new_out()
a = Str('3')
# get_value(1)
# get_value('s')


b = Num(4, name='b', local=True)
get_value(b)
c = Num(5)
print(b.name())
b <<= c
print(b, b.val, b.name())
b <<= 15
# a <<= 3

if b == c:
    print('True')
else:
    print(False)

d = Num(4.1, 'd')
# reveal_type(d)
d <<= 3
print(d.val)
get_value(d)
# reveal_type(d)
# b <<= 3.1
# d <<= b
d <<= -d
# reveal_type(-d)
inc(b)
# inc(d)
dec(b)

c += b
c <<= b / (2 + b)
c <<= b << 2 * (15 / b)
print(f'c = {c.val}')
# c <<= b // c

print(str(out))
