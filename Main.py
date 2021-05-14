import mysql.connector
import string
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="penjualan_tiket_pesawat"
)

mycursor = mydb.cursor()


def login():
    print("Login")
    print("Harap inputkan data-data dibawah ini")
    Username = str(input("\tUsername\t: "))
    Password = str(input("\tPassword\t: "))
    if not (Username and Password):
        print("Username dan Password tidak dapat dikosongkan")
        return 0
    mycursor.execute("Select password from pembeli where Username  = '" + Username + "\'")
    result = mycursor.fetchall()
    if not result:
        print("Username tidak ditemukan, silakahkan sign up terlebih dahulu!")
        return 0
    result = (result[0])[0]
    if result == Password:
        print("Anda Berhasil Login!")
        #pergi ke menu()

    else:
        print("Username atau Password Salah!")
