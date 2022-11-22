class CompoundInterest:
    def __init__(self, principal, percent, year, monthly_con):
        self.principal = principal
        self.percent = percent / 100
        self.number_of_time_per_year = 12
        self.interest = self.percent / self.number_of_time_per_year
        self.year = year
        self.monthly_con = monthly_con
        self.investment = self.principal * (1 + self.interest) ** (self.number_of_time_per_year * self.year)

    def invest_without_monthly_contribution(self):
        return round(self.investment, 2)
        

    def invest_with_monthly_contribution(self): 
        return round(self.investment + self.monthly_con * (((1 + self.interest)**(self.number_of_time_per_year* self.year)-1)/ self.interest) * (1 + self.interest), 2)
