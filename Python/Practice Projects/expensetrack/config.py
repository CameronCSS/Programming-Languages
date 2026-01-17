import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "super-secret-key")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "postgresql://postgres:postgres@db:5432/expensetrack"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "super-jwt-secret")
