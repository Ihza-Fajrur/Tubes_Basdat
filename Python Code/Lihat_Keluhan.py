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


def List_Keluhan(User,Admin):
    clear()
    Keluhan = []
    No_tiket_Keluhan = []
    ID_CS = []
    Balasan = []
    order = f'select no_tiket_keluhan,Isi_keluhan,nama_cs,Balasan from keluhan left join cs on keluhan.id_cs=cs.id_cs where Username = \'{User.Username}\''
    mycursor.execute(order)
    result = mycursor.fetchall()
    text = "Keluhan anda belum dibalas, Keluhan anda akan dibalas dalam 3x24 Jam"
    for x in range(len(result)):
        if result[x][3] == "":
            perintah = f'update keluhan set Balasan = \'{text}\' where keluhan.no_tiket_keluhan = \'{result[x][0]}\''
            mycursor.execute(perintah)
            mydb.commit()
    print("List Keluhan Anda:")
    a = PrettyTable(["No. Tiket Keluhan", "Isi Keluhan", "Nama CS","Balasan"])
    for y in result:
        a.add_row(y)
    print(a)
    print("\nAnda akan diarahkan ke Menu Utama")
    pause()
    clear()
    KeMenuUtama(User.Username,Admin)

def KeMenuUtama(Username,Admin):
    from Main import DariLuar
    DariLuar(Username,Admin)

def Main(Username,Admin):
    User = Current_User(Username)
    List_Keluhan(User,Admin)

if __name__ == "__main__":
    clear()
    Main("Ihza",0)
