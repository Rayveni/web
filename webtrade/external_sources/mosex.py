#http://iss.moex.com/iss/reference/
#http://iss.moex.com/iss/securitygroups/stock_index/collections
import requests
from .thread_pool import thread_pool
from functools import partial
from time import sleep

class mosex:
    __slots__ = ['base_url','references_dict','return_data_type','error']

    def __init__(self):
        self.base_url = r'http://iss.moex.com/iss/'

        self.references_dict ={'securities_list':{'link':'securities'
                                                 ,'chunk':False},
                               'global_dict':{'link':r'index'
                                               ,'chunk':False}
                                ,'security_spec':{'link':r'securities/{r[security]}'
                                                  ,'chunk':False}
                                ,'security_history':{'link':r'history/engines/{r[engine]}/markets/{r[market]}/securities/{r[security]}'
                                                     ,'chunk':True}
                               ,'index_list':{'link':r'statistics/engines/stock/markets/index/analytics'
                                             , 'chunk':False}
                               }
        self.return_data_type='json'

    def __common_structure(self,_resp):
        return {'data':_resp['data'],'columns':_resp['columns']}
        
    def __url_construct(self,reference,params=None):
 
        url='{0}{1}.{2}'.format(self.base_url,self.references_dict[reference]['link'],self.return_data_type)
        if params is not None:
            url=url.format(r=params)
        return url
           
    def query(self,reference,reference_params=None):
        url=self.__url_construct(reference,params=reference_params) 
        return requests.get(url).json()
    
    def __security_hist_worker(self,session,url:str,params:dict,start:int)->tuple:
        response=session.get(url , params = {'start' :start,**params})
        if response.ok:
            return True,response.json()['history']
        return (False,start)
        
    def security_hist(self,security:str,engine:str,market:str,date_from:str='2016-01-01',n_threads:int=7)->tuple:
        url=self.__url_construct('security_history'
                                 ,params={'engine':engine
                                          ,'market':market
                                          ,'security':security}
                                 )
                              
        query_params={'from':date_from}
        s = requests.Session()
        response=s.get(url , params = {'start' :0,**query_params})
        start_cursor,end_cursor,step=response.json()['history.cursor']['data'][0]
     
        worker=partial(self.__security_hist_worker,s,url,query_params)     
        i=0
        true_results_final=[]
        worker_args=[i for i in range(start_cursor,end_cursor,step)]
		
        while i < 6:
            true_results,false_results=thread_pool(worker,worker_args,n_threads=n_threads)
            true_results_final=true_results+true_results_final
            if len(false_results)==0:			
                break    			
            worker_args=false_results[1]
            sleep(1)
            i+=1

        s.close()
        if len(false_results)>0:
            return (False,)
        columns=true_results_final[0]['columns']
        return True,{'columns':columns,'data':sum([el['data'] for el in true_results_final], [])}
    
    def industry_indices_list(self,img):
        start_point=(41,66)
        step_params=(154,20)
        n_chunks= (img.size[1]-start_point[1])//step_params[1]
        chunks=[img.crop((start_point[0]
                        ,start_point[1]+i*step_params[1]
                        ,step_params[0]
                        ,start_point[1]+(i+1)*step_params[1])) 
                for i in range(n_chunks)]
        return chunks
    
    def get_security_spec(self,security_spec):
        r=self.query('security_spec',{'security':security_spec})
        return self.__common_structure(r['description'])

    def get_index_list(self):
        r=self.query('index_list')
        return self.__common_structure(r['indices'])     

		
#iis.__url_construct('security_spec',{'security':'RTSog'})
#r=iis.query('security_spec',{'security':'RTSog'})
#r=iis.security_hist('RTSog','stock','index',n_threads=7)
#iis.security_hist('RTSFN','stock','index',n_threads=7,date_from='2016-01-01')
#iis.security_hist('GAZP','stock','shares',n_threads=7,date_from='2016-01-01')