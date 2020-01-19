from flask import render_template
from . import index_bp
#from backend import engine,assets_management
#from json import load,dump,dumps

#config_path='config.json'
@index_bp.route("/")
def index():
    data={'title':'index'}
    return render_template('index.html',data=data)	