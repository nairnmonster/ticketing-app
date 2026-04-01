import sqlite3
from app.database import add_ticket, get_all_tickets, create_table

def test_add_ticket_creates_entry():
    create_table()
    add_ticket("Test Ticket", "Test Description")
    tickets = get_all_tickets()

    assert len(tickets) >= 1
    assert tickets[-1][1] == "Test Ticket"
    assert tickets[-1][2] == "Test Description"