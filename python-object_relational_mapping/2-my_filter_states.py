#!/usr/bin/python3
"""Script that takes an argument and displays
   all matching states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],      # First argument: MySQL username
        passwd=sys.argv[2],    # Second argument: MySQL password
        db=sys.argv[3]         # Third argument: database name
    )

    # Get the state name to search for
    state_name = sys.argv[4]

    # Create a cursor object
    cur = db.cursor()

    # Build SQL query with parameterized input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with the parameter
    cur.execute(query, (state_name,))

    # Fetch all the rows
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
