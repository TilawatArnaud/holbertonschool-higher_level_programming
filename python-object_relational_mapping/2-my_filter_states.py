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
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Get the state name to search for
    state_name = sys.argv[4]

    # Create a cursor object
    cur = db.cursor()

    # Create SQL query using format()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(
        state_name
    )
    # Execute the query
    cur.execute(query)

    # Fetch all the rows
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
