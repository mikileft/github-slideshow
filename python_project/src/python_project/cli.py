"""命令行入口。"""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from python_project import __version__
from python_project.core import greet


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python_project",
        description="一个示例命令行工具，演示项目结构。",
    )
    parser.add_argument(
        "-n",
        "--name",
        default="World",
        help="要问候的名字 (默认: %(default)s)",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
