class LightsModule:
    def __init__(self):
        self.lights = False
    
    def toggle_lights(self):
        self.lights = not self.lights
        status = "on" if self.lights else "off"
        print(f"Lights are now {status}")
    
    def menu(self):
        while True:
            print("\nLights Control")
            print("1. Toggle Lights")
            print("2. Back")

            choice = input("Select an option: ")

            if choice == "1":
                self.toggle_lights()
            elif choice == "2":
                break
            else:
                print("Invalid choice. Please select a valid option.")
      