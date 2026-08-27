# Vue + Express + MongoDB

Standalone three-tier deployment fixture.

- Priority tier: **mainstream**
- Frontend: **Vue**
- Backend: **Express**
- Database: **MongoDB**
- Backend port: `4000`
- Backend health endpoint: `GET /healthz`
- Public API prefix: `/api/v2`
- Frontend calls: `GET /api/v2/message`
- Database ENV profile: `MONGODB`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
npm start
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
