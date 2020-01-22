from json import load,dump
from os import path
from ..commons import exception


class config_manager:
    __slots__='params','config_path'
    def __init__(self,params:dict,config_path:str):
        self.params=params
        self.config_path=config_path
        
        if not path.exists(config_path):
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
    def update_config(self,form_data,config)->tuple:
        err,data=read_config(conf_path)


        for param in config_fields:
            data[param]=form_data[f'mongo_{param}'][0]

        with open(conf_path, 'w') as outfile:  
            dump(data, outfile)

        return (True,data)