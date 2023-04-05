.PHONY: pre-commit
pre-commit:
	pip install pre-commit && pre-commit install && pre-commit autoupdate

