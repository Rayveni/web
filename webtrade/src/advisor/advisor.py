from flask import render_template,request,redirect,url_for
from . import advisor_bp

#from .config_manager import config_manager
from ..commons import flash_complex_result,exception,init_db_manager




@advisor_bp.route("/bonds")
def _bonds():
    data={'title':'admin|params'}

    return render_template('bonds.html',data=data)
	
