# Push Applications One by One

Each numbered folder should be pushed as its own GitHub repository.

Example:

```bash
cd 01-react-fastapi-postgres

git init
git add .
git commit -m "feat: add React FastAPI PostgreSQL test app"
git branch -M main
git remote add origin <GITHUB_REPOSITORY_URL>
git push -u origin main
```

Repeat for the next application using a new repository.

Before deployment, copy the exact values from `DEPLOY_ENV.txt`.

Do not commit production `.env` files or real credentials.
