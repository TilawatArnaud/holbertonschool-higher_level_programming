#!/usr/bin/python3
"""
Lists all cities with their corresponding states from the database hbtn_0e_4_usa.
The results are displayed as (city_id, city_name, state_name)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor object
    cur = db.cursor()

    # Execute SQL query to fetch cities with their states
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cur.execute(query)

    # Fetch and print all rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
