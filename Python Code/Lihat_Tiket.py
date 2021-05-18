import os
import mysql.connector
import random
from prettytable import PrettyTable

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

def List_tiket(User):
    order = f' select no_tiket,no_booking,asal,tujuan,tgl_keberangkatan,harga from penjualan_tiket natural join tiket where username = \'{User.Username}\''
    mycursor.execute(order)
    result = mycursor.fetchall()

    x = PrettyTable(["No. Tiket", "No. Booking", "Asal", "Tujuan","Tanggal Keberangkatan","Harga"])
    for j in result:
        x.add_row(j)
    print(x)
    print("\nAnda akan diarahkan ke Menu Utama")
    pause()
    clear()
    KeMenuUtama(User.Username)

def KeMenuUtama(Username):
    from Main import DariLuar
    DariLuar(Username)

def Main(Username):
    User = Current_User(Username)
    List_tiket(User)

if __name__ == "__main__":
    clear()
    Main("Ihza")
