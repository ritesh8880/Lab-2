from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class User(UserCreate):
    id: int

users: List[User] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI REST API assignment"}

@app.get("/users", response_model=List[User])
def read_users():
    return users

@app.post("/users", response_model=User, status_code=201)
def create_user(user_in: UserCreate):
    user = User(id=len(users) + 1, **user_in.dict())
    users.append(user)
    return user

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_in: UserCreate):
    for idx, user in enumerate(users):
        if user.id == user_id:
            updated_user = User(id=user_id, **user_in.dict())
            users[idx] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    for idx, user in enumerate(users):
        if user.id == user_id:
            users.pop(idx)
            return
    raise HTTPException(status_code=404, detail="User not found")

# run with: uvicorn starter-code:app --reload
