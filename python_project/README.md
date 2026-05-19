# python_project

一个使用现代 Python 最佳实践初始化的项目模板。

## 特性

- **`src/` 布局**：避免 import 路径混乱，更适合打包分发。
- **`pyproject.toml`**：单一配置文件（PEP 517/518/621），无需 `setup.py` 或 `setup.cfg`。
- **构建后端**：使用 [Hatchling](https://hatch.pypa.io/)。
- **代码风格 & Lint**：[Ruff](https://docs.astral.sh/ruff/)（同时替代 black、isort、flake8）。
- **类型检查**：[Mypy](https://mypy-lang.org/)（已配置为严格模式）。
- **测试**：[Pytest](https://docs.pytest.org/) + `pytest-cov` 覆盖率。
- **命令行入口**：通过 `[project.scripts]` 暴露 `python_project` 命令。

## 项目结构

```text
python_project/
├── pyproject.toml          # 项目元数据、依赖、工具配置
├── README.md
├── .gitignore
├── Makefile                # 常用命令快捷方式
├── src/
│   └── python_project/
│       ├── __init__.py
│       ├── core.py         # 业务逻辑示例
│       └── cli.py          # 命令行入口
└── tests/
    ├── __init__.py
    └── test_core.py
```

## 快速开始

### 1. 创建并激活虚拟环境

```bash
cd python_project
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 2. 安装项目（开发模式 + 开发依赖）

```bash
pip install -e ".[dev]"
```

### 3. 运行命令行工具

```bash
python_project --name 世界
# 或者
python -m python_project.cli --name 世界
```

### 4. 运行测试

```bash
pytest
```

### 5. 代码检查与格式化

```bash
ruff check .          # 静态检查
ruff format .         # 自动格式化
mypy                  # 类型检查
```

也可以使用 `Makefile` 一键执行：

```bash
make install   # 安装依赖
make lint      # 检查代码
make format    # 格式化代码
make test      # 运行测试
make all       # 一次执行 lint + test
```

## 许可证

MIT
