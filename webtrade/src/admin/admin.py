from flask import render_template,request,redirect,url_for
from datetime import datetime
from json import dumps
from . import admin_bp

from .config_manager import config_manager
from ..commons import flash_complex_result,exception

from sys import path
path.append("...")
from db_drivers import mongo_manager

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
err,config=cf_m.read_config()

@exception
def __db_stats():
    mm=mongo_manager(config)
    return mm.dbstats()	 

@exception	
def __drop_db():
    mm=mongo_manager(config)
    return mm.drop_db()	 
	
@admin_bp.route("/admin/params")
def _params():
    data={'title':'admin|params'}
    err,file_config=cf_m.read_config()
    if not err[0]:
        pass#flash_complex_result(err,res,'Mongo Database dropped')

    data['params']={key:{**value,'value':file_config[key]} for key,value in params.items()}
    data['optional_js_bottom']=['js/table_search_filter']
    return render_template('params.html',data=data)
	
@admin_bp.route("/admin/database")
def _database():
    data={'title':'admin|database'}
    err,db_stats=__db_stats()
    if not err[0]:
        flash_complex_result(err,db_stats)
        data['db_stats']={}
    else:
        data['db_stats']=db_stats     
    return render_template('database.html',data=data)
	


@exception
def __get_table(table_name,result='matrix'):
    mm=mongo_manager(config)
    return mm.get_table(table_name,result)

@exception
def __all_tables():
    mm=mongo_manager(config)
    return mm.all_tables()

@admin_bp.route("/admin/tables")
def _tables():
    data={'title':'admin|tables'}
    err,all_tables=__all_tables()
    if not err[0]:
        flash_complex_result(err,table_data)
        all_tables_list=None
    else:
        all_tables_list=all_tables
    data['optional_js_bottom']=['js/drop_down_filter','js/admin','vendor/handsontable/handsontable.full.min','js/ajax_get_data'] 
    data['optional_css_top']=['handsontable.full.min']
    data['db_drop_down_filter']={'placeholder':'Select database table','id':1,'filter_vals':all_tables_list,'onclick':"process_htable(this,'dropdown_id_1')"}
    return render_template('tables.html',data=data)
	

@admin_bp.route("/upload_mongo_form",methods=["POST"])
def upload_mongo_form():
    global config

    form_data=request.form.to_dict(flat=False) 
    submit_case=form_data['submit_button'][0]

    if submit_case=='update_config':
        err,res=cf_m.update_config('input_name_',form_data,params)
        err2,config=cf_m.read_config()	
        flash_complex_result(err,res,'Config updated')         
        return redirect(url_for('admin_bp._params'))
    
    elif submit_case=='drop_db':
        err,res=__drop_db()
        flash_complex_result(err,res,'database dropped')
        return redirect(url_for('admin_bp._database'))


def __convert_to_front(arr):
    if len (arr)>0:
        last_row=arr[-1]
        datetime_cols=[i for i in range(len(last_row)) if isinstance(last_row[i], datetime)]

        for i in range(1, len(arr)):
            for col in datetime_cols:   
                arr[i][col]=arr[i][col].strftime("%Y-%m-%d %H:%M:%S")
    return arr

@admin_bp.route('/query_data', methods=['GET', 'POST'])
def query_data():
    err,data_request=__get_table(request.args.get('table'))
    return dumps(__convert_to_front(data_request),ensure_ascii=False)

