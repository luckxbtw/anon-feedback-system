from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import feedback, auth

app = FastAPI(title="Anonymous Feedback API", version="1.0")

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(feedback.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Welcome"}