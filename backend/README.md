# MCDA Studio — Backend

FastAPI backend for MCDA Studio.

## Requirements
- Python 3.13+
- uv

## Setup

1. Copy `.env.example` to `.env` and adjust values if needed:
```
cp .env.example .env
```

2. Install dependencies:
```
uv sync
```

## Run
```
uv run uvicorn app.main:app --reload
```

## Test
```
uv run pytest
```

## API Documentation
http://localhost:8000/docs
