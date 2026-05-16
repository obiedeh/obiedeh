# Local Deployment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
uvicorn api.main:app --reload --port 8080
```

In another terminal:

```bash
python -m edge.worker --source examples/sample_source.json --backend http://127.0.0.1:8080
```

Docker:

```bash
docker compose up --build
```

