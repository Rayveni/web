class fond_index_history:
    __slots__ ='ticker','year','history'
    def __init__(self,ticker:str,year:int,history:list):
        self.ticker=ticker
        self.year=year
        self.history=[ {'date':row['date'],
                        'open':float(row['open']),
                        'hight':float(row['hight']),
                        'low':float(row['low']),
                        'close':float(row['close']),
                        'volume':int(row['volume'])
                       } for row in self.history]