import sys
from database import (
    create_table,
    add_ticket,
    get_all_tickets,
    search_ticket,
    update_ticket,
    delete_ticket
)

# Improved CLI menu formatting and user flow

def print_menu():
    print("\n" + "=" * 40)
    print("          TICKETING SYSTEM")
    print("=" * 40)
    print("[1] Add Ticket")
    print("[2] View All Tickets")
    print("[3] Search Ticket")
    print("[4] Update Ticket")
    print("[5] Delete Ticket")
    print("[0] Exit")
    print("-" * 40)

def main():
    create_table()  # Make sure the table exists

    while True:
        print_menu()
        choice = input("Select an option: ")

        if choice == "1":
            print("\n--- Add Ticket ---")
            title = input("Title: ")
            description = input("Description: ")
            add_ticket(title, description)
            print("Ticket added successfully.")

        elif choice == "2":
            print("\n--- All Tickets ---")
            tickets = get_all_tickets()
            if tickets:
                for t in tickets:
                    print(f"ID: {t[0]} | Title: {t[1]} | Status: {t[3]}")
            else:
                print("No tickets found.")

        elif choice == "3":
            print("\n--- Search Ticket ---")
            tid = input("Enter Ticket ID: ")
            ticket = search_ticket(tid)
            if ticket:
                print(f"\nID: {ticket[0]}")
                print(f"Title: {ticket[1]}")
                print(f"Description: {ticket[2]}")
                print(f"Status: {ticket[3]}")
            else:
                print("Ticket not found.")

        elif choice == "4":
            print("\n--- Update Ticket ---")
            tid = input("Ticket ID: ")

            existing = search_ticket(tid)
            if not existing:
                print("Ticket not found.")
                continue

            print("Leave a field blank to keep existing value.")

            new_title = input(f"New Title ({existing[1]}): ") or existing[1]
            new_desc = input(f"New Description ({existing[2]}): ") or existing[2]
            new_status = input(f"New Status ({existing[3]}): ") or existing[3]

            update_ticket(tid, new_title, new_desc, new_status)
            print("Ticket updated successfully.")

        elif choice == "5":
            print("\n--- Delete Ticket ---")
            tid = input("Ticket ID: ")
            ticket = search_ticket(tid)
            if not ticket:
                print("Ticket not found.")
                continue

            delete_ticket(tid)
            print("Ticket deleted successfully.")

        elif choice == "0":
            print("Goodbye!")
            sys.exit()

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
