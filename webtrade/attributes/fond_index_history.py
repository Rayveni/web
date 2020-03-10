class fond_index_history:
    __slots__ ='ticker','year','history'
    def __init__(self,ticker:str,year:int,history:list):
        self.ticker=ticker
        self.year=year
        self.history=[ {'date':row['date'],
                        'open':float(row['1. open']),
                        'hight':float(row['2. high']),
                        'low':float(row['3. low']),
                        'close':float(row['4. close']),
                        'volume':int(row['5. volume'])
                       } for row in history]