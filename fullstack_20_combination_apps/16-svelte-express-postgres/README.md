# Svelte + Express + PostgreSQL

Standalone three-tier deployment fixture.

- Priority tier: **extended**
- Frontend: **Svelte**
- Backend: **Express**
- Database: **PostgreSQL**
- Backend port: `4000`
- Backend health endpoint: `GET /health`
- Public API prefix: `/v1`
- Frontend calls: `GET /v1/message`
- Database ENV profile: `POSTGRES`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
npm start
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
