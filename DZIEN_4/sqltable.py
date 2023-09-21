import mysql.connector

db = mysql.connector.connect(user="root", password="abc123",host="127.0.0.1",port=3306, database="dbspecjalna")

cursorObject = db.cursor()
tabela_student = ("CREATE TABLE IF NOT EXISTS student(firstname varchar(100), "
                  "lastname varchar(100), nrstudenta int);")
cursorObject.execute(tabela_student)

ins_data = "INSERT INTO student(firstname,lastname,nrstudenta) values(%s,%s,%s);"
val_one = ("Jan","Kot",574857)

cursorObject.execute(ins_data,val_one)

val_multi = [
    ("Maria","Nowak",635454),
    ("Marek","Nowik",566564),
    ("Leon","Kos",635444),
    ("Paweł","Kol",63576),
    ("Roch","Kot",7675),
    ("Feliks","Kit",635756),
    ("Henio","Krak",98787),

]
cursorObject.executemany(ins_data,val_multi)

db.commit()

db.close()
