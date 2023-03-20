from game.character import GameCharacter
from typing import Callable, Any

# 这里小写是应为， 这个不是常量，而是一个变量
character_creation_funcs: dict[str, Callable[..., GameCharacter]] = {}

# 下面两个方法是用来操作character_craetion_func
# 为什么不用类， 是因为不用类就不需要考虑初始化
def register(character_type: str, creation_func: Callable[..., GameCharacter]):
    """Register a new game character type"""
    character_creation_funcs[character_type] = creation_func


def unregister(character_type: str):
    """Unregister a game character"""
    character_creation_funcs.pop(character_type, None)


def create(arguments: dict[str, Any]) -> GameCharacter:
    """Create a game character of a specific type, given a dictionary of arguments。"""
    args_copy = arguments.copy()  # 如果要改动输入的元素，常见的方式是做一个浅拷贝
    character_type = args_copy.pop("type")  # make sure the key exists, or raise key error
    try:
        creation_func = character_creation_funcs[character_type]
        return creation_func(**args_copy)  # 这里不需要type这个key, 这里注意json中的结构, type不是创建对象所需要的key，这是一种反序列化的常用写法
    except KeyError:
        raise ValueError(f"Unknown character type {character_type!r}") from None # !r 表示打印是 repr(), !s 表示打印的是str()
        # 这里解释了为什么用 from None 语法 https://stefan.sofa-rockers.org/2020/10/28/raise-from/
        # 查看在vscode中是否有pylint， mypy，pylint2.6提示 raise exception from None





