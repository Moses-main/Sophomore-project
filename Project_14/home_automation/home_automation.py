from modules.lights_module import LightsModule
from modules.temperature_module import TemperatureModule
from modules.appliances_module import AppliancesModule

class HomeAutomationSystem:
    def __init__(self):
        self.lights_module = LightsModule()
        self.temperature_module = TemperatureModule()
        self.appliances_module = AppliancesModule()

    def main_menu(self):
        while True:
            print("\nHome Automation System")
            print("1. Lights Control")
            print("2. Temperature Control")
            print("3. Appliances Control")
            print("4. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                self.lights_module.menu()
            elif choice == "2":
                self.temperature_module.menu()
            elif choice == "3":
                self.appliances_module.menu()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")

def main():
    home_system = HomeAutomationSystem()
    home_system.main_menu()

if __name__ == "__main__":
    main()
      