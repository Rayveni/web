from requests import Session
import lxml.html as lh
import re
import time
from .thread_pool import thread_pool
from functools import partial
from time import sleep
class alphavantage:
    __slots__='url','http_headers','sources','token'
    def __init__(self,token):
        self.url:str=r'https://www.alphavantage.co/'
        self.__token=token       
        self.sources:dict={'daily':r'query?function=TIME_SERIES_DAILY'
                          }                    
        self.http_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}          
            
               
    def __init_session(self):
        s = Session()
        s.headers.update(self.http_headers)
        return s
		

    def __fond_index_history_worker(self,session,url:str,params:dict,ticker:str)->tuple:
        response=session.get(url , params = {'symbol' :ticker,**params})
        if response.ok:
            return True,response.json()
        return (False,ticker)


    def fond_index_history(self,tickers_list:list,full_reload:bool=True,token:str,n_threads:int=7)->tuple:
        if full_reload:
            outputsize='full'
        else:
            outputsize='compact'
        params={'outputsize':outputsize,'apikey':self.__token}
        s=self.__init_session()        
        worker=partial(self.__fond_index_history_worker,s,self.url+self.sources['daily'],params)             
    
        i,true_results_final=0,[]

        while i < 6:
            true_results,false_results=thread_pool(worker,tickers_list,n_threads=n_threads)
            true_results_final=true_results+true_results_final
            if len(false_results)==0:
                break   
            worker_args=false_results[1]
            sleep(1)
            i+=1

        s.close()
        if len(false_results)>0:
            return (False,)

        return True,true_results_final

