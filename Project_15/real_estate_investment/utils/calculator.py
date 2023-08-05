class Calculator:
    @staticmethod
    def calculate_roi(property):
        total_rental_income = property.rental_income * property.holding_period
        total_expenses = property.operating_expenses * property.holding_period
        total_profit = total_rental_income - total_expenses
        roi = (total_profit / property.purchase_price) * 100
        return roi
      