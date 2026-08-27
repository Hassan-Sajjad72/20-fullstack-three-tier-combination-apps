# Vue + FastAPI + PostgreSQL

Standalone three-tier deployment fixture.

- Priority tier: **mainstream**
- Frontend: **Vue**
- Backend: **FastAPI**
- Database: **PostgreSQL**
- Backend port: `8000`
- Backend health endpoint: `GET /ready`
- Public API prefix: `/api`
- Frontend calls: `GET /api/message`
- Database ENV profile: `DB`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
