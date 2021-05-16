import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root"
)

print(mydb)

mycursor = mydb.cursor()
perintah = "show databases"

while perintah:
    mycursor.execute(perintah)
    for db in mycursor:
        print(db)
    perintah = input()
mydb.commit()

masukkan = 1
while masukkan:
    perintah = "insert into %s values %s"
    alamat = "penjualan_tiket.pembeli"
    Nama = input("Nama\t: ")
    KTP = input("KTP\t: ")
    Nomor = input("Nomor\t: ")
    insert = (Nama,KTP,Nomor)
    insert = str(insert)
    insert = (alamat,insert)
    mycursor.execute(perintah%insert)
    masukkan = input("Lanjut?")

perintah = "select KTP from penjualan_tiket.pembeli where Nama = 'fjkb' "
mycursor.execute(perintah)
result = mycursor.fetchall()
if not result:
    print("Empty guys!")
print(result)
