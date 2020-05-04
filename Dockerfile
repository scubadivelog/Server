FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv && pipenv install --system

COPY . /code
