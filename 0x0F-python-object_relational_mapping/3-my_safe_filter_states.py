#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
Make it safe from MySQL injections!
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         charset="utf8")
    c = db.cursor()
    search = sys.argv[4]
    c.execute("SELECT * FROM states WHERE BINARY name = %s\
              ORDER BY id ASC", (search,))
    table = c.fetchall()
    for row in table:
        print(row)
    c.close()
    db.close()
