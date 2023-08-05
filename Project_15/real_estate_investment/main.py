import csv
import interfaces.gui
from models.property import Property
from utils.calculator import Calculator

def load_properties(filename):
    properties = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            properties.append(Property(
                int(row['id']),
                row['name'],
                float(row['purchase_price']),
                float(row['rental_income']),
                float(row['operating_expenses']),
                int(row['holding_period'])
            ))
    return properties

def main():
    print("Real Estate Investment Analysis")
    print("------------------------------")
    
    properties = load_properties("data/properties.csv")
    
    for prop in properties:
        roi = Calculator.calculate_roi(prop)
        print(f"Property: {prop.name}")
        print(f"ROI over {prop.holding_period} months: {roi:.2f}%")
        print("-----------------------------")

# ... (previous code)

def main():
    print("Real Estate Investment Analysis")
    print("------------------------------")
    
    properties = load_properties("data/properties.csv")
    
    for prop in properties:
        roi = Calculator.calculate_roi(prop)
        print(f"Property: {prop.name}")
        print(f"ROI over {prop.holding_period} months: {roi:.2f}%")
        print("-----------------------------")

    print("\n\nLaunching GUI Interface...\n")

  
if __name__ == "__main__":
    main()
              