# Project

This is hooks for python projects. Use with pre-commit

## How to add hooks

- `make pre-commit`
- add your hooks to python_hooks/\_\_init__.py
- Add entry point to your hooks in pyproject.toml `[project.scripts]`
- commit and push your changes


## How to use in your project:

- requirements.txt: `api-session @ git+http://git@gitlab.com/tabby.ai/testing/tools/python-hooks`
- install with pip: `pip install git+https://gitlab.com/tabby.ai/testing/tools/python-hooks`
- add hook into your pre-commit file as:
              
```repos:
    - repo: local
      hooks:
          id: python_hooks
          name: python_hooks
          entry: prepare_commit_msg
          language: system
