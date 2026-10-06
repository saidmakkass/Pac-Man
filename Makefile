
NAME = pac-man.py
CONFIG_FILE = config.json

install:
	@uv sync

run:
	@uv run python3 $(NAME) $(CONFIG_FILE)

debug:
	@uv run python3 -m pdb $(NAME) $(CONFIG_FILE)

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".mypy_cache" -exec rm -rf {} +


.PHONY: install run debug lint clean
