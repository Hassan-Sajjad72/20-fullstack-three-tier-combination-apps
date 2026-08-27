# Next.js static + FastAPI + PostgreSQL

Standalone three-tier deployment fixture.

- Priority tier: **extended**
- Frontend: **Next.js static**
- Backend: **FastAPI**
- Database: **PostgreSQL**
- Backend port: `8000`
- Backend health endpoint: `GET /health`
- Public API prefix: `/api/v1`
- Frontend calls: `GET /api/v1/message`
- Database ENV profile: `URL`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
