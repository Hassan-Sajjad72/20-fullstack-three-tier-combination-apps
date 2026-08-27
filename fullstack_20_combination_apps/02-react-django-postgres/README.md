# React + Django + PostgreSQL

Standalone three-tier deployment fixture.

- Priority tier: **mainstream**
- Frontend: **React**
- Backend: **Django**
- Database: **PostgreSQL**
- Backend port: `8000`
- Backend health endpoint: `GET /health`
- Public API prefix: `/api`
- Frontend calls: `GET /api/message`
- Database ENV profile: `DB`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
