# Auth Service

Node.js + Express authentication service with Prisma/PostgreSQL.

Exposes versioned REST APIs under:

- `POST /api/v1/auth/*`
- `GET/PUT/DELETE /api/v1/users/*`

## Project setup

### Prerequisites

- Node.js (recommended Node 18+)
- Docker Desktop (optional, if you want PostgreSQL via docker-compose)
- PostgreSQL (if not using Docker)

### 1) Install dependencies

```bash
npm install
```

### 2) Configure environment variables

Create a `.env` file in the repo root (you can copy `.env.example` as a starting point).

> Notes:
>
> - JWT secret values are required by `src/config/jwt.config.js` (startup will throw if missing).
> - `DATABASE_URL` is required by Prisma (`prisma/schema.prisma`).
> - Never commit your real `.env` file — only commit `.env.example`.

Example `.env.example`:

```env
# =========================================
# Auth Service - Environment Variables
# Copy this file to `.env` and fill in real values.
# Never commit your actual `.env` file.
# =========================================

# ---- Server ----
NODE_ENV=development
PORT=5000

# Base path prefix used for all routes (e.g. /api/v1/auth/...)
API_PREFIX=/api/v1

# ---- Prisma / PostgreSQL ----
# Format: postgresql://<user>:<password>@<host>:<port>/<database>?schema=public
DATABASE_URL="postgresql://postgres:postgres@localhost:5432/auth_service?schema=public"

# ---- JWT ----
# Required by src/config/jwt.config.js - app will throw on startup if missing.
# Use long, random, unique secrets in production.
# Generate one with: openssl rand -hex 64
JWT_ACCESS_SECRET="replace_with_a_long_random_access_secret"
JWT_REFRESH_SECRET="replace_with_a_long_random_refresh_secret"

# Token TTL (e.g. 15m, 1h, 7d)
JWT_ACCESS_EXPIRES=15m
JWT_REFRESH_EXPIRES=7d

# ---- Redis ----
# Used for caching / rate limiting / OTP storage (if applicable)
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=

# ---- Mail (SMTP) ----
# Used for sending verification / OTP / password-reset emails.
# Example below uses Mailtrap sandbox for local testing - replace with your own credentials.
MAIL_HOST=sandbox.smtp.mailtrap.io
MAIL_PORT=2525
MAIL_USER=your_mail_user
MAIL_PASSWORD=your_mail_password
MAIL_FROM=no-reply@authservice.local
```

### 3) Start PostgreSQL

#### Option A (recommended): using Docker

```bash
docker compose up -d
```

`docker-compose.yml` starts Postgres with:

- db: `auth_service`
- user: `postgres`
- password: `postgres`
- port: `5432`

#### Option B: local Postgres

Make sure Postgres is running and update `DATABASE_URL` accordingly.

### 4) Apply Prisma migrations

This repo already contains Prisma migrations under `prisma/migrations/`.

Run:

```bash
npx prisma migrate deploy
```

> If you’re setting up from scratch and the database is empty, this applies the full migration history.

### 5) Generate Prisma client

```bash
npx prisma generate
```

### 6) Run the API

Development:

```bash
npm run dev
```

Production:

```bash
npm start
```

API base URL:

- `http://localhost:5000/api/v1`

### Swagger API docs

Once the server is running, you can explore and test all endpoints directly from the browser via Swagger UI:

- [http://localhost:5000/api-docs](http://localhost:5000/api-docs/#/)

This is the quickest way to try out requests (signup, login, profile, etc.) without curl/Postman.

## Request validation (schemas)

Incoming request bodies are validated using Zod validators:

- `src/validators/signup.validator.js`
  - `fullName`: 3-100 chars
  - `email`: valid email format
  - `phoneNumber`: exactly 10 digits (`/^[0-9]{10}$/`)
  - `password`: min 8, includes uppercase, lowercase, number, and special character
- `src/validators/login.validator.js`
  - `email`: valid email
  - `password`: non-empty

## API: endpoints and test flow

### 1) Sign up

**POST** `/api/v1/auth/signup`

Request body:

```json
{
  "fullName": "John Doe",
  "email": "john@example.com",
  "phoneNumber": "1234567890",
  "password": "StrongPass!1"
}
```

Response (example):

```json
{
  "success": true,
  "message": "User registered",
  "data": {
    "userId": "1",
    "email": "john@example.com",
    "verificationToken": "<raw-token>")
  }
}
```

Important:

- The response includes `verificationToken` (raw token).
- The email verification endpoint expects this raw token.

### 2) Verify email

**GET** `/api/v1/auth/verify-email?token=<verificationToken>`

Example:

```http
GET /api/v1/auth/verify-email?token=REPLACE_WITH_verificationToken
```

On success:

- returns `Email verified successfully`.

### 3) Log in

**POST** `/api/v1/auth/login`

Request body:

```json
{
  "email": "john@example.com",
  "password": "StrongPass!1"
}
```

Response (example):

```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "accessToken": "<jwt-access-token>",
    "user": {
      "id": "1",
      "email": "john@example.com",
      "fullName": "John Doe"
    }
  }
}
```

Also, the server sets a refresh token cookie:

- cookie name: `refreshToken`

### 4) Get profile (authenticated)

**GET** `/api/v1/users/profile`

Headers:

- `Authorization: Bearer <jwt-access-token>`

### 5) Update profile (authenticated)

**PUT** `/api/v1/users/profile`

Headers:

- `Authorization: Bearer <jwt-access-token>`

Request body:

- The service/controller accepts an update payload (validate rules are implemented in the repository/service layer).

### 6) Delete account (authenticated)

**DELETE** `/api/v1/users/account`

Headers:

- `Authorization: Bearer <jwt-access-token>`

### 7) Refresh token

**POST** `/api/v1/auth/refresh-token`

The server reads refresh token from:

- cookie `refreshToken`, or
- request body `refreshToken`

### 8) Logout

**POST** `/api/v1/auth/logout`

The server reads refresh token from:

- cookie `refreshToken`, or
- request body `refreshToken`

## Curl-based end-to-end test with schema

> This script demonstrates the expected request shape.
> Replace tokens and emails as needed.

### Sign up

```bash
curl -s http://localhost:5000/api/v1/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "fullName":"John Doe",
    "email":"john@example.com",
    "phoneNumber":"1234567890",
    "password":"StrongPass!1"
  }' | jq
```

Copy `data.verificationToken` from the output.

### Verify email

```bash
curl -s "http://localhost:5000/api/v1/auth/verify-email?token=PASTE_VERIFICATION_TOKEN" | jq
```

### Log in

```bash
curl -s http://localhost:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"john@example.com","password":"StrongPass!1"}' -c cookies.txt | jq
```

Copy `data.accessToken` from the output.

### Get profile

```bash
curl -s http://localhost:5000/api/v1/users/profile \
  -H "Authorization: Bearer PASTE_ACCESS_TOKEN" -b cookies.txt | jq
```

## Database / Prisma schema overview

Prisma schema is located at:

- `prisma/schema.prisma`

Key models:

- `User`
- `EmailVerificationToken` (hashed token stored; raw token is returned on signup)
- `RefreshToken` (hashed token stored; raw token is stored in cookie)
- `PasswordResetToken`
- `OtpLog`
- `LoginHistory`
- `AuditLog`

Database connection uses `DATABASE_URL`.

## Run tests

There are Jest tests under `src/tests/`.

To run:

```bash
npm test
```

(If `npm test` is not configured in your environment, you can run Jest directly.)
