import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class Config:
    SQLALCHEMY_DATABASE_URI = (
            os.environ.get('DATABASE_URL') or
            'sqlite:///'+os.path.join(BASE_DIR, 'blog.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
