import os


class Config:
    TESTING = False
    SECRET_KEY = os.environ.get("APP_SECRET_KEY", "development-only-change-me")


class TestConfig(Config):
    TESTING = True
