from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/")
def home():
    return {"message": "API Running 🚀"}

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User created", "user": user}

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "User not found"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": "User deleted"}
    return {"error": "User not found"}