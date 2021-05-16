# # import mysql.connector
# #
# # mydb = mysql.connector.connect(
# #     host="localhost",
# #     user="root"
# # )
# #
# # print(mydb)
# #
# # mycursor = mydb.cursor()
# # perintah = "show databases"
# #
# # # while perintah:
# # #     mycursor.execute(perintah)
# # #     for db in mycursor:
# # #         print(db)
# # #     perintah = input()
# # no_tik = input("Nomor Tiket : \t")
# # kod_bok= input("Kode Bokking: \t")
# # mycursor.execute('use penjualan_tiket;')
# # perintah = f'insert into tiket values (\'{no_tik}\',\'{kod_bok}\')'
# # mycursor.execute(perintah)
# # mycursor.execute('select * from tiket;')
# # for db in mycursor:
# #         print(db)
# #
# # #
# # # import random
# # # x=['A','B','C','D',1,2,3,4,5,6,7,8,9]
# # # n=random.choice(x)
# # # print(n)
# # # n=[]
# # # for i in range(4):
# # #     n.append(random.choice(x))
# # # print(n)
#
# import mysql.connector
# import string
# import random
#
# # def rand_gen()
# #   def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
# #     return ''.join(random.choice(chars) for _ in range(size))
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root"
# )
#
# mycursor = mydb.cursor()
# order = "use penjualan_tiket;"
# mycursor.execute(order)
# order = "desc pembeli;"
# mycursor.execute(order)
#
# for db in mycursor:
#         print(db)
#
#
# # n = str(random.randint(121000,125000))
# # random.ranchar()
# # print(n)
#
# print("MENU\n\t1. Pembelian Tiket\n\t2. Keluhan")
# Menu_opt = int(input())
# if Menu_opt == 1:
#   print("Harap inputkan data-data dibawah ini")
#   temp_1 = input("KTP:\t")
#   temp_2 = input("Nama:\t")
#   temp_3 = input("Kontak:\t")
#
#   order = f'insert into pembeli values (\'{temp_2}\',\'{temp_1}\',\'{temp_3}\')'
#   mycursor.execute(order)
# elif Menu_opt == 2:
#   print("Membuat Keluhan")
#
# mycursor.execute(f'select *from pembeli;')
#
# for db in mycursor:
#         print(db)
# berhenti_nggak = "1"
# while berhenti_nggak:
#     berhenti_nggak = input()

import fpdf
import webbrowser

data=[("aud",'bvjbvev','vjvbev'),2,3,4,5,6]

pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)
Gedung = "E"
pdf.write(5,"Daftar Barang di Gedung "+Gedung)
pdf.ln()
for i in data:
    pdf.write(5,str(i))
    pdf.ln()
pdf.output("D:\Redoqx\ testings.pdf")
path = r'file://D:\Redoqx\ testings.pdf'
webbrowser.open_new(path)
