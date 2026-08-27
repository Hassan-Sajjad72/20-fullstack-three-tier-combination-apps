# React + Express + MongoDB

Standalone three-tier deployment fixture.

- Priority tier: **mainstream**
- Frontend: **React**
- Backend: **Express**
- Database: **MongoDB**
- Backend port: `4000`
- Backend health endpoint: `GET /ready`
- Public API prefix: `/api/v1`
- Frontend calls: `GET /api/v1/message`
- Database ENV profile: `MONGO`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
npm start
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
