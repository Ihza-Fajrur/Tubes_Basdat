import matplotlib.pyplot as plt
import os
import mysql.connector

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

def jumlah_asal(User,Admin):
    asal = ['Medan', 'Padang', 'Lampung', 'Jakarta', 'Pontianak', 'Yogyakarta','Palangkaraya','Bali','Palu']
    jumlah = []
    mycursor.execute("select asal from tiket where asal = \'Medan\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select asal from tiket where asal = \'Padang\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select asal from tiket where asal = \'Lampung\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select asal from tiket where asal = \'Jakarta\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select asal from tiket where asal = \'Pontianak\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select asal from tiket where asal = \'Yogyakarta\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select asal from tiket where asal = \'Palangkaraya\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select asal from tiket where asal = \'Bali\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select asal from tiket where asal = \'Palu\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))

    plt.plot(asal, jumlah)

    plt.title('Jumlah Pembelian Tiket Asal Tertentu', size=15)
    plt.ylabel('Jumlah pembelian', size=15)
    plt.xlabel('Asal', size=15)
    plt.plot(size=10)
    plt.plot(size=10)

    plt.show()

    print("\nAnda akan diarahkan ke Menu Utama")
    pause()
    clear()
    KeMenuUtama(User.Username,Admin)

def Main(Username,Admin):
    User = Current_User(Username)
    jumlah_asal(User,Admin)

def KeMenuUtama(Username,Admin):
    from Main import DariLuar
    DariLuar(Username,Admin)