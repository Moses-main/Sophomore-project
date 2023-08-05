class Ticket:
    def __init__(self, customer_name, issue_description, priority):
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.priority = priority


class TicketingSystem:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, customer_name, issue_description, priority):
        # Create a new ticket instance and add it to the list of tickets
        ticket = Ticket(customer_name, issue_description, priority)
        self.tickets.append(ticket)
        print("Ticket created successfully!")

    def process_tickets(self):
        if not self.tickets:
            print("No tickets to process.")
            return

        # Sorting tickets based on priority (higher priority first)
        self.tickets.sort(key=lambda ticket: ticket.priority, reverse=True)

        print("Processing tickets:")
        for idx, ticket in enumerate(self.tickets, start=1):
            print(f"Ticket {idx}:")
            print(f"Customer Name: {ticket.customer_name}")
            print(f"Issue Description: {ticket.issue_description}")
            print(f"Priority: {ticket.priority}")
            print("-----------------------")

    def run(self):
        while True:
            print("\nCustomer Support Ticketing System")
            print("1. Create Ticket")
            print("2. Process Tickets")
            print("3. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                customer_name = input("Enter customer name: ")
                issue_description = input("Enter issue description: ")
                priority = int(input("Enter priority (1 - Low, 2 - Medium, 3 - High): "))
                self.create_ticket(customer_name, issue_description, priority)
            elif choice == "2":
                self.process_tickets()
            elif choice == "3":
                print("Exiting the ticketing system.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    ticketing_system = TicketingSystem()
    ticketing_system.run()
                 