# React + FastAPI + PostgreSQL

Standalone three-tier deployment fixture.

- Priority tier: **mainstream**
- Frontend: **React**
- Backend: **FastAPI**
- Database: **PostgreSQL**
- Backend port: `8000`
- Backend health endpoint: `GET /health`
- Public API prefix: `/api/v1`
- Frontend calls: `GET /api/v1/message`
- Database ENV profile: `POSTGRES`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
