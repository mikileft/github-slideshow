"""cli 模块的单元测试。"""

from __future__ import annotations

import pytest

from python_project.cli import main


def test_cli_default(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main([])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "Hello, World!"


def test_cli_with_name(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["--name", "Cursor"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "Hello, Cursor!"
