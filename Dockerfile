FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \ PYTHONBUFFERED=1 \ POETRY_VERSION=2.2.1

RUN pip install --no-cache-dir "poetry==2.2.1"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY /src src/

EXPOSE 5000

CMD ["poetry", "run", "start"]