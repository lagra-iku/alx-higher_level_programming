#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    if (len(sys.argv) == 4):
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3],
                             charset="utf8")
        c = db.cursor()
        c.execute("SELECT * FROM states ORDER BY id ASC")
        table = c.fetchall()
        for row in table:
            print(row)
        c.close()
        db.close()
