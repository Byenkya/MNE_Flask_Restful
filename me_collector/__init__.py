from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import urllib.parse


app = Flask(__name__)
api = Api(app)


password_with_special_chars = "Arua@2020*+"

#Encode the password
encoded_password = urllib.parse.quote_plus(password_with_special_chars)

# db_uri = 'postgresql://mne_user:123123123@172.19.0.2:5432/mne'
db_uri = 'postgresql://munigisn:Arua@2020*+@us16.acugis-dns.com:5432/munigisn_mne_demo'

# Construct the new URI with the encoded password
new_uri = db_uri.replace(password_with_special_chars, encoded_password)


app.config['SQLALCHEMY_DATABASE_URI'] = new_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/projectUploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize Flask extensions
db = SQLAlchemy(app)
