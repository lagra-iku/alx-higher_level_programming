#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         charset="utf8")
    c = db.cursor()
    search = sys.argv[4]
    c.execute("SELECT cities.name FROM cities\
                JOIN states on cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (search,))
    table = c.fetchall()
    city_names = [row[0] for row in table]
    result = ", ".join(city_names)
    print(result)
    c.close()
    db.close()
