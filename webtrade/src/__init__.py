from flask import Flask

from .admin import admin_bp
#from .upload_data import upload_data_bp
from .index import index_bp

app = Flask(__name__)
app.secret_key = 'random string'
app.static_folder = 'static'

app.register_blueprint(admin_bp)
#app.register_blueprint(upload_data_bp)
app.register_blueprint(index_bp)