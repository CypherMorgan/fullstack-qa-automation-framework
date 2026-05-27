# 🚀 Fullstack QA Automation Framework (Python + Selenium + API + DB + CI/CD)

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green?logo=selenium)
![PyTest](https://img.shields.io/badge/PyTest-Framework-orange?logo=pytest)
![Allure](https://img.shields.io/badge/Allure-Reports-purple)
![FastAPI](https://img.shields.io/badge/FastAPI-Mock%20Server-teal?logo=fastapi)
![Postman](https://img.shields.io/badge/Postman-API%20Testing-orange?logo=postman)
![Newman](https://img.shields.io/badge/Newman-CLI-blue)
![SQLite](https://img.shields.io/badge/SQLite-DB-lightgrey?logo=sqlite)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI/CD-blue?logo=githubactions)
![Status](https://img.shields.io/badge/status-active-success)
![Tests](https://img.shields.io/badge/tests-automated-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-UI%20%7C%20API%20%7C%20DB-blue)
![Parallel](https://img.shields.io/badge/execution-parallel-informational)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A **production-style hybrid test automation framework** built using **Python, Selenium, PyTest, API testing, database validation, and CI/CD pipelines**.

This framework demonstrates how modern QA systems validate applications across **multiple layers**:

* UI (Frontend)
* API (Backend services)
* Database (Data integrity)

---

## 🔗 Live Reports
- Allure Report: https://cyphermorgan.github.io/fullstack-qa-automation-framework/

# 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.11 |
| UI Automation | Selenium WebDriver |
| Test Runner | PyTest |
| API Testing | Requests, Postman, Newman |
| Mock Services | FastAPI |
| Database | SQLite |
| Reporting | Allure, pytest-html |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Parallel Execution | pytest-xdist |

# 🔥 Key Features

### 🖥️ UI Automation

* Selenium WebDriver
* Page Object Model (POM)
* Multi-browser support
* Screenshot capture on failure

### 🌐 API Testing

* Python-based API client
* Postman collection support
* Newman CLI execution
* API validation with structured logging

### 🗄️ Database Validation

* SQLite DB integration
* API vs DB validation tests
* Data integrity checks

### 🧪 Test Framework

* PyTest test runner
* Parametrized (data-driven) tests
* Retry mechanism for flaky tests
* Parallel execution (pytest-xdist)

### 📊 Reporting

* Allure Reports (rich UI)
* HTML reports
* Postman HTML reports

### ⚙️ Configuration Management

* YAML-based config system
* Environment support (`dev`, `staging`, etc.)
* CLI overrides (browser, env)

### 🧾 Logging

* Centralized logging system
* Logs for UI, API, DB layers

### 🚀 CI/CD Pipeline

* GitHub Actions integration
* Automated test execution
* Allure report deployment (GitHub Pages)
* Postman test execution via Newman

### 🧪 Mock API Server

* Built with FastAPI
* Ensures deterministic and reliable API tests

### 🐳 Containerized Infrastructure

* Docker Compose orchestration
* Selenium standalone Chrome container
* FastAPI mock server container
* PyTest execution container
* Persistent report and artifact volumes
* Environment-isolated execution

---

# 📁 Project Structure

```text
fullstack-qa-automation-framework/
│
├── tests/
│   ├── ui/
│   ├── api/
│   └── db/
│
├── pages/
│
├── framework/
│   ├── core/
│   ├── api/
│   ├── db/
│   └── utils/
│
├── mock_server/
│
├── postman/
│
├── config/
│
├── reports/
├── allure-results/
├── screenshots/
├── logs/
│
├── .github/
│   └── workflows/
│
├── docker-compose.yml
├── Dockerfile
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# 🧠 Framework Architecture

```text
                    GitHub Actions
                           │
                           ▼
                  Docker Compose Stack
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
 Selenium Container   Mock API Server    PyTest Container
        │                  │                  │
        ▼                  ▼                  ▼
 Chrome Browser       FastAPI Service    UI/API/DB Tests
                           │
                           ▼
                    Allure Reports
```

---

## UI Layer

Handles frontend automation using Selenium WebDriver and the Page Object Model (POM).

---

## API Layer

Handles backend validation using:

- Python API client
- Postman collections
- Newman CLI execution

---

## Database Layer

Validates backend data consistency using SQLite queries and API-to-DB validation checks.

---

## Infrastructure Layer

Provides:

- Dockerized execution
- Service orchestration
- Environment isolation
- CI/CD integration
- Artifact persistence

---

# ▶️ Running Tests

## 🔹 Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔹 Run all tests

```bash
pytest tests --env=dev
```

---

## 🔹 Run with parallel execution

Run tests concurrently using pytest-xdist:

```bash
pytest tests -n 2
```

Example:

```bash
pytest tests/ui -n 2 --env=local
```

---

## 🔹 Run specific layer

```bash
pytest tests/ui
pytest tests/api
pytest tests/db
```

---

# 🌍 Environment Modes

The framework supports multiple execution environments.

| Mode | Description |
|------|-------------|
| local | Local Selenium + local mock server |
| dev | Dockerized execution |
| CI | GitHub Actions pipeline |

---

## Local Execution

### Start Selenium

```bash
docker run -d -p 4444:4444 selenium/standalone-chrome:4.21.0
```

### Start Mock Server

```bash
uvicorn mock_server.app:app --host 127.0.0.1 --port 8000
```

### Run Tests

```bash
pytest --env=local
```

---

## Docker Execution

```bash
docker compose up --build
```

---

# 📊 Reporting

## Allure Report

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

👉 CI Report (GitHub Pages):
https://cyphermorgan.github.io/fullstack-qa-automation-framework/

---

## Postman (Newman)

```bash
newman run postman/Hybrid_QA_API.postman_collection.json
```

HTML report:

```bash
reports/postman_report.html
```

---

# 🧪 Mock API Server

Run locally:

```bash
uvicorn mock_server.app:app --reload
```

Base URL:

```bash
http://127.0.0.1:8000
```

---

# 🔄 CI/CD Pipeline

GitHub Actions automatically:

* Runs UI + API + DB tests
* Executes Postman collection
* Generates Allure report
* Deploys report to GitHub Pages

---

# 🐳 Dockerized Execution

This framework supports fully containerized execution using Docker Compose.

Services include:

- Selenium standalone Chrome
- FastAPI mock server
- PyTest execution container

## Build Containers

```bash
docker compose build
```

## Run Full Stack

```bash
docker compose up --build
```

## Stop Containers

```bash
docker compose down
```

---

# Container Architecture

```text
automation-tests
    ↓
selenium container
    ↓
chrome browser

automation-tests
    ↓
mock-server container
```

---

# 🔍 Example Test Flow

```text
Start CI pipeline
    ↓
Start Mock API
    ↓
Run PyTest (UI + API + DB)
    ↓
Run Postman (Newman)
    ↓
Validate API ↔ DB consistency
    ↓
Generate Allure report
    ↓
Deploy report to GitHub Pages
```

---

# 🚀 What This Project Demonstrates

* Real-world QA automation architecture
* Multi-layer validation strategy
* CI/CD integration
* Clean, scalable framework design
* Strong debugging & reporting practices

---

# 📚 Key Engineering Concepts Practiced

* Remote WebDriver execution
* Docker container orchestration
* Environment-based configuration management
* CI/CD pipeline integration
* Service isolation and dependency management
* Parallel test execution
* API mocking strategies
* Multi-layer validation (UI + API + DB)
* Persistent reporting and artifact handling
* Scalable test framework architecture

---

# 👤 Author

Designed to simulate a modern enterprise-grade QA automation ecosystem with UI, API, database, reporting, containerization, and CI/CD integration.

---

# ⭐ If you like this project

Give it a ⭐ and feel free to fork & extend it!