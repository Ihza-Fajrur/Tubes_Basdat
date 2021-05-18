import mysql.connector
import os
import Beli_Tiket
import Lihat_Tiket
import Ajukan_Keluhan
import Lihat_Keluhan

#Inisilasi
clear = lambda: os.system('cls')
pause = lambda: os.system('pause')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="penjualan_tiket_pesawat"
)

mycursor = mydb.cursor()

class Current_User:
    def __init__(self,Username):
        self.Username = Username

    def Import_Username(self):
        return self.Username

def Menu(User,Admin):
    loop = True
    while loop:
        try:
            #menu
            if !(Admin):
                Option = int(input("Pilih Menu di Bawah\n 1.Beli Tiket | 2.Lihat Tiket | 3.Ajukan Keluhan | 4.Lihat Tanggapan Keluhan | 5.Log Out\n> "))
            else :
                Option = int(input("Pilih Menu di Bawah\n 1.Beli Tiket | 2.Lihat Tiket | 3.Ajukan Keluhan | 4.Lihat Tanggapan Keluhan | 5.Log Out | 6. Tampilkan Graph\n> "))
            #pilih menu
            if Option == 1:
                loop = False
                clear()
                Beli_Tiket.Main(User.Import_Username())
            elif Option == 2:
                loop = False
                clear()
                Lihat_Tiket.Main(User.Import_Username())
            elif Option == 3:
                loop = False
                clear()
                Ajukan_Keluhan.Main(User.Import_Username())
            elif Option == 4:
                loop = False
                clear()
                Lihat_Keluhan.Main(User.Import_Username())
            elif Option == 5:
                loop = False
                print("Terima Kasih")
                pause()
                clear()
                Main()
            elif admin:
                if Option == 6:
                    loop = False
                    Tampilkan_Graph()
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
        admin = 0
        mycursor.execute("Select password from pembeli where Username  = '" + Username + "\'")
        result = mycursor.fetchall()
        if not result:
            mycursor.execute("Select Id_petugas from petugas where Nama_Petugas  = '" + Username + "\'")
            result = mycursor.fetchall()
            admin = 1
        result = (result[0])[0]
        if result == Password:
            loop = False
            print("Anda Berhasil Login!")
            User = Current_User(Username)
            pause()
            clear()
            Menu(User,admin)
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
            clear()
            Login()


def Main():
    loop = True
    while loop:
        try:
            Option = int(input("Pilih Menu di Bawah\n 1.Sign In | 2.Sign Up | 3.Tutup Aplikasi\n> "))
            if Option == 1:
                loop = False
                clear()
                Login()
            elif Option == 2:
                loop = False
                clear()
                Sign_Up()
            elif Option == 3:
                loop = False
                print("Sampai jumpa!")
                exit()
            else:
                print("Inputan salah!")
        except ValueError:
            print("Harap masukkan integer")

def DariLuar(Username):
    User = Current_User(Username)
    clear()
    Menu(User)

if __name__ == "__main__":
    clear()
    Main()
