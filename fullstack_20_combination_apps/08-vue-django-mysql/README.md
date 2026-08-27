# Vue + Django + MySQL

Standalone three-tier deployment fixture.

- Priority tier: **mainstream**
- Frontend: **Vue**
- Backend: **Django**
- Database: **MySQL**
- Backend port: `8000`
- Backend health endpoint: `GET /health`
- Public API prefix: `/v1`
- Frontend calls: `GET /v1/message`
- Database ENV profile: `MYSQL`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
