#!/usr/bin/python3
"""
lists all states with a name starting with N(upper N)
from the database hbtn_0e_0_usa

"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    # Create a cursor object
    cursor = db.cursor()
    # Execute the query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch all the rows
    rows = cursor.fetchall()
    # Print the results
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    # Close the cursor and database connection
    cursor.close()
    db.close()
