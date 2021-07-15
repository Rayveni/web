from json import load,dump
from os import path
from .exception_func import exception


class config_manager:
    __slots__='params','config_path'
    def __init__(self):
        self.params={"driver":{"type":'str','len':32,'default':None},
                     "db_name": {"type":'str','len':32,'default':None},
                     "host": {"type":'str','len':32,'default':None},
                     "port": {"type":'int','len':10,'default':None},
                     "user": {"type":'str','len':32,'default':None},
                     "user_pswd": {"type":'str','len':32,'default':None},
                     "mongo_data": {"type":'str','len':64,'default':None},"open_broker_report":{"type":'str','len':64,'default':None}
                    }
        self.config_path='config.json'
        
        if not path.exists(self.config_path):
            self._create_config()            
        
    def _create_config(self)->bool:
        data={key:value['default'] for key,value in self.params.items()}

        with open(self.config_path, 'w') as outfile:  
             dump(data, outfile)
        print("empty config created")
    @exception
    def read_config(self)->dict:
        with open(self.config_path) as json_file:  
            data = load(json_file)
        none_replace=lambda t:'' if t is None else t		
        return {key:none_replace(value) for key,value	in data.items()}

    @exception
    def update_config(self,prefix:str,form_data:dict)->tuple:
        data={}
        for key,value in self.params.items():
            _value,len_match=self._format_convert(form_data[prefix+key][0],value['type'],value['len'])
            if len_match:
                data[key]=_value
            else:
                return (False,f'Length {key}={_value} shoud be less then {value["len"]} ')

        with open(self.config_path, 'w') as outfile:  
            dump(data, outfile)

        return (True,data)

    def _format_convert(self,t,_format:str,_len:int)->tuple:
        _s=str(t)
        _n=len(_s)<=_len
        if _format=='str':
            return _s,_n
        elif _format=='int':
            return int(t),_n
        else:
            pass