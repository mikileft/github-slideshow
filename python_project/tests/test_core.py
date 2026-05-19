"""core 模块的单元测试。"""

from __future__ import annotations

import pytest

from python_project.core import greet


def test_greet_default() -> None:
    assert greet() == "Hello, World!"


def test_greet_with_name() -> None:
    assert greet("Cursor") == "Hello, Cursor!"


def test_greet_empty_name_raises() -> None:
    with pytest.raises(ValueError, match="name 不能为空字符串"):
        greet("")
