from flask import render_template
from . import upload_bp
#from .config_manager import config_manager
#from ..commons import flash_complex_result,exception

from sys import path
path.append("...")
from db_drivers import mongo_manager
config_path='config.json'

@upload_bp.route("/upload_jobs")
def _upload_jobs():
    data={'title':'uploads'}
    return render_template('index.html',data=data)	


