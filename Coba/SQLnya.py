import mysql.connector
import fpdf

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="tubes_pbo"
)
mycursor = mydb.cursor()

def masukin(tabel,nilai):
    print('Masukkah?')
    perintah = "insert into %s values %s"
    nilai = str(nilai)
    nilai = (tabel,nilai)
    mycursor.execute(perintah%nilai)
    mydb.commit()


def masukanBerGambar(tabel,nilai_lain,gambar):
    pass
