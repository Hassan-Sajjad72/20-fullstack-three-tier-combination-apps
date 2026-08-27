# Vue + Flask + PostgreSQL

Standalone three-tier deployment fixture.

- Priority tier: **mainstream**
- Frontend: **Vue**
- Backend: **Flask**
- Database: **PostgreSQL**
- Backend port: `5000`
- Backend health endpoint: `GET /health`
- Public API prefix: `/service`
- Frontend calls: `GET /service/message`
- Database ENV profile: `POSTGRES`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
