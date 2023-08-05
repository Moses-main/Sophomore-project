class RealEstateInvestment:
    def __init__(self, purchase_price, rental_income, operating_expenses, holding_period):
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.operating_expenses = operating_expenses
        self.holding_period = holding_period
    
    def calculate_roi(self):
        total_rental_income = self.rental_income * self.holding_period
        total_expenses = self.operating_expenses * self.holding_period
        total_profit = total_rental_income - total_expenses
        roi = (total_profit / self.purchase_price) * 100
        return roi

def main():
    print("Real Estate Investment Analysis")
    print("------------------------------")
    
    purchase_price = float(input("Enter the purchase price of the property: "))
    rental_income = float(input("Enter the expected monthly rental income: "))
    operating_expenses = float(input("Enter the estimated monthly operating expenses: "))
    holding_period = int(input("Enter the holding period (in months): "))
    
    investment = RealEstateInvestment(purchase_price, rental_income, operating_expenses, holding_period)
    roi = investment.calculate_roi()
    
    print("\nInvestment Analysis Result")
    print("----------------------------")
    print(f"ROI over {holding_period} months: {roi:.2f}%")

if __name__ == "__main__":
    main()
      