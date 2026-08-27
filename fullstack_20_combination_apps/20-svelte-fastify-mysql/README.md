# Svelte + Fastify + MySQL

Standalone three-tier deployment fixture.

- Priority tier: **extended**
- Frontend: **Svelte**
- Backend: **Fastify**
- Database: **MySQL**
- Backend port: `3000`
- Backend health endpoint: `GET /health`
- Public API prefix: `/service`
- Frontend calls: `GET /service/message`
- Database ENV profile: `MYSQL`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
npm start
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
