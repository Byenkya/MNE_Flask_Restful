with open('me_collector/secret.key', 'r') as f:
    secret_key = f.read().strip()


class Config:
    UPLOAD_FOLDER = 'me_collector/static/projectUploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    SECRET_KEY = secret_key
