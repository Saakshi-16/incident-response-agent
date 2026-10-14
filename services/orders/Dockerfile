# 1. Start from an official, small Python 3.12 image
FROM python:3.12-slim

# 2. Copy the uv tool into the image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 3. All following commands run inside /app
WORKDIR /app

# 4. Install dependencies first (this layer is cached)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# 5. Copy the application code
COPY main.py ./

# 6. Make the installed packages available as commands
ENV PATH="/app/.venv/bin:$PATH"

# 7. Document the port the app listens on
EXPOSE 8000

# 8. The command that runs when the container starts
CMD ["fastapi", "run", "main.py", "--port", "8000"]