#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    # Create cursor object using the cursor() method
    cursor = db.cursor()

    # SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the last executed statement
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the database connection and cursor
    cursor.close()
    db.close()
