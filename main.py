from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

# 假設的資料庫操作
def get_db():
    pass  # 這裡會是實際的資料庫 session

def create_user_in_db(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_from_db(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

@app.post("/users")
def create_user(user: User, db: Session = Depends(get_db)):
    return create_user_in_db(db, user)

@app.get("/users/{email}")
def get_user(email: str, db: Session = Depends(get_db)):
    return get_user_from_db(db, email)
