# Air Quality Monitoring System

> An end-to-end IoT platform that reads indoor air-quality sensors on an Arduino, serves the data through a **FastAPI** backend (REST API, JWT auth, threshold-based email alerts, ML prediction), and presents it on **web** and **mobile (Flutter)** clients.

![Backend](https://img.shields.io/badge/Backend-FastAPI-009688)
![Auth](https://img.shields.io/badge/Auth-JWT%2FOAuth2-000000)
![ML](https://img.shields.io/badge/ML-scikit--learn-F7931E)
![Web](https://img.shields.io/badge/Web-TypeScript-3178C6)
![Mobile](https://img.shields.io/badge/Mobile-Flutter-02569B)

University team project (6 members). **My role: I built the FastAPI backend end-to-end.**

---

## 🏗️ Architecture
```
+------------+        +-------------------+        +--------------+
|  Arduino   | -----> |   FastAPI backend | -----> |  Web (TS)    |
|  sensors   |  REST  |  REST API + auth  |  REST  |  Mobile      |
|  CO2/PM/.. |        |  alerts + ML      |        |  (Flutter)   |
+------------+        +-------------------+        +--------------+
```
- `arduino/` — reads CO2 / PM2.5 / PM10 / VOC sensors and posts readings to the API.
- `backend/` — FastAPI service (this is the part I built).
- `frontend/` — TypeScript web client (dashboard, analytics, settings).
- `mobile/` — Flutter mobile client.

## ⚙️ Backend (FastAPI)
A REST API with **14+ endpoints**, JWT/OAuth2 authentication, SQLAlchemy ORM, threshold-based email alerting, and a RandomForest prediction endpoint.

| Area | Endpoints |
|------|-----------|
| **Auth** | `POST /auth/register` · `POST /auth/login` · `GET /auth/me` |
| **Sensors** | `POST /api/sensors/data` · `GET /api/sensors/history` · `GET /api/sensors/summary` · `GET /api/sensors/current` · `GET /api/stats` |
| **Settings** | `GET /api/settings` · `POST /api/settings` (per-user thresholds & notifications) |
| **Alerts** | `GET /api/alerts/unacknowledged` · `POST /api/alerts/acknowledge` · `POST /api/alerts/acknowledgeall` |
| **ML** | `GET /api/ai/latest` · `POST /ml/process` (RandomForest via `joblib`) |

Key features:
- **JWT/OAuth2 auth** with hashed passwords (passlib, python-jose).
- **Sensor ingestion & querying** — store readings, then serve history / summary / current / stats.
- **Threshold-based email alerts** — per-user thresholds, background email sending (fastapi-mail + Jinja2 templates), with a **5-minute debounce** to avoid duplicate alerts.
- **Alert acknowledgement** workflow.
- **ML prediction** — a pre-trained RandomForest model classifies air quality; predictions are stored and exposed via the API.

## 🧱 Tech Stack
FastAPI · SQLAlchemy · python-jose (JWT) · passlib · fastapi-mail · Jinja2 · scikit-learn (RandomForest) · joblib

## 🚀 Run the backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r ../requirements.txt

cp .env.example .env             # fill in the values below
uvicorn main:app --reload        # http://localhost:8000  (Swagger: /docs)
```

`.env` (required):
| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | SQLAlchemy connection string |
| `SECRET_KEY` | JWT signing key (long, random) |
| `MAIL_USERNAME` / `MAIL_PASSWORD` | SMTP credentials |
| `MAIL_FROM` / `MAIL_SERVER` / `MAIL_PORT` | SMTP sender & server |

## 📸 Screenshots
<!-- Add a couple of dashboard / mobile screenshots here. -->

## 👥 Team & My Contribution
6-person university project. I designed and implemented the **entire FastAPI backend** (~10 modules): REST API, auth, data model, alerting, and ML integration. Web and mobile clients were built by teammates against this API.
