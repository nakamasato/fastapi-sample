FROM python:3.14-slim
COPY --from=ghcr.io/astral-sh/uv:0.12.19 /uv /bin/uv
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*
WORKDIR /app
# docker-compose bind-mounts ./app over /app, so install into the system interpreter instead of /app/.venv
ENV UV_PROJECT_ENVIRONMENT=/usr/local
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-cache
COPY ./ /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
