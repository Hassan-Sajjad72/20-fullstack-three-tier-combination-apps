# React + NestJS + MongoDB

Standalone three-tier deployment fixture.

- Priority tier: **mainstream**
- Frontend: **React**
- Backend: **NestJS**
- Database: **MongoDB**
- Backend port: `3000`
- Backend health endpoint: `GET /health`
- Public API prefix: `/backend`
- Frontend calls: `GET /backend/message`
- Database ENV profile: `MONGO`

The API prefix is intentionally separate from the health endpoint.

Backend start command:

```bash
npm run build && npm start
```

Use **`DEPLOY_ENV.txt`** as the complete safe test ENV.
