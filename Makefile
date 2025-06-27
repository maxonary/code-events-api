.PHONY: help install install-dev test test-cov lint format clean run run-docker build docker-up docker-down generate-requirements

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install production dependencies
	uv pip install -e .

install-dev: ## Install development dependencies
	uv pip install -e ".[dev]"
	pre-commit install

test: ## Run tests
	pytest

test-cov: ## Run tests with coverage
	pytest --cov=app --cov-report=html --cov-report=term-missing

lint: ## Run linting checks
	flake8 app tests
	mypy app

format: ## Format code with black and isort
	black app tests
	isort app tests

clean: ## Clean up generated files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .coverage htmlcov dist build

run: ## Run the development server
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

run-docker: ## Run with Docker Compose
	docker-compose up --build

build: ## Build Docker image
	docker build -t campus-event-organizer .

docker-up: ## Start Docker services
	docker-compose up -d

docker-down: ## Stop Docker services
	docker-compose down

setup: ## Initial setup for new developers
	python scripts/setup_dev.py

check: ## Run all checks (format, lint, test)
	format
	lint
	test

generate-requirements: ## Generate requirements.txt from pyproject.toml
	python scripts/generate_requirements.py 