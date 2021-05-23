import os
import mysql.connector
import random
from prettytable import PrettyTable
import subprocess

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

def Cancel_Tiket():
    print("Pembatalan Tiket")
    temp_1 = str(input("Masukkan nomor tiket yang ingin di hapus\n>"))
    order = f'select no_tiket from tiket where no_tiket  = \'{temp_1}\''
    mycursor.execute(order)
    result = mycursor.fetchall()
    if result:
        order = f'DELETE FROM tiket WHERE tiket.no_tiket = \'{temp_1}\''
        mycursor.execute(order)
        mydb.commit()
        clear()
        print("Pembatalan tiket berhasil!\n")
    else:
        print("Nomor tiket tidak ditemukan!")
        pause()
        clear()
        Cancel_Tiket()

def List_tiket(User,Admin):
    print("Tiket "+User.Username+" : ")
    order = f'select penjualan_tiket.username,tiket.no_tiket,tiket.no_booking,tiket.asal,tiket.tujuan,tiket.tgl_keberangkatan,pembeli.kontak '
    order = order + f'from tiket LEFT JOIN penjualan_tiket ON tiket.no_penjualan = penjualan_tiket.no_penjualan '
    order = order + f'LEFT JOIN pembeli ON penjualan_tiket.Username = pembeli.Username '
    order = order + f'where `penjualan_tiket`.`Username` = \'{User.Username}\''
    mycursor.execute(order)
    result = mycursor.fetchall()
    x = PrettyTable(['username','no_tiket','no_booking','asal','tujuan','tgl_keberangkatan','kontak'])
    for j in result:
        x.add_row(j)
    print(x)

    try:
        option =  int(input("Apakah anda ingin membatalkan tiket?\n1.Ya | 2.Tidak\n>"))
        if option == 1:
            Cancel_Tiket()
        elif option == 2:
            pass
        else:
            print("Inputan Salah!")
            pause()
            clear()
            List_tiket(User,Admin)
    except ValueError:
        print("Harap masukkan integer!")
        pause()
        clear()
        List_tiket(User,Admin)

    print("\nAnda akan diarahkan ke Menu Utama")
    pause()
    clear()
    KeMenuUtama(User.Username,Admin)

def KeMenuUtama(Username,Admin):
    from Main import DariLuar
    DariLuar(Username,Admin)

def Main(Username,Admin):
    User = Current_User(Username)
    List_tiket(User,Admin)

if __name__ == "__main__":
    clear()
    Main("Ihza",0)
