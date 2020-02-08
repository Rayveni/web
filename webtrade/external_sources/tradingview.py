from requests import Session
import lxml.html as lh
import re
import time
from .thread_pool import thread_pool

class tradingview:
    __slots__='url','http_headers','sources'
    def __init__(self):
        self.url:str=r'https://ru.tradingview.com'
        self.sources:dict={'rus_sectorandindustry':r'/markets/stocks-russia/sectorandindustry-industry/'
                          }                    
        self.http_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}          
            
               
    def __init_session(self):
        s = Session()
        s.headers.update(self.http_headers)
        return s
		
    def __transform_str(self,text):
        return text.replace('\t','').replace('\n','')

    def parse_sector(self,sector_url,session) :
        try:
            _sector_url=self.url+sector_url
            page=session.get(_sector_url)   

            doc = lh.fromstring(page.content)
            table_body = doc.xpath('//tbody[@class="tv-data-table__tbody"]')[0]
            r=[]
            for row  in table_body.getchildren():
                _list=row[0].text_content().split('\t')
                _extract=[]
                for el in _list:
                    _el=self.__transform_str(el)
                    if len(_el)>0:
                        _extract.append(_el)
                r.append([*_extract,row[4].text_content()])              
        except:
            [False,None,None]
                
        return [True,sector_url,r]
            
    
    def rus_security_sector(self)->tuple:
        s=self.__init_session()
        
        page=s.get(self.url+self.sources['rus_sectorandindustry'])   
        doc = lh.fromstring(page.content)

        res=[]       
        table_body = doc.xpath('//tbody[@class="tv-data-table__tbody"]')[0]
        
        extract_r=lambda _row:list(map(lambda f:self.__transform_str(f.text_content()),[_row[0],_row[-2]]))
       
        _urls={row.xpath('.//@href')[0]:extract_r(row) for row in table_body.getchildren()}
        _worker=lambda url:self.parse_sector(url,s)
        
        n_tries=3
        n_threads=8
        final_res=[]
        while n_tries>0:
            true_res,false_res=thread_pool(_worker,list(_urls.keys()),n_threads)
            final_res=final_res+true_res
            if len(false_res)==0:
                break
            _urls=false_res
            print(n_tries)
            n_threads=n_threads/2
            n_tries-=1
        if len(false_res)>0:
            return (False,)
        else:
            return (True,[[el[1],_urls[el[0]]] for el in final_res])
