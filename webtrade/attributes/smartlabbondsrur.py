class smartlabbondsrur:
    __slots__ ='bond_category', 'ticker', 'last_deal', 'sec_name', 'redemption', 'oferta','years_till_redemption', 'pers_profit', 'duraction_years', 'ofz_type', 'annual_bond_pers_profit','last_deals_bond_pers_profit', 'price', 'volume_rur_mln', 'bond_rur','frequency_in_year', 'nkd_rur', 'bond_date'
    def __init__(self,
                 bond_category, 
                 ticker,
                 last_deal,
                 sec_name, 
                 redemption, 
                 oferta,
                 years_till_redemption,
                 pers_profit,
                 duraction_years,
                 ofz_type,
                 annual_bond_pers_profit,
                 last_deals_bond_pers_profit,
                 price,
                 volume_rur_mln,
                 bond_rur,
                 frequency_in_year,
                 nkd_rur, 
                 bond_date):
        self.bond_category= bond_category
        self.ticker=ticker
        self.last_deal=last_deal
        self.sec_name=sec_name 
        self.redemption= redemption
        self.oferta=oferta
        self.years_till_redemption=years_till_redemption
        self.pers_profit=pers_profit
        self.duraction_years=duraction_years
        self.ofz_type=ofz_type
        self.annual_bond_pers_profit=annual_bond_pers_profit
        self.last_deals_bond_pers_profit=last_deals_bond_pers_profit
        self.price=price
        self.volume_rur_mln=volume_rur_mln
        self.bond_rur=bond_rur
        self.frequency_in_year=frequency_in_year
        self.nkd_rur=nkd_rur
        self.bond_date=bond_date
   