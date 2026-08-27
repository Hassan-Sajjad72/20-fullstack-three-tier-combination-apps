# 20 Minimal Three-Tier Full-Stack Combination Applications

This ZIP contains **20 independent application folders** designed for repository-by-repository deployment testing.

The matrix intentionally prioritizes mainstream combinations first:

- React + FastAPI / Django / Flask / Express / NestJS / Fastify
- Vue + FastAPI / Django / Flask / Express / Fastify
- PostgreSQL, MySQL, MongoDB

The final six broaden coverage with:

- Svelte
- Next.js static export
- additional Python and JavaScript backend combinations

Each application is a true three-tier fixture:

```text
frontend
   ↓
backend API
   ↓
database
```

Every application contains:

- `frontend/`
- `backend/`
- `.env.example`
- `DEPLOY_ENV.txt`
- `README.md`
- `.gitignore`

`DEPLOY_ENV.txt` contains synthetic test values that can be copied directly for testing. Do not use these values for production systems.

## Application matrix

| # | Folder | Tier | Frontend | Backend | Database | API Prefix | Health |
|---:|---|---|---|---|---|---|---|
| 1 | `01-react-fastapi-postgres` | mainstream | React | FastAPI | PostgreSQL | `/api/v1` | `/health` |
| 2 | `02-react-django-postgres` | mainstream | React | Django | PostgreSQL | `/api` | `/health` |
| 3 | `03-react-flask-postgres` | mainstream | React | Flask | PostgreSQL | `/v1` | `/healthz` |
| 4 | `04-react-express-mongodb` | mainstream | React | Express | MongoDB | `/api/v1` | `/ready` |
| 5 | `05-react-express-postgres` | mainstream | React | Express | PostgreSQL | `/api/v2` | `/health` |
| 6 | `06-react-fastapi-mongodb` | mainstream | React | FastAPI | MongoDB | `/backend` | `/health` |
| 7 | `07-vue-fastapi-postgres` | mainstream | Vue | FastAPI | PostgreSQL | `/api` | `/ready` |
| 8 | `08-vue-django-mysql` | mainstream | Vue | Django | MySQL | `/v1` | `/health` |
| 9 | `09-vue-express-mongodb` | mainstream | Vue | Express | MongoDB | `/api/v2` | `/healthz` |
| 10 | `10-vue-flask-postgres` | mainstream | Vue | Flask | PostgreSQL | `/service` | `/health` |
| 11 | `11-react-nestjs-mongodb` | mainstream | React | NestJS | MongoDB | `/backend` | `/health` |
| 12 | `12-react-fastify-mysql` | mainstream | React | Fastify | MySQL | `/api/v1` | `/ready` |
| 13 | `13-vue-fastify-postgres` | mainstream | Vue | Fastify | PostgreSQL | `/service` | `/health` |
| 14 | `14-vue-express-mysql` | mainstream | Vue | Express | MySQL | `/api` | `/healthz` |
| 15 | `15-svelte-fastapi-mongodb` | extended | Svelte | FastAPI | MongoDB | `/api` | `/healthz` |
| 16 | `16-svelte-express-postgres` | extended | Svelte | Express | PostgreSQL | `/v1` | `/health` |
| 17 | `17-svelte-flask-mysql` | extended | Svelte | Flask | MySQL | `/api/v2` | `/ready` |
| 18 | `18-nextjs-fastapi-postgres` | extended | Next.js static | FastAPI | PostgreSQL | `/api/v1` | `/health` |
| 19 | `19-nextjs-express-mongodb` | extended | Next.js static | Express | MongoDB | `/backend` | `/ready` |
| 20 | `20-svelte-fastify-mysql` | extended | Svelte | Fastify | MySQL | `/service` | `/health` |

## Why ENV naming varies

The applications deliberately exercise real-world configuration styles:

- `POSTGRES_*`
- native PostgreSQL `PG*`
- generic `DB_*`
- `DATABASE_URL`
- `MYSQL_*`
- `MONGO_URI`
- `MONGODB_URI` + `MONGODB_DATABASE`

The public frontend URL also varies between:

- `VITE_API_BASE_URL`
- `NEXT_PUBLIC_API_BASE_URL`

## Important routing characteristic

The public API prefix is not necessarily a callable health endpoint.

Example:

```text
API prefix: /api/v1
health: /health
actual frontend request: /api/v1/message
```

This is intentional.

## GitHub usage

Each numbered folder is intended to become its **own GitHub repository** for clean repository + branch testing.

See `PUSH_ONE_BY_ONE.md`.
