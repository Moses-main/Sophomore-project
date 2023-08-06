class CustomerSupportTicket:
    def __init__(self, customer_name, issue_description, priority):
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.priority = priority

class TicketingSystem:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, customer_name, issue_description, priority):
        ticket = CustomerSupportTicket(customer_name, issue_description, priority)
        self.tickets.append(ticket)
        self.tickets.sort(key=lambda x: x.priority, reverse=True)

    def process_tickets(self):
        while self.tickets:
            ticket = self.tickets.pop(0)
            print(f"Processing ticket from {ticket.customer_name} - Priority: {ticket.priority}")
            print(f"Issue Description: {ticket.issue_description}")
            print("Ticket resolved.\n")

    def delete_ticket(self, index):
        if 0 <= index < len(self.tickets):
            deleted_ticket = self.tickets.pop(index)
            print(f"Ticket from {deleted_ticket.customer_name} with priority {deleted_ticket.priority} deleted.")
        else:
            print("Invalid ticket index.")

    def list_customers_by_priority(self):
        sorted_tickets = sorted(self.tickets, key=lambda x: x.priority, reverse=True)
        for index, ticket in enumerate(sorted_tickets):
            print(f"{index + 1}. Customer: {ticket.customer_name} - Priority: {ticket.priority}")

def main():
    ticket_system = TicketingSystem()

    while True:
        print("1. Create a ticket")
        print("2. Process tickets")
        print("3. Delete a ticket")
        print("4. List customers by priority")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            customer_name = input("Enter customer name: ")
            issue_description = input("Enter issue description: ")
            priority = int(input("Enter priority (1 - Low, 2 - Medium, 3 - High): "))
            ticket_system.create_ticket(customer_name, issue_description, priority)
            print("Ticket created successfully.\n")

        elif choice == '2':
            ticket_system.process_tickets()

        elif choice == '3':
            index = int(input("Enter the index of the ticket to delete: "))
            ticket_system.delete_ticket(index)

        elif choice == '4':
            ticket_system.list_customers_by_priority()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
      