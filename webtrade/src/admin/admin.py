from flask import render_template,request,redirect,url_for
from datetime import datetime
from json import dumps
from . import admin_bp

#from .config_manager import config_manager
from ..commons import flash_complex_result,exception,config_manager

from sys import path
path.append("...")
from db_drivers import mongo_manager

cf_m=config_manager()
err,config=cf_m.read_config()

@exception
def __db_stats():
    mm=mongo_manager(config)
    return mm.dbstats()	 
    
@exception
def __current_tokens()->dict:
    mm=mongo_manager(config)
    if mm.table_exists('api_tokens'):
        return mm.get_table('api_tokens')
    else:
        return None

@exception	
def __drop_db():
    mm=mongo_manager(config)
    return True,mm.drop_db()	 

@exception	
def __drop_table(table):
    mm=mongo_manager(config)
    return True,mm.drop_table(table)		
@exception
def __update_api_tokens(form_data,key_prefix,except_key):
    data=[(key[len(key_prefix):],value[0]) for key,value in form_data.items() if key !=except_key]
    from attributes import tokens
    insert_data=[tokens(*el) for el in data]
    db_manager=mongo_manager(config)
    return db_manager.insert_into_table_from_attr('api_tokens',insert_data,bulk=True,rewrite=True)   
    
    
@admin_bp.route("/admin/params")
def _params():
    data={'title':'admin|params'}
    err,file_config=cf_m.read_config()
    if not err[0]:
        pass#flash_complex_result(err,res,'Mongo Database dropped')

    data['params']={key:{**value,'value':file_config[key]} for key,value in cf_m.params.items()}
    data['optional_js_bottom']=['js/table_search_filter']
    return render_template('params.html',data=data)
    
@admin_bp.route("/admin/api_keys")
def _api_keys():
    data={'title':'admin|api keys'}
    tokens=['alphavantage']
    
    err,_tokens=__current_tokens()
    if not err[0]:
        flash_complex_result(err,_tokens)
        data['params']=None      
    else:
        if _tokens is None:
            data['params']={el:'' for el in tokens}
        else:
            _tokens={el['key']:el['value'] for el in _tokens} 
            data['params']={ el:(_tokens[el] if el in _tokens.keys() else '') for el in tokens}

    data['optional_js_bottom']=['js/table_search_filter']
    return render_template('api_keys.html',data=data)      
	
@admin_bp.route("/admin/database")
def _database():
    data={'title':'admin|database'}
    err,db_stats=__db_stats()
    if not err[0]:
        flash_complex_result(err,db_stats)
        data['db_stats']={}
    else:
        data['db_stats']=db_stats  

    err,all_tables=__all_tables()
    if not err[0]:
        flash_complex_result(err,table_data)
        all_tables_list=None
    else:
        all_tables_list=all_tables
    data['optional_js_bottom']=['js/drop_down_filter','js/admin']		
    data['db_drop_down_filter']={'placeholder':'drop table','id':1,'filter_vals':all_tables_list,'onclick':"drop_db_table(this,'dropdown_id_1')"}		
    return render_template('database.html',data=data)

@exception
def __get_table(table_name,result='matrix',view_id=None):
    mm=mongo_manager(config)
    if view_id is not None:
        return __get_view(mm,view_id,result)
    else:	
        return mm.get_table(table_name,result,query={})

def __get_view(db_manager,view_id,result):
    if view_id=="markets_index_data":
        now=datetime.now()
        start_date=now.replace(year=now.year - 5)
        return db_manager.get_table('fond_index_history',
                                    query={'date':{'$gte':start_date}},
                                    columns=['index_id','close_price','date','volume'],
                                    result=result
                                   )


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
        err,res=cf_m.update_config('input_name_',form_data)
        err2,config=cf_m.read_config()	
        flash_complex_result(err,res,'Config updated')         
        return redirect(url_for('admin_bp._params'))
    
    elif submit_case=='drop_db':
        err,res=__drop_db()
        flash_complex_result(err,res,'database dropped')
        return redirect(url_for('admin_bp._database'))
        
    elif submit_case=='update_tokens':
        err,res=__update_api_tokens(form_data,'input_name_','submit_button')
        flash_complex_result(err,res,'keys updated')
        return redirect(url_for('admin_bp._api_keys'))
		
    elif submit_case=='drop_table':
        _table=form_data['table'][0]	
        err,res=__drop_table(_table)
	
        flash_complex_result(err,res,"dddd")
			
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
    _res_form=request.args.get('result')
    _table=request.args.get('table')	
    _view_id=request.args.get('view_id')		

    if  _res_form is None:
        err,data_request=__get_table(_table,view_id=_view_id)
    else:
        err,data_request=__get_table(_table,_res_form,view_id=_view_id)	
    return dumps(__convert_to_front(data_request),ensure_ascii=False)

