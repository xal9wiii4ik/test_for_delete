FROM python:3.9-alpine as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add curl

COPY . .
RUN curl https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py > get-poetry
RUN python get-poetry.py
ENV PATH = "${PATH}:/root/.poetry/bin"
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

RUN chmod +x /usr/src/app/entrypoint.sh
ENTRYPOINT /usr/src/app/entrypoint.sh
