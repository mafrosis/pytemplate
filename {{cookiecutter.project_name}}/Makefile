.PHONY: lint
lint:
	docker compose run --rm --entrypoint=pylint test /src/{{cookiecutter.project_name}}

.PHONY: typecheck
typecheck:
	docker compose run --rm test --mypy /src/{{cookiecutter.project_name}}

.PHONY: dist
dist:
	pip install wheel build
	python -m build
