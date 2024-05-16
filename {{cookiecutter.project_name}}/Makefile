.PHONY: lint
lint:
	docker compose run --rm --entrypoint=pylint test /src/{{cookiecutter.project_name}}

.PHONY: typecheck
typecheck:
	docker compose run --rm test --mypy /src/{{cookiecutter.project_name}}

.PHONY: test
test:
	docker compose run --rm test --disable-pytest-warnings /src/{{cookiecutter.project_name}}

.PHONY: dist
dist:
	pip install wheel build
	python -m build
