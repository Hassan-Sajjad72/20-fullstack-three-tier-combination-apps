# Svelte + Flask + MySQL

Standalone three-tier deployment fixture.

- Priority tier: **extended**
- Frontend: **Svelte**
- Backend: **Flask**
- Database: **MySQL**
- Backend port: `5000`
- Backend health endpoint: `GET /ready`
- Public API prefix: `/api/v2`
- Frontend calls: `GET /api/v2/message`
- Database ENV profile: `MYSQL`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
