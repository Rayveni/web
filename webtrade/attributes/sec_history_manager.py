class sec_history_manager:
    __slots__ ='ticker','sec_name','currency','start_date','end_date','current_year'
    def __init__(self,ticker:str,sec_name:str,currency:str,start_date:str,end_date:str,current_year:int):
        self.ticker=ticker
        self.start_date=start_date
        self.sec_name=sec_name         
        self.currency=currency  
        self.end_date=end_date
        self.current_year=current_year