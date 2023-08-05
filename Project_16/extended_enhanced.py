import csv


class Ticket:
    def __init__(self, ticket_id, customer_name, issue_description, priority):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.priority = priority


class TicketingSystem:
    def __init__(self):
        self.tickets = []
        self.load_tickets()

    def load_tickets(self):
        try:
            with open("tickets.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    ticket_id, customer_name, issue_description, priority = row
                    ticket = Ticket(int(ticket_id), customer_name, issue_description, int(priority))
                    self.tickets.append(ticket)
        except FileNotFoundError:
            pass

    def save_tickets(self):
        with open("tickets.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for ticket in self.tickets:
                writer.writerow([ticket.ticket_id, ticket.customer_name, ticket.issue_description, ticket.priority])

    def create_ticket(self, customer_name, issue_description, priority):
        ticket_id = len(self.tickets) + 1
        ticket = Ticket(ticket_id, customer_name, issue_description, priority)
        self.tickets.append(ticket)
        self.save_tickets()
        print("Ticket created successfully!")

    def process_tickets(self):
        if not self.tickets:
            print("No tickets to process.")
            return

        # Sorting tickets based on priority (higher priority first)
        sorted_tickets = sorted(self.tickets, key=lambda ticket: ticket.priority, reverse=True)

        print("Processing tickets:")
        for idx, ticket in enumerate(sorted_tickets, start=1):
            print(f"Ticket {ticket.ticket_id}:")
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
      