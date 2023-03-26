FROM python:3-alpine

RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml /app/


RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /app

CMD python3 main.py