FROM amazon/aws-lambda-python:3.11

RUN pip install --upgrade pip
RUN pip install poetry

ENV POETRY_VIRTUALENVS_IN_PROJECT=true