clean:
	@echo "Cleaning project..."
	@rm -rf __pycache__ app/__pycache__ tests/__pycache__ .pytest_cache
	@echo "Project cleaned successfully."