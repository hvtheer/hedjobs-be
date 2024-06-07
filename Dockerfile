# Use an official Python runtime as a parent image
FROM python:3.11

# Install dependencies
RUN curl -sSL https://install.python-poetry.org | python -

# Set work directory
WORKDIR /usr/srv

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Add a user for security purposes (optional but recommended)
RUN useradd -rm -d /code -s /bin/bash -g root -G sudo -u 1001 ubuntu

# Copy the poetry.lock and pyproject.toml file
COPY ./pyproject.toml /usr/srv/pyproject.toml
# COPY ./poetry.lock /usr/srv/poetry.lock

RUN pip install --upgrade pip
RUN pip install poetry

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-dev

# Switch to a non-root user (optional but recommended)
USER ubuntu

# Expose port 8000
EXPOSE 8000

# Define the command to run your application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
