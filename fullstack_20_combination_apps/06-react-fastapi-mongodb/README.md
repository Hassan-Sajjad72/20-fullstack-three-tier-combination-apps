# React + FastAPI + MongoDB

Standalone three-tier deployment fixture.

- Priority tier: **mainstream**
- Frontend: **React**
- Backend: **FastAPI**
- Database: **MongoDB**
- Backend port: `8000`
- Backend health endpoint: `GET /health`
- Public API prefix: `/backend`
- Frontend calls: `GET /backend/message`
- Database ENV profile: `MONGODB`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
