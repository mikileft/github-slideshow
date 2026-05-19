.PHONY: help install lint format test typecheck all clean

PYTHON ?= python

help:
	@echo "可用命令:"
	@echo "  make install    安装项目和开发依赖（editable 模式）"
	@echo "  make lint       使用 ruff 进行静态检查"
	@echo "  make format     使用 ruff 自动格式化代码"
	@echo "  make typecheck  使用 mypy 进行类型检查"
	@echo "  make test       运行 pytest 测试套件"
	@echo "  make all        一次执行 lint + typecheck + test"
	@echo "  make clean      清理构建和缓存产物"

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e ".[dev]"

lint:
	ruff check .

format:
	ruff format .
	ruff check --fix .

typecheck:
	mypy

test:
	pytest

all: lint typecheck test

clean:
	rm -rf build dist *.egg-info .pytest_cache .ruff_cache .mypy_cache htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
