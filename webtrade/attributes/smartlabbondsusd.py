class smartlabbondsusd:
    __slots__ ='bond_category', 'ticker', 'last_deal', 'sec_name', 'redemption','years_till_redemption', 'pers_profit', 'annual_bond_pers_profit', 'last_deals_bond_pers_profit', 'price','volume_thousand_usd', 'bond_usd', 'frequency_in_year', 'nkd_usd','bond_date', 'oferta'
    def __init__(self,
                 bond_category,
                 ticker,
                 last_deal, 
                 sec_name, 
                 redemption,
                 years_till_redemption, 
                 pers_profit, 
                 annual_bond_pers_profit, 
                 last_deals_bond_pers_profit, 
                 price,
                 volume_thousand_usd,
                 bond_usd, 
                 frequency_in_year, 
                 nkd_usd,
                 bond_date, 
                 oferta
                ):
      
        self.bond_category=bond_category
        self.ticker=ticker
        self.last_deal=last_deal
        self.sec_name= sec_name
        self.redemption=redemption
        self.years_till_redemption=years_till_redemption 
        self.pers_profit=pers_profit
        self.annual_bond_pers_profit= annual_bond_pers_profit
        self.last_deals_bond_pers_profit= last_deals_bond_pers_profit
        self.price=price
        self.volume_thousand_usd=volume_thousand_usd
        self.bond_usd=bond_usd
        self.frequency_in_year=frequency_in_year 
        self.nkd_usd=nkd_usd
        self.bond_date=bond_date 
        self.oferta=oferta