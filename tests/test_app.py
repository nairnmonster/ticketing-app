import sys
import os

# Ensure project root is on PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import sqlite3
from app.database import add_ticket, get_all_tickets, create_table

def test_add_ticket_creates_entry():
    # Arrange
    create_table()  # ensure table exists
    add_ticket("Test Ticket", "Test Description")

    # Act
    tickets = get_all_tickets()

    # Assert
    assert len(tickets) >= 1
    assert tickets[-1][1] == "Test Ticket"
    assert tickets[-1][2] == "Test Description"