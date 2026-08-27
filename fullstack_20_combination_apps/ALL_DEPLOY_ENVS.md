# All Deployment ENVs

These are the exact synthetic test ENV values included with each application.


## 01-react-fastapi-postgres

```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=combo_app
POSTGRES_USER=combo_user
POSTGRES_PASSWORD=combo_password
HOST=0.0.0.0
PORT=8000
```


## 02-react-django-postgres

```env
VITE_API_BASE_URL=http://localhost:8000/api
DB_HOST=localhost
DB_PORT=5432
DB_NAME=combo_app
DB_USER=combo_user
DB_PASSWORD=combo_password
HOST=0.0.0.0
PORT=8000
DJANGO_SECRET_KEY=deploy-test-django-key-not-production
DJANGO_DEBUG=False
```


## 03-react-flask-postgres

```env
VITE_API_BASE_URL=http://localhost:5000/v1
PGHOST=localhost
PGPORT=5432
PGDATABASE=combo_app
PGUSER=combo_user
PGPASSWORD=combo_password
HOST=0.0.0.0
PORT=5000
```


## 04-react-express-mongodb

```env
VITE_API_BASE_URL=http://localhost:4000/api/v1
MONGO_URI=mongodb://localhost:27017/combo_app
HOST=0.0.0.0
PORT=4000
```


## 05-react-express-postgres

```env
VITE_API_BASE_URL=http://localhost:4000/api/v2
DATABASE_URL=postgresql://combo_user:combo_password@localhost:5432/combo_app
HOST=0.0.0.0
PORT=4000
```


## 06-react-fastapi-mongodb

```env
VITE_API_BASE_URL=http://localhost:8000/backend
MONGODB_URI=mongodb://localhost:27017
MONGODB_DATABASE=combo_app
HOST=0.0.0.0
PORT=8000
```


## 07-vue-fastapi-postgres

```env
VITE_API_BASE_URL=http://localhost:8000/api
DB_HOST=localhost
DB_PORT=5432
DB_NAME=combo_app
DB_USER=combo_user
DB_PASSWORD=combo_password
HOST=0.0.0.0
PORT=8000
```


## 08-vue-django-mysql

```env
VITE_API_BASE_URL=http://localhost:8000/v1
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=combo_app
MYSQL_USER=combo_user
MYSQL_PASSWORD=combo_password
HOST=0.0.0.0
PORT=8000
DJANGO_SECRET_KEY=deploy-test-django-key-not-production
DJANGO_DEBUG=False
```


## 09-vue-express-mongodb

```env
VITE_API_BASE_URL=http://localhost:4000/api/v2
MONGODB_URI=mongodb://localhost:27017
MONGODB_DATABASE=combo_app
HOST=0.0.0.0
PORT=4000
```


## 10-vue-flask-postgres

```env
VITE_API_BASE_URL=http://localhost:5000/service
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=combo_app
POSTGRES_USER=combo_user
POSTGRES_PASSWORD=combo_password
HOST=0.0.0.0
PORT=5000
```


## 11-react-nestjs-mongodb

```env
VITE_API_BASE_URL=http://localhost:3000/backend
MONGO_URI=mongodb://localhost:27017/combo_app
HOST=0.0.0.0
PORT=3000
```


## 12-react-fastify-mysql

```env
VITE_API_BASE_URL=http://localhost:3000/api/v1
DB_HOST=localhost
DB_PORT=3306
DB_NAME=combo_app
DB_USER=combo_user
DB_PASSWORD=combo_password
HOST=0.0.0.0
PORT=3000
```


## 13-vue-fastify-postgres

```env
VITE_API_BASE_URL=http://localhost:3000/service
PGHOST=localhost
PGPORT=5432
PGDATABASE=combo_app
PGUSER=combo_user
PGPASSWORD=combo_password
HOST=0.0.0.0
PORT=3000
```


## 14-vue-express-mysql

```env
VITE_API_BASE_URL=http://localhost:4000/api
DATABASE_URL=mysql://combo_user:combo_password@localhost:3306/combo_app
HOST=0.0.0.0
PORT=4000
```


## 15-svelte-fastapi-mongodb

```env
VITE_API_BASE_URL=http://localhost:8000/api
MONGO_URI=mongodb://localhost:27017/combo_app
HOST=0.0.0.0
PORT=8000
```


## 16-svelte-express-postgres

```env
VITE_API_BASE_URL=http://localhost:4000/v1
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=combo_app
POSTGRES_USER=combo_user
POSTGRES_PASSWORD=combo_password
HOST=0.0.0.0
PORT=4000
```


## 17-svelte-flask-mysql

```env
VITE_API_BASE_URL=http://localhost:5000/api/v2
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=combo_app
MYSQL_USER=combo_user
MYSQL_PASSWORD=combo_password
HOST=0.0.0.0
PORT=5000
```


## 18-nextjs-fastapi-postgres

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api/v1
DATABASE_URL=postgresql://combo_user:combo_password@localhost:5432/combo_app
HOST=0.0.0.0
PORT=8000
```


## 19-nextjs-express-mongodb

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:4000/backend
MONGO_URI=mongodb://localhost:27017/combo_app
HOST=0.0.0.0
PORT=4000
```


## 20-svelte-fastify-mysql

```env
VITE_API_BASE_URL=http://localhost:3000/service
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=combo_app
MYSQL_USER=combo_user
MYSQL_PASSWORD=combo_password
HOST=0.0.0.0
PORT=3000
```
