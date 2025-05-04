# 📢 Anonymous Feedback System

FastAPI backend для корпоративної системи анонімного зворотного зв'язку з можливістю фільтрації, аналітики та адмін-панеллю.

---

## 🚀 Стек технологій

* **Backend:** FastAPI + PostgreSQL + SQLAlchemy
* **Auth:** JWT
* **Async:** `asyncpg`, `asyncio`
* **DevOps:** Docker, Docker Compose

---

## 📁 Структура проекту

```
app/
├── api/           # Роутери (feedback, auth)
├── core/          # Налаштування (config, security)
├── crud/          # Робота з БД
├── db/            # Сесія, моделі
├── schemas/       # Pydantic-схеми
├── services/      # Додаткові сервіси (опційно)
└── main.py        # Точка входу
```

---

## ⚙️ Налаштування `.env`

```
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/feedback_db
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=60
ALGORITHM=HS256
```

---

## 🐳 Docker запуск

```
docker-compose up --build
```

---

## ✅ Старт без Docker

```bash
uvicorn app.main:app --reload
```
