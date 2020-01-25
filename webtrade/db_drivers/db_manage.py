import datetime
from pymongo import MongoClient,DESCENDING,ASCENDING
from pandas import DataFrame
from bson.son import SON

class MongoDriver:
    __slots__ ='config','__client','db'
    def __init__(self,config: dict):
        self.config={key:value for key,value in config if key in ['host','port','db_name']}
        for el in ['host','port']:
            if self.config[el]=='':
                self.config[el]=None
        self.__client=MongoClient(config['host'],config['port'])
        self.db=self.__client[self.config['db_name']]


    def drop_db(self):
        self.__client.drop_database(self.db.name)
        #self.__add_indexes()

    def all_tables(self):
        return [collection for collection in self.db.collection_names()]
 
    def table_exists(self,col_name):
        return self.config[col_name] in self.all_tables()
      
    def create_table(self,table_def=None):
        pass
 
