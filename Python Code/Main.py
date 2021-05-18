import mysql.connector
import os
import Beli_Tiket
import Lihat_Tiket
import Ajukan_Keluhan
import Lihat_Keluhan
import chart4
import linechart4
import piechart

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
            if not (Admin):
                Option = int(input("Pilih Menu di Bawah\n 1.Beli Tiket | 2.Lihat Tiket | 3.Ajukan Keluhan | 4.Lihat Tanggapan Keluhan | 5.Log Out\n> "))
            else :
                Option = int(input("Pilih Grafik data yang ingin ditampilkan\n\t1.Jumlah pembelian tiket tujuan tertentu\n\t2.Jumlah pembelian tiket asal tertentu\n\t3.Jumlah pembelian tiket pada bulan tertentu\n\t4.Log Out\n\t> "))
            #pilih menu
            if not Admin:
                if Option == 1:
                    loop = False
                    clear()
                    Beli_Tiket.Main(User.Import_Username(),Admin)
                elif Option == 2:
                    loop = False
                    clear()
                    Lihat_Tiket.Main(User.Import_Username(),Admin)
                elif Option == 3:
                    loop = False
                    clear()
                    Ajukan_Keluhan.Main(User.Import_Username(),Admin)
                elif Option == 4:
                    loop = False
                    clear()
                    Lihat_Keluhan.Main(User.Import_Username(),Admin)
                elif Option == 5:
                    loop = False
                    print("Terima Kasih")
                    pause()
                    clear()
                    Main()
                else:
                    print("Inputan salah!")
                    pause()
            elif Admin:
                if Option == 1:
                    loop = False
                    chart4.Main(User.Import_Username(),Admin)
                if Option == 2:
                    loop = False
                    linechart4.Main(User.Import_Username(),Admin)
                if Option == 3:
                    loop = False
                    piechart.Main(User.Import_Username(),Admin)
                elif Option == 4:
                    loop = False
                    print("Terima Kasih")
                    pause()
                    clear()
                    Main()
                else:
                    print("Inputan salah!")
                    clear()
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
        Admin = 0
        try:
            mycursor.execute("Select password from pembeli where Username  = '" + Username + "\'")
            result = mycursor.fetchall()
            if not result:
                mycursor.execute("Select Id_petugas from petugas where Nama_Petugas  = '" + Username + "\'")
                result = mycursor.fetchall()
                Admin = 1

            if result[0][0] == Password:
                loop = False
                print("Anda Berhasil Login!")
                User = Current_User(Username)
                pause()
                clear()
                Menu(User,Admin)
            else:
                print("Username atau Password Salah!")
                pause()
                clear()
        except IndexError:
            print("Username Salah!")
            pause()
            clear()

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

def DariLuar(Username,Admin):
    User = Current_User(Username)
    clear()
    Menu(User,Admin)

if __name__ == "__main__":
    clear()
    Main()
