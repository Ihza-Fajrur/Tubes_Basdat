import mysql.connector
import string
import random
import os

clear = lambda: os.system('cls')
pause = lambda: os.system('pause')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="penjualan_tiket_pesawat"
)

mycursor = mydb.cursor()


def Login():
    loop = True
    while loop:
        print("Sign In")
        print("Harap inputkan data-data dibawah ini")
        Username = str(input("\tUsername\t: "))
        Password = str(input("\tPassword\t: "))
        if not (Username and Password):
            print("Username dan Password tidak dapat dikosongkan")
        mycursor.execute("Select password from pembeli where Username  = '" + Username + "\'")
        result = mycursor.fetchall()
        if not result:
            print("Username atau Password Salah!")
        result = (result[0])[0]
        if result == Password:
            loop = False
            print("Anda Berhasil Login!")
            pause()
            clear()
            #pergi ke menu()
        else:
            print("Username atau Password Salah!")

def Sign_Up():
    pass

def Main():
    loop = True
    while loop:
        try:
            Option = int(input("Pilih Menu di Bawah\n 1.Sign In | 2.Sign Up\n>"))
            if Option == 1:
                loop = False
                clear()
                Login()
            elif Option == 2:
                loop = False
                clear()
                Sign_Up()
            else:
                print("Inputan salah!")
        except ValueError:
            print("Harap masukkan integer")

Main()

