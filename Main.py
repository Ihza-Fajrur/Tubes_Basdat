import mysql.connector
import string
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="penjualan_tiket_pesawat"
)

mycursor = mydb.cursor()


print("Login")
print("Harap inputkan data-data dibawah ini")
temp_1 = str(input("\tUsername\t: "))
temp_2 = str(input("\tPassword\t: "))


  