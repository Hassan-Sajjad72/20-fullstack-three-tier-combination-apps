# Svelte + FastAPI + MongoDB

Standalone three-tier deployment fixture.

- Priority tier: **extended**
- Frontend: **Svelte**
- Backend: **FastAPI**
- Database: **MongoDB**
- Backend port: `8000`
- Backend health endpoint: `GET /healthz`
- Public API prefix: `/api`
- Frontend calls: `GET /api/message`
- Database ENV profile: `MONGO`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
