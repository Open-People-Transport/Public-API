# Configure the environment
FROM python:3.10
WORKDIR /app
EXPOSE 80
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VERSION=1.2.0
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_VIRTUALENVS_IN_PROJECT=false
ENV UVICORN_HOST=0.0.0.0
ENV UVICORN_PORT=80

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$PATH:$POETRY_HOME/bin"

# Copy root package metadata for later installation
COPY /README.md ./

# Install runtime dependencies
COPY /poetry.lock /pyproject.toml ./
RUN poetry install --only main --no-root --no-cache --no-interaction

# Copy source code into the container
COPY /opt_public_server/ ./opt_public_server/
RUN poetry install --only-root --no-cache

# Provide the container execution command
CMD ["uvicorn", "opt_public_server.main.app:app"]
