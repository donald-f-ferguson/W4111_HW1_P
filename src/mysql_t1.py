import pymysql
import json

default_cnx = pymysql.connect(host='localhost',
                             user='dbuser',
                             password='dbuserdbuser',
                             db='w4111',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


cur = default_cnx.cursor()
res = cur.execute("select * from countries limit 10;")
data = cur.fetchall()

print("Data = ")
print(json.dumps(data, indent=2))

