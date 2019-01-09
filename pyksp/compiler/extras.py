from .abstract import Output
from .abstract import KSP
from .abstract import IName

from .script import kScript
from .functions import kLocals

from typing import Union
from typing import List
from typing import Optional
from typing import Callable
from typing import cast
from typing import Any
from typing import TypeVar

from functools import wraps
from inspect import cleandoc

from re import sub


def docstring(f):
    """Decorator for placing docastrings as comments to code
    docstring will be placed at the function invocation place
    if script docs attribute is set to True"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not KSP.docs:
            return f(*args, **kwargs)
        Output().put('{%s}' % f.__doc__)
        # if not KSP.indents:
        #     Output().put('{%s}' % f.__doc__)
        #     return
        # comm = cleandoc(f.__doc__).split('\n')
        # new = comm[0]
        # if len(comm) > 1:
        #     for line in comm[1:]:
        #         new += f'\n{" " * KSP.indents}{line}'
        # Output().put('{%s}' % new)
        return f(*args, **kwargs)

    return wrapper


def scope(f):
    """Decorator for making all Ksp declarations 'local'
    adds current scope to the declaration name"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        # print(dir(f))
        scope = f'{f.__module__}_{f.__qualname__}_'
        scope = sub(r'(__init__)|[<>]', '', scope)
        scope = sub(r'\.', '_', scope)
        IName.scope(scope)
        ret_val = f(*args, **kwargs)
        IName.scope('')
        return ret_val

    return wrapper


def scope_with_locals(local: kLocals):

    def scope(f):
        """Decorator for making all Ksp declarations 'local'
        adds current scope to the declaration name"""
        @wraps(f)
        def wrapper(*args, **kwargs):
            # print(dir(f))
            scope = f'{f.__module__}_{f.__qualname__}_'
            scope = sub(r'(__init__)|[<>]', '', scope)
            scope = sub(r'\.', '_', scope)
            IName.scope(scope)
            ret_val = f(*args, **kwargs)
            IName.scope('')
            return ret_val

        return wrapper
    local.init_vars()
    return scope


def comment(comment: str):
    """Place comment to the result code
    comment will be placed if script docs attribute is set to True"""
    if not KSP.docs:
        return
    comm: Union[str, List[str]]
    if not KSP.indents:
        Output().put('{%s}' % comment)
        return
    # Output().put('{%s}' % cleandoc(comment))
    comm = cleandoc(comment).split('\n')
    new = comm[0]
    if len(comm) > 1:
        for line in comm[1:]:
            new += f'\n{" " * KSP.indents}{line}'
    Output().put('{%s}' % new)


F = TypeVar('F', bound=Callable[..., None])


def quick_script(f: F) -> F:

    @wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        script = kScript(kScript.clipboard,
                         compact=False,
                         max_line_length=70,
                         indents=2)
        setattr(script, 'main', lambda: f(*args, **kwargs))
        script.compile()

    return cast(F, wrapper)
