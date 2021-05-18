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


def List_Keluhan(User):
    clear()
    Keluhan = []
    No_tiket_Keluhan = []
    ID_CS = []
    Balasan = []
    order = f'select no_tiket_keluhan,Isi_keluhan,ID_CS,Balasan from keluhan where Username = \'{User.Username}\''
    mycursor.execute(order)
    result = mycursor.fetchall()
    for x in range(len(result)):
        No_tiket_Keluhan.append(result[x][0])
        Keluhan.append(result[x][1])
        ID_CS.append(result[x][2])
        if result[x][3] == "":
            Balasan.append("Keluhan anda belum dibalas, Keluhan anda akan dibalas dalam waktu 1x24 Jam")
        else:
            Balasan.append(result[x][3])
    print("List Keluhan Anda:")
    print("No Tiket Keluhan\t| Isi Keluhan\t| ID CS\t\t| Balasan")
    # a = PrettyTable(["No. Tiket", "No. Booking", "Asal", "Tujuan","Tanggal Keberangkatan","Harga"])
    for i in range(len(result)):
        print(No_tiket_Keluhan[i], "\t\t\t| ", Keluhan[i], "\t| ",ID_CS[i], "\t| ",Balasan[i])
    # for y in result:
    #     a.add_row(y)
    print("\nAnda akan diarahkan ke Menu Utama")
    pause()
    clear()
    KeMenuUtama(User.Username)

def KeMenuUtama(Username):
    from Main import DariLuar
    DariLuar(Username)

def Main(Username):
    User = Current_User(Username)
    List_Keluhan(User)

if __name__ == "__main__":
    clear()
    Main("Ihza")
