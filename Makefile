install:
	poetry install

gendiff:
	poetry run python -m gendif.scripts.gendif

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*whl

package-reinstall:
	pip install --user --forse-reinstall dist/*.whl

uninstall:
	python3 -m pip uninstall hexlet-code