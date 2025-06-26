#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create cursor object using the cursor() method
    cursor = db.cursor()

    # SQL query to fetch all states
    query = "SELECT * FROM states ORDER BY id ASC"

    try:
        # Execute the SQL query
        cursor.execute(query)

        # Fetch all rows from the last executed statement
        results = cursor.fetchall()

        # Print each row
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the database connection
        db.close()
