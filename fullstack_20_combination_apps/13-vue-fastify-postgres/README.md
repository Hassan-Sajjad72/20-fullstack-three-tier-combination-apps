# Vue + Fastify + PostgreSQL

Standalone three-tier deployment fixture.

- Priority tier: **mainstream**
- Frontend: **Vue**
- Backend: **Fastify**
- Database: **PostgreSQL**
- Backend port: `3000`
- Backend health endpoint: `GET /health`
- Public API prefix: `/service`
- Frontend calls: `GET /service/message`
- Database ENV profile: `PG`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
npm start
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
