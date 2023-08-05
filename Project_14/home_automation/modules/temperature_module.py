from helpers.temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius

class TemperatureModule:
    def __init__(self):
        self.temperature = 25.0
    
    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Temperature set to {self.temperature}°C")
    
    def menu(self):
        while True:
            print("\nTemperature Control")
            print("1. Set Temperature (°C)")
            print("2. Set Temperature (°F)")
            print("3. Back")

            choice = input("Select an option: ")

            if choice == "1":
                temperature = float(input("Enter temperature in °C: "))
                self.set_temperature(temperature)
            elif choice == "2":
                temperature_f = float(input("Enter temperature in °F: "))
                temperature_c = fahrenheit_to_celsius(temperature_f)
                self.set_temperature(temperature_c)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please select a valid option.")
      