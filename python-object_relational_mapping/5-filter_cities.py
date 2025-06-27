#!/usr/bin/python3
"""
Script that lists all cities of a specific state from the database hbtn_0e_4_usa.
The script is safe from MySQL injections.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Get the state name from command line argument
    state_name = sys.argv[4]

    # Create cursor object
    cur = db.cursor()

    # Execute SQL query with parameterized input to prevent SQL injection
    query = """
    SELECT cities.name 
    FROM cities 
    JOIN states ON cities.state_id = states.id 
    WHERE states.name = %s 
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    # Fetch all rows and extract city names
    cities = [row[0] for row in cur.fetchall()]
    
    # Print cities separated by commas
    print(", ".join(cities))

    # Close cursor and database connection
    cur.close()
    db.close()
