class HomeAutomationSystem:
    def __init__(self):
        self.lights = False
        self.temperature = 25.0
        self.appliances = False
    
    def toggle_lights(self):
        self.lights = not self.lights
        status = "on" if self.lights else "off"
        print(f"Lights are now {status}")
    
    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Temperature set to {self.temperature}°C")
    
    def toggle_appliances(self):
        self.appliances = not self.appliances
        status = "on" if self.appliances else "off"
        print(f"Appliances are now {status}")
    
def main():
    home_system = HomeAutomationSystem()
    
    while True:
        print("\nHome Automation System")
        print("1. Toggle Lights")
        print("2. Set Temperature")
        print("3. Toggle Appliances")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            home_system.toggle_lights()
        elif choice == "2":
            temperature = float(input("Enter temperature in °C: "))
            home_system.set_temperature(temperature)
        elif choice == "3":
            home_system.toggle_appliances()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()