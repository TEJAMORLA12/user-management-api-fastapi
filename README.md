# 🚀 User Management API (FastAPI)

This is a RESTful API built using FastAPI for managing users with basic CRUD operations.

## 🔧 Tech Stack
- Python
- FastAPI
- Uvicorn

## 📌 Features
- Create User (POST)
- Get All Users (GET)
- Get User by ID (GET)
- Delete User (DELETE)

## 📡 API Endpoints

| Method | Endpoint        | Description         |
|--------|----------------|---------------------|
| POST   | /users         | Create a user       |
| GET    | /users         | Get all users       |
| GET    | /users/{id}    | Get user by ID      |
| DELETE | /users/{id}    | Delete a user       |

## ▶️ Run Locally

```bash
pip install fastapi uvicorn
uvicorn main:app --reload