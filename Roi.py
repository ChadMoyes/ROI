class RentalProperty:
    def __init__(self, income, expenses, investment):
        self.income = income #This is a dictionary for storing where the income comes from
        self.expenses = expenses #This is a dictionary for the expenses of the property
        self.investment = investment #This is a dictionary for the cost of all investments

    #I use .values() because we only want the sum of the money in the dictionaries, not the keys.

    def calculate_total_income(self):
        return sum(self.income.values()) #This will return a sum of the total monthly income
    
    def calculate_total_expenses(self):
        return sum(self.expenses.values()) #This will return a sum of the total monthly expenses
    
    def calculate_cash_flow(self):
        total_income = self.calculate_total_income()
        total_expenses = self.calculate_total_expenses()
        return total_income - total_expenses #subtracts the expenses from the income so we learn cash flow
    
    def calculate_roi(self):
        #Annual cash flow
        monthly_cash_flow = self.calculate_cash_flow()
        annual_cash_flow = monthly_cash_flow * 12

        #The total investment
        total_investment = sum(self.investment.values())
        
        #ROI
        roi = (annual_cash_flow / total_investment) * 100 #We turn it to a percentage
        return roi 
    
income = {'retnal_income' : 2000}
expenses = {
    'tax' : 150, 'insurance': 100, 'utilities': 0, 'HOA' : 0, 'vacancy': 100, 'repairs': 100, 'capEx': 100,
    'property_management': 200, 'mortgage': 860
}
investment = {'down_payment': 40000, 'closing_costs': 3000, 'rehab_budget': 7000, 'misc': 0}

first_property = RentalProperty(income, expenses, investment)
print("Total Monthly Income:", first_property.calculate_total_income())
print("Total Monthly Expenses:", first_property.calculate_total_expenses())
print("Monthly Cash Flow:", first_property.calculate_cash_flow())
print("Cash-on-Cash ROI", first_property.calculate_roi())