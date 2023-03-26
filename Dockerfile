FROM python:3-alpine

# because in the case of arm64 we need to build from source some packages
RUN apk add libffi-dev gcc musl-dev

RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml /app/


RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /app

CMD python3 main.py