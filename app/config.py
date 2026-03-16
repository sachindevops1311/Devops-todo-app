import os

class Config:
    DEBUG = os.getenv("DEBUG", "True") == "True"
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))
    APP_NAME = "devops-todo-app"
    VERSION = "1.0.0"
