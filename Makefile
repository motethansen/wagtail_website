# Makefile for Django project
.PHONY: help migrate createsuperuser deletesuperuser run

# Default target when running `make` with no arguments
help:
	@echo "Available commands:"
	@echo "  make migrate          - Run Django migrations"
	@echo "  make createsuperuser  - Create superuser from .env file if it doesn’t exist"
	@echo "  make deletesuperuser  - Delete superuser specified in .env file"
	@echo "  make run              - Run the Django development server"

# Apply migrations
migrate:
	python manage.py migrate

# Create superuser using the custom command
createsuperuser:
	python manage.py createsuperuserauto

# Delete superuser using the custom command
deletesuperuser:
	python manage.py deletesuperuser

# Run the development server
run:
	python manage.py collectstatic --noinput
	python manage.py runserver

build:
	pip install -r requirements.txt
	python manage.py makemigrations
	python manage.py migrate
	python manage.py collectstatic --noinput
