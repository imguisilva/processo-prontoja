from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8000",
    "https://localhost:8000",
    "http://localhost:5000",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root Route
@app.get("/")
def raiz():
    return {"Task2": "API"}

# Create Model
class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    gender: str
    nationality: str
    
# Create Database
data_base = [
    User(id=1, name="Guilherme Pereira", email="guilhermesccp01@hotmail.com", password="1234Mudar#", gender="Male", nationality="Brazilian"),
    User(id=2, name="User Test", email="prontoja@gmail.com", password="test123*", gender="Male", nationality="German")
]


# Route Get All
@app.get("/users")
def get_all_users():
    return data_base

# Route Get Id
@app.get("/users/{id_user}")
def get_user_id(id_user: int):
    for user in data_base:
        if (user.id == id_user):
            return user
        
    return {"Status": 404, "Message": "User not found"}

# Route Insert
@app.post("/users")
def insert_user(user: User):
    data_base.append(user)
    return user

# Type -> uvicorn main:app --reload <- to start the server

# To insert a new user, simply access http://127.0.0.1:8000/docs, go to "POST", click "Try", insert the user's data in the field below and click "Execute".
