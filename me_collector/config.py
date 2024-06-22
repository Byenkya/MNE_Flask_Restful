import os

with open('me_collector/secret.key', 'r') as f:
    secret_key = f.read().strip()


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static/projectUploads')
    UPLOAD_FOLDER = 'me_collector/static/projectUploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    SECRET_KEY = secret_key
