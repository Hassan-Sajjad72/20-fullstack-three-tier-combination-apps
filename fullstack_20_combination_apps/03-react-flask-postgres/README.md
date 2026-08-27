# React + Flask + PostgreSQL

Standalone three-tier deployment fixture.

- Priority tier: **mainstream**
- Frontend: **React**
- Backend: **Flask**
- Database: **PostgreSQL**
- Backend port: `5000`
- Backend health endpoint: `GET /healthz`
- Public API prefix: `/v1`
- Frontend calls: `GET /v1/message`
- Database ENV profile: `PG`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
