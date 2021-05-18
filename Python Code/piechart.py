import re
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

def jumlah_bulan(User,Admin):
    bulan = []
    jumlah = []
    mycursor.execute("select tgl_keberangkatan from tiket where month(tgl_keberangkatan)=1")
    result = mycursor.fetchall()
    if result:
        jumlah.append(len(result))
        bulan.append("Januari")
    mycursor.execute("select tgl_keberangkatan from tiket where month(tgl_keberangkatan)=2")
    result = mycursor.fetchall()
    if result:
        jumlah.append(len(result))
        bulan.append("Februari")
    mycursor.execute("select tgl_keberangkatan from tiket where month(tgl_keberangkatan)=3")
    result = mycursor.fetchall()
    if result:
        jumlah.append(len(result))
        bulan.append("Maret")
    mycursor.execute("select tgl_keberangkatan from tiket where month(tgl_keberangkatan)=4")
    result = mycursor.fetchall()
    if result:
        jumlah.append(len(result))
        bulan.append("April")
    mycursor.execute("select tgl_keberangkatan from tiket where month(tgl_keberangkatan)=5")
    result = mycursor.fetchall()
    if result:
        jumlah.append(len(result))
        bulan.append("Mei")
    mycursor.execute("select tgl_keberangkatan from tiket where month(tgl_keberangkatan)=6")
    result = mycursor.fetchall()
    if result:
        jumlah.append(len(result))
        bulan.append("Juni")
    mycursor.execute("select tgl_keberangkatan from tiket where month(tgl_keberangkatan)=7")
    result = mycursor.fetchall()
    if result:
        jumlah.append(len(result))
        bulan.append("Juli")
    mycursor.execute("select tgl_keberangkatan from tiket where month(tgl_keberangkatan)=8")
    result = mycursor.fetchall()
    if result:
        jumlah.append(len(result))
        bulan.append("Agustus")
    mycursor.execute("select tgl_keberangkatan from tiket where month(tgl_keberangkatan)=9")
    result = mycursor.fetchall()
    if result:
        jumlah.append(len(result))
        bulan.append("September")
    mycursor.execute("select tgl_keberangkatan from tiket where month(tgl_keberangkatan)=10")
    result = mycursor.fetchall()
    if result:
        jumlah.append(len(result))
        bulan.append("Oktober")
    mycursor.execute("select tgl_keberangkatan from tiket where month(tgl_keberangkatan)=11")
    result = mycursor.fetchall()
    if result:
        jumlah.append(len(result))
        bulan.append("November")
    mycursor.execute("select tgl_keberangkatan from tiket where month(tgl_keberangkatan)=12")
    result = mycursor.fetchall()
    if result:
        jumlah.append(len(result))
        bulan.append("Desember")
    plt.pie(jumlah,labels = bulan,autopct='%1.2f%%')

    plt.title('Jumlah Pembelian Tiket Pada Bulan Tertentu', size=15)

    plt.show()

    print("\nAnda akan diarahkan ke Menu Utama")
    pause()
    clear()
    KeMenuUtama(User.Username,Admin)

def Main(Username,Admin):
    User = Current_User(Username)
    jumlah_bulan(User,Admin)

def KeMenuUtama(Username,Admin):
    from Main import DariLuar
    DariLuar(Username,Admin)