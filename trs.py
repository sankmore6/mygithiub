class Ticket:
    def __init__(self, id, description, status):
        self.id = id
        self.description = description
        self.status = status

class TicketSystem:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, description):
        ticket_id = len(self.tickets) + 1
        ticket = Ticket(ticket_id, description, "Open")
        self.tickets.append(ticket)
        print(f"Ticket {ticket_id} created successfully.")

    def view_tickets(self):
        if not self.tickets:
            print("No tickets found.")
        else:
            print("ID\tDescription\tStatus")
            for ticket in self.tickets:
                print(f"{ticket.id}\t{ticket.description}\t{ticket.status}")

    def close_ticket(self, id):
        for ticket in self.tickets:
            if ticket.id == id:
                ticket.status = "Closed"
                print(f"Ticket {id} closed successfully.")
                return
        print(f"Ticket {id} not found.")

def main():
    ticket_system = TicketSystem()

    while True:
        print("\n1. Create Ticket")
        print("2. View Tickets")
        print("3. Close Ticket")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter ticket description: ")
            ticket_system.create_ticket(description)
        elif choice == "2":
            ticket_system.view_tickets()
        elif choice == "3":
            ticket_id = int(input("Enter ticket ID to close: "))
            ticket_system.close_ticket(ticket_id)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
