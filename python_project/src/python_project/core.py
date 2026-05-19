"""核心业务逻辑示例模块。"""

from __future__ import annotations


def greet(name: str = "World") -> str:
    """返回一个问候字符串。

    Args:
        name: 要问候的对象名称，默认 "World"。

    Returns:
        形如 "Hello, <name>!" 的问候语。

    Raises:
        ValueError: 当 ``name`` 为空字符串时抛出。
    """
    if not name:
        raise ValueError("name 不能为空字符串")
    return f"Hello, {name}!"
