# React + Express + PostgreSQL

Standalone three-tier deployment fixture.

- Priority tier: **mainstream**
- Frontend: **React**
- Backend: **Express**
- Database: **PostgreSQL**
- Backend port: `4000`
- Backend health endpoint: `GET /health`
- Public API prefix: `/api/v2`
- Frontend calls: `GET /api/v2/message`
- Database ENV profile: `URL`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
npm start
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
