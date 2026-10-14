# Orders Service

Lets customers view and place orders. Part of the demo shop monitored by the incident agent.

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/orders` | List all orders |
| GET | `/orders/{order_id}` | Get one order (404 if not found) |
| POST | `/orders` | Create an order (201) |

## Run locally

```bash
uv run fastapi dev main.py
```

## Run with Docker

```bash
docker build -t orders:dev .
docker run --rm -p 8000:8000 orders:dev
```

Docs: http://localhost:8000/docs