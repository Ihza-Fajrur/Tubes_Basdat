import mysql.connector
import string
import random
import os
import Beli_Tiket
import Lihat_Tiket
import Ajukan_Keluhan
import Lihat_Keluhan

clear = lambda: os.system('cls')
pause = lambda: os.system('pause')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="penjualan_tiket_pesawat"
)

mycursor = mydb.cursor()

def Menu():
    loop = True
    while loop:
        try:
            Option = int(input("Pilih Menu di Bawah\n 1.Beli Tiket | 2.Lihat Tiket | 3.Ajukan Keluhan | 4.Lihat Tanggapan Keluhan\n> "))
            if Option == 1:
                loop = False
                clear()
                Beli_Tiket.Main()
            elif Option == 2:
                loop = False
                clear()
                Lihat_Tiket.Main()
            elif Option == 3:
                loop = False
                clear()
                Ajukan_Keluhan.Main()
            elif Option == 4:
                loop = False
                clear()
                Lihat_Keluhan.Main()
            else:
                print("Inputan salah!")
        except ValueError:
            print("Harap masukkan integer")

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
            Menu()
        else:
            print("Username atau Password Salah!")

def Sign_Up():
    loop = True
    while loop:
        print("Sign Up")
        print("Harap inputkan data-data dibawah ini")
        Username = str(input("\tUsername\t: "))
        Password = str(input("\tPassword\t: "))
        Kontak   = str(input("\tNo Telepon\t: "))
        mycursor.execute("select username from pembeli where username = '"+Username+"'")
        result = mycursor.fetchall()
        if (not Username) or (not Password) or (not Kontak):
            print("Silahkan isi semua data yang dibutuhkan!")
            pause()
            clear()
        elif result:
            print("Username telah ada!")
            pause()
            clear()
        else:
            perintah = f'insert into pembeli values (\'{Kontak}\',\'{Username}\',\'{Password}\')'
            mycursor.execute(perintah)
            mydb.commit()
            loop = False
            print("Selamat akun Anda telah dibuat!, Anda akan diarahkan ke halaman Sign In")
            pause()
            Login()


def Main():
    loop = True
    while loop:
        try:
            Option = int(input("Pilih Menu di Bawah\n 1.Sign In | 2.Sign Up\n> "))
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
