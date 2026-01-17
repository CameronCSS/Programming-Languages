# 💰 ExpenseTrack

A Flask expense tracking app with PostgreSQL and Docker.

![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

---

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd expensetrack
```

### 2. Create `.env` File
```env
FLASK_APP=app.py
FLASK_ENV=development

DB_NAME=expensetrack
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

JWT_SECRET_KEY=supersecretkey
```

### 3. Build & Start
```bash
docker compose build
docker compose up -d
```

### 4. Database Setup
```bash
docker compose exec web flask db init
docker compose exec web flask db migrate -m "Initial migration"
docker compose exec web flask db upgrade
```

### 5. Access App
🌐 **http://localhost:5000/**

---

## 🛠️ Useful Commands

**View logs:**
```bash
docker compose logs -f web
```

**Stop containers:**
```bash
docker compose down
```

**New migration:**
```bash
docker compose exec web flask db migrate -m "Description"
docker compose exec web flask db upgrade
```

---

## 📡 API Examples

**Register:**
```bash
POST /api/auth/register
{"username": "user@example.com", "password": "pass123"}
```

**Login:**
```bash
POST /api/auth/login
{"username": "user@example.com", "password": "pass123"}
```

**Get expenses:**
```bash
GET /api/expenses
Authorization: Bearer <token>
```

---

## 📄 License

MIT License