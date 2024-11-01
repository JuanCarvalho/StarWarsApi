# Para rodar os testes, execute:
# make

all: testing black isort lint mypy
	@echo
	@echo "\033[0;32m All Validations Done! \033[0m"
	@echo

testing:
	@echo
	@echo "Running unit tests..."
	pytest -vv -W ignore::DeprecationWarning --ignore=app/test/full_test
	@echo

black:
	@echo
	@echo "Running black..."
	black --line-length 140 .
	@echo

lint:
	@echo
	@echo "Running flake8..."
	flake8p .
	@echo

isort:
	@echo
	@echo "Running isort..."
	isort . --line-length 140
	@echo

mypy:
	@echo
	@echo "Running mypy..."
	mypy .
	@echo


