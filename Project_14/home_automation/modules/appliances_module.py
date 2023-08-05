class AppliancesModule:
    def __init__(self):
        self.appliances = False
    
    def toggle_appliances(self):
        self.appliances = not self.appliances
        status = "on" if self.appliances else "off"
        print(f"Appliances are now {status}")
    
    def menu(self):
        while True:
            print("\nAppliances Control")
            print("1. Toggle Appliances")
            print("2. Back")

            choice = input("Select an option: ")

            if choice == "1":
                self.toggle_appliances()
            elif choice == "2":
                break
            else:
                print("Invalid choice. Please select a valid option.")
      