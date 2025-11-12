.PHONY: lint
lint:
	 poetry run mypy \
		--check-untyped-defs \
		src/typedre

.PHONY: format
format:
	poetry run isort \
		--tc \
		--profile=black \
		src/typedre
	poetry run black \
		src/typedre

.PHONY: formatcheck
formatcheck:
	poetry run isort \
		--tc \
		--profile black \
		--check-only \
		src/typedre
	poetry run black \
		--check \
		src/typedre

.PHONY: test
test:
	poetry run pytest \
		tests
