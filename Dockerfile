FROM python:3-alpine

# https://stackoverflow.com/questions/71372066/docker-fails-to-install-cffi-with-python3-9-alpine-in-dockerfile&cd=1&hl=en&ct=clnk&gl=ch
RUN apk add libffi-dev

RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml /app/


RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /app

CMD python3 main.py