from flask import render_template
from . import admin_bp
#from backend import engine,assets_management
#from json import load,dump,dumps

#config_path='config.json'
@admin_bp.route("/admin")
def _params():
    data={'title':'admin|params'}
    params={"driver":{"type":'str','len':32},
            "db_name": {"type":'str','len':32},
            "host": {"type":'str','len':32},
            "port": {"type":'int','len':32},
            "user": {"type":'str','len':32},
            "user_pswd": {"type":'str','len':32},
            "mongo_data": {"type":'str','len':64}
           }
    data['params']=params
	
    data['optional_js_bottom']=['table_search_filter']	
    return render_template('params.html',data=data)
	
@admin_bp.route("/database")
def _database():
    data={'title':'admin|database'}
    return render_template('database.html',data=data)		
	
@admin_bp.route("/tables")
def _tables():
    data={'title':'admin|tables'}
    return render_template('tables.html',data=data)