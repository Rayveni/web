from flask import render_template,request,redirect,url_for
from . import advisor_bp

#from .config_manager import config_manager
from ..commons import flash_complex_result,exception,init_db_manager

@exception
def __last_updated_bonds():
    return init_db_manager().find_one('upload_info',
                                      {"sys_name": "smartlabbondsusd"},
                                      return_fields=['sys_updated'])['sys_updated'].strftime("%Y-%m-%d %H:%M:%S")

@advisor_bp.route("/bonds")
def _bonds():
    data={'title':'admin|params'}
    data['optional_css_top']=['daterangepicker']
    err,last_updated_date=__last_updated_bonds()
  
    if not err[0]:
        flash_complex_result(err,last_updated_date)
        last_updated_date='error updated date'		


    data['last_updated_date']=last_updated_date	
    data['optional_js_bottom']=['vendor/daterangepicker/moment.min','vendor/daterangepicker/daterangepicker.min','js/bonds'] 	
    return render_template('bonds.html',data=data)
	
