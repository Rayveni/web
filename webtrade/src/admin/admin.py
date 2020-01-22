from flask import render_template,request,redirect,url_for
from . import admin_bp


from .config_manager import config_manager
from ..commons import flash_complex_result,exception

config_path='config.json'
params={"driver":{"type":'str','len':32,'default':None},
        "db_name": {"type":'str','len':32,'default':None},
        "host": {"type":'str','len':32,'default':None},
        "port": {"type":'int','len':10,'default':None},
        "user": {"type":'str','len':32,'default':None},
        "user_pswd": {"type":'str','len':32,'default':None},
        "mongo_data": {"type":'str','len':64,'default':None}
       }

cf_m=config_manager(params,config_path)
  
 

@admin_bp.route("/admin/params")
def _params():
    data={'title':'admin|params'}
    err,file_config=cf_m.read_config()
    if not err[0]:
        pass#flash_complex_result(err,res,'Mongo Database dropped')

    data['params']={key:{**value,'value':file_config[key]} for key,value in params.items()}
    data['optional_js_bottom']=['table_search_filter']
    return render_template('params.html',data=data)
	
@admin_bp.route("/admin/database")
def _database():
    data={'title':'admin|database'}
    return render_template('database.html',data=data)		
	
@admin_bp.route("/admin/tables")
def _tables():
    data={'title':'admin|tables'}
    return render_template('tables.html',data=data)
	

	
@admin_bp.route("/upload_mongo_form",methods=["POST"])#,methods=["POST"]
def upload_mongo_form():
    form_data=request.form.to_dict(flat=False) 
    flash_complex_result([True,'dddddd'],[False,'2222'],'Constants updated')
    return redirect(url_for('admin_bp._database'))
    print(form_data)
    return 11
    submit_case=form_data['submit_button'][0]
    print(submit_case,form_data)	
    if submit_case=='mongo_config':
        err,res=update_config(config_path,form_data)
        flash_complex_result(err,res,'Config updated')
  
    elif submit_case=='drop_db':
        err,res=drop_db()
        flash_complex_result(err,res,'Mongo Database dropped')
    elif submit_case=='rebuild_indexes':
        flash('rebuild_indexes updated','info')  #success info error  заглушка
    elif submit_case=='Save changes':
        err,res=update_constants(form_data)	
        flash_complex_result(err,res,'Constants updated')  #success info error  заглушка		
         
    return redirect(url_for('admin_bp.index'))#render_template('admin.html',data=res[1])#
	

	
