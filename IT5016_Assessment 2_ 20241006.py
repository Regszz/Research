import random
import string


class SupportTicket:
    ticketCounter = 2000
    activeTickets = 0
    closedTickets = 0

    def __init__(self, staffID, requesterName, emailAddress, issueDesc):
        self.ticketID = SupportTicket.ticketCounter
        SupportTicket.ticketCounter += 1
        self.staffID = staffID
        self.requesterName = requesterName
        self.emailAddress = emailAddress
        self.issueDesc = issueDesc
        self.responseMessage = "Pending"
        self.status = "Active"
        SupportTicket.activeTickets += 1
        self.generatedPassword = None

    def showTicket(self):
        print(f"Ticket ID: {self.ticketID}")
        print(f"Requester: {self.requesterName}")
        print(f"Staff ID: {self.staffID}")
        print(f"Email: {self.emailAddress}")
        print(f"Issue Description: {self.issueDesc}")
        print(f"Response: {self.responseMessage}")
        if self.generatedPassword:
            print(f"Password: {self.generatedPassword}")
        print(f"Status: {self.status}\n")

    def addResponse(self, response):
        self.responseMessage = response
        self.status = "Closed"
        SupportTicket.activeTickets -= 1
        SupportTicket.closedTickets += 1

    def processPasswordChange(self):
        if "password change" in self.issueDesc.lower():
            newPassword = self.createPassword()
            self.responseMessage = f"Password has been changed to: {newPassword}"
            self.status = "Closed"
            SupportTicket.activeTickets -= 1
            SupportTicket.closedTickets += 1
            self.generatedPassword = newPassword

    def createPassword(self):
        staffID_chars = self.staffID[:2]
        requesterName_chars = self.requesterName[3:]

        random_chars = ''.join(random.choices(string.ascii_letters, k=3))

        newPassword = staffID_chars + requesterName_chars + random_chars

        return newPassword

    def reopen(self):
        self.status = "Reopened"
        SupportTicket.activeTickets += 1
        SupportTicket.closedTickets -= 1

    @classmethod
    def getTicketStats(cls):
        return (f"Tickets Created: {cls.ticketCounter - 2000}\n"
                f"Tickets Resolved: {cls.closedTickets}\n"
                f"Tickets To Resolve: {cls.activeTickets}")


def main():
    ticket_list = []

    while True:
        print("\nMenu:")
        print("1. Create New Ticket")
        print("2. Close a Ticket")
        print("3. Process Password Change Request")
        print("4. View All Tickets")
        print("5. View Active Tickets")
        print("6. View Closed Tickets")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            requesterName = input("Enter Requester Name: ")
            staffID = input("Enter Staff ID: ")
            emailAddress = input("Enter Email Address: ")
            issueDesc = input("Enter Issue Description: ")

            ticket_list.append(SupportTicket(staffID, requesterName, emailAddress, issueDesc))
            print("Ticket created successfully.")
        elif choice == "2":
            for i, ticket in enumerate(ticket_list, start=1):
                print(f"{i}. Ticket ID: {ticket.ticketID} (Status: {ticket.status})")
            ticket_index = int(input("Enter the index of the ticket to close: ")) - 1
            if 0 <= ticket_index < len(ticket_list):
                response = input("Enter response for the selected ticket: ")
                ticket_list[ticket_index].addResponse(response)
                print("Ticket closed successfully.")
            else:
                print("Invalid ticket index.")
        elif choice == "3":
            print("Active Tickets:\n")
            for i, ticket in enumerate(ticket_list, start=1):
                if ticket.status == "Active":
                    print(f"{i}. Ticket ID: {ticket.ticketID} (Status: {ticket.status})")

            ticket_index = int(input("Enter the index of the password change request: ")) - 1
            if 0 <= ticket_index < len(ticket_list):
                ticket_list[ticket_index].processPasswordChange()
                print("Password changed successfully.")
            else:
                print("Invalid ticket index.")
        elif choice == "4":
            print("\nAll Tickets:")
            for ticket in ticket_list:
                ticket.showTicket()
            print("\nTicket Statistics:")
            print(SupportTicket.getTicketStats())
        elif choice == "5":
            print("\nActive Tickets:\n")
            for ticket in ticket_list:
                if ticket.status == "Active":
                    ticket.showTicket()
            print("\nTicket Statistics:\n")
        elif choice == "6":
            print("\nClosed Tickets:\n")
            for ticket in ticket_list:
                if ticket.status == "Closed":
                    ticket.showTicket()
            print("\nTicket Statistics:\n")
            print(SupportTicket.getTicketStats())
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
