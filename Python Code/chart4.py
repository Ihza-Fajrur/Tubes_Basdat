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

def jumlah_tujuan(User,Admin):
    jurusan = ['Medan', 'Padang', 'Lampung', 'Jakarta', 'Pontianak', 'Yogyakarta','Palangkaraya','Bali','Palu']
    jumlah = []
    mycursor.execute("select tujuan from tiket where tujuan = \'Medan\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select tujuan from tiket where tujuan = \'Padang\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select tujuan from tiket where tujuan = \'Lampung\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select tujuan from tiket where tujuan = \'Jakarta\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select tujuan from tiket where tujuan = \'Pontianak\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select tujuan from tiket where tujuan = \'Yogyakarta\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select tujuan from tiket where tujuan = \'Palangkaraya\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select tujuan from tiket where tujuan = \'Bali\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))
    mycursor.execute("select tujuan from tiket where tujuan = \'Palu\'")
    result = mycursor.fetchall()
    jumlah.append(len(result))


    plt.bar(jurusan, jumlah, color=['#7CFC00'])

    plt.title('Jumlah Pembelian Tiket Tujuan Tertentu', size=15)
    plt.ylabel('Jumlah Pembelian', size=15)
    plt.xlabel('Tujuan', size=15)
    plt.xticks(size=10)
    plt.yticks(size=10)

    plt.show()

    print("\nAnda akan diarahkan ke Menu Utama")
    pause()
    clear()
    KeMenuUtama(User.Username,Admin)

def Main(Username,Admin):
    User = Current_User(Username)
    jumlah_tujuan(User,Admin)

def KeMenuUtama(Username,Admin):
    from Main import DariLuar
    DariLuar(Username,Admin)