import os
import mysql.connector
import random

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

def Import_CS_List():
    CS_List = []
    i=0
    mycursor.execute("Select id_cs from cs")
    result = mycursor.fetchall()
    for x in result:
        CS_List.append(x[i])
    return random.choice(CS_List)

def Isi_Keluhan(User,Admin):
    loop_1 = True
    while loop_1:
        # temp_1 = str(random.randint(101000,101999))
        mycursor.execute("Select no_tiket_keluhan from keluhan")
        result = mycursor.fetchall()
        temp_1 = random.choice([i for i in range(101000,101999) if i not in result])
        temp_2 = input("Harap Masukkan Pesan Keluhan:\n>")
        temp_3 = Import_CS_List()
        order = f'insert into keluhan (no_tiket_keluhan,Username,isi_keluhan,ID_CS) values (\'{temp_1}\',\'{User.Username}\',\'{temp_2}\',\'{temp_3}\')'
        mycursor.execute(order)
        mydb.commit()
        loop_2 = True
        while loop_2:
            try:
                clear()
                option = int(input("Apakah anda ingin mengisi keluhan lagi?\n1.Ya | 2.Tidak\n>"))
                if option == 1:
                    loop_2 = False
                    clear()
                elif option == 2:
                    loop_2 = False
                    loop_1 = False
                else:
                    print("Inputan salah!")
            except ValueError:
                print("Harap masukkan integer")
    print("\nAnda akan diarahkan ke Menu Utama")
    pause()
    clear()
    KeMenuUtama(User.Username,Admin)

def Main(Username,Admin):
    User = Current_User(Username)
    Isi_Keluhan(User,Admin)

def KeMenuUtama(Username,Admin):
    from Main import DariLuar
    DariLuar(Username,Admin)

if __name__ == "__main__":
    clear()
    Main("Ihza")
