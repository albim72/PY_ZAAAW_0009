import mysql.connector

db = mysql.connector.connect(user="root", password="abc123",host="127.0.0.1",port=3306, database="dbspecjalna")

cursorObject = db.cursor()

query = "SELECT firstname,nrstudenta FROM student;"

cursorObject.execute(query)
wynik = cursorObject.fetchall()
print(type(wynik))
for x,y in wynik:
    print(f'imię: {x}, nr studenta: {y}')

print("_"*45)

query2 = "SELECT * FROM student where nrstudenta>=100000"
cursorObject.execute(query2)
wynik2 = cursorObject.fetchall()

for x,y,z in wynik2:
    print(f'imię: {x},nazwisko: {y} nr studenta: {z}')

db.close()
