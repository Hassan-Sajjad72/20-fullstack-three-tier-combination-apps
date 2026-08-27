# Vue + Express + MySQL

Standalone three-tier deployment fixture.

- Priority tier: **mainstream**
- Frontend: **Vue**
- Backend: **Express**
- Database: **MySQL**
- Backend port: `4000`
- Backend health endpoint: `GET /healthz`
- Public API prefix: `/api`
- Frontend calls: `GET /api/message`
- Database ENV profile: `URL`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
npm start
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
