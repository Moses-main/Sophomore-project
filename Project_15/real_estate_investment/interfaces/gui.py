import tkinter as tk
from tkinter import messagebox
from models.property import Property
from utils.calculator import Calculator

class RealEstateGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Real Estate Investment Analysis")
        
        self.load_properties_button = tk.Button(self.root, text="Load Properties", command=self.load_properties)
        self.load_properties_button.pack()
        
        self.result_text = tk.Text(self.root, height=10, width=40)
        self.result_text.pack()
        
    def load_properties(self):
        properties = load_properties("data/properties.csv")
        self.result_text.delete('1.0', tk.END)
        
        for prop in properties:
            roi = Calculator.calculate_roi(prop)
            result = f"Property: {prop.name}\nROI over {prop.holding_period} months: {roi:.2f}%\n\n"
            self.result_text.insert(tk.END, result)

def main():
    root = tk.Tk()
    app = RealEstateGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
      