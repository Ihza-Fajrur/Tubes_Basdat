import mysql.connector
import random
import os

clear = lambda: os.system('cls')
pause = lambda: os.system('pause')
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="penjualan_tiket_pesawat"
)
mycursor = mydb.cursor()

#koordinat
kota = []
kota.append(['Medan',5,7])
kota.append(['Padang',4,4])
kota.append(['Lampung',8,1])
kota.append(['Jakarta',12,2])
kota.append(['Pontianak',13,6])
kota.append(['Yogyakarta',18,1])
kota.append(['Palangkaraya',21,6])
kota.append(['Bali',25,1])
kota.append(['Palu',24,6])

class Current_User:
    def __init__(self,Username):
        self.Username = Username

def Import_Ticketer_List():
    Ticketer_List = []
    mycursor.execute("Select id_ticketer from ticketer")
    result = mycursor.fetchall()
    for x in result:
        Ticketer_List.append(x[0])
    return random.choice(Ticketer_List)

def Beli_Tiket(User,Admin):
    destinasi = True
    while destinasi:
        asal = pilihKota("asal")
        tujuan = pilihKota("tujuan")
        print("Masukan Waktu Keberangkatan Anda")
        tahun = input("\nTahun Keberangkatan Anda  (0000-9999): ")
        bulan = input("\nBulan Keberangkatan Anda  (1-12): ")
        tgl = input("\nTanggal Keberangkatan Anda (01-31): ")
        if len(tahun)==4:
            tahun=str(tahun)
        elif len(tahun)!=4:
            print("Inputan salah tahun salah")
            pause()
            clear()
            Beli_Tiket(User,Admin)
        if len(bulan)==1:
            bulan='0'+str(bulan)
        if len(tgl)==1:
            tgl = '0'+str(tgl)
        tgl = tahun+'-'+bulan+'-'+tgl
        harga = hitungHarga(asal,tujuan)
        clear()
        print(f'Tiket perjalanan\nDari\t: {kota[asal][0]}\nMenuju\t: {kota[tujuan][0]}\nHarga\t: {harga}\nPada\t: {tgl}')
        loop_2 = True
        while loop_2:
            try:
                option = int(input("Apakah anda yakin dengan pesanan Anda?\n1.Ya | 2.Tidak\n>"))
                if option == 1:
                    destinasi = False
                    loop_2 = False
                    clear()
                elif option == 2:
                    loop_2 = False
                    Ngulang(User,Admin)
                    clear()
                else:
                    print("Inputan salah!")
            except ValueError:
                print("Harap masukkan angka!")
    #############################################
    penjualan = True
    while penjualan:
        lanjut = 1
        no_penjualan = 'JLA'+str(random.randint(1000000,9999999))
        id_ticketer  = Import_Ticketer_List()
        #Input Data Penjualan Tiket
        try:
            sql_insert_blob_query = """INSERT INTO penjualan_tiket
                          (no_penjualan, id_ticketer, Username) VALUES (%s,%s,%s)"""

            datanya = (no_penjualan,id_ticketer,User.Username)
            result = mycursor.execute(sql_insert_blob_query,datanya)
            mydb.commit()
        except mysql.connector.Error as error:
            print(error)
            pause()
            lanjut = 0
        if lanjut:
            penjualan=0
    #############################################
    tiket = True
    while tiket:
        lanjut = 1
        no_tiket  = 'Tkt'+str(random.randint(1000000,9999999))
        no_booking= 'BKG'+str(random.randint(1000000,9999999))

        try:
            sql_insert_blob_query = """INSERT INTO tiket
                           (no_tiket, no_booking, asal, tujuan, harga, no_penjualan, tgl_keberangkatan)VALUES (%s,%s,%s,%s,%s,%s,%s)"""

            datanya = (no_tiket,no_booking,kota[asal][0],kota[tujuan][0],harga,no_penjualan,tgl)
            result = mycursor.execute(sql_insert_blob_query,datanya)
            mydb.commit()
        except mysql.connector.Error as error:
            print(error)
            pause()
            lanjut = 0
        if lanjut:
            tiket = 0
    clear()
    print("Anda Berhasil Membeli Tiket!")
    pause()
    Ngulang(User,Admin)
    #############################################

def Ngulang(User,Admin):
    try:
        clear()
        option = int(input("Apakah anda ingin membeli tiket lagi?\n1.Ya | 2.Tidak\n>"))
        if option == 1:
            clear()
            Beli_Tiket(User,Admin)
        elif option == 2:
            pass
        else:
            print("Inputan salah!")
    except ValueError:
        print("Harap masukkan integer")
    print("\nAnda akan diarahkan ke Menu Utama")
    pause()
    clear()
    KeMenuUtama(User.Username,Admin)


def pilihKota(ke):
    pilih=1
    while pilih:
        print(f'Silahkan Pilih {ke} Destinasi Anda:')
        i=1
        for j in kota:
            destinasi = j[0]
            print(f'{i}. {destinasi}')
            i=i+1
        try:
            destinasi = int(input("> "))
            if destinasi<1 or destinasi>len(kota):
                print("Pilihan Anda tidak tersedia di sistem kami")
                pause()
                clear()
            else:
                pilih=0
        except ValueError:
            print("Harap masukkan angka!")
            clear()
        clear()
    return destinasi-1

def hitungHarga(A,B):
    Ax = kota[A][1]
    Ay = kota[A][2]
    Bx = kota[B][1]
    By = kota[B][2]
    X = Ax-Bx
    Y = Ay-By
    jarak = (X**2) + (Y**2)
    jarak = jarak**(1.0/2)
    jarak = jarak*117.7 #kaliin harga
    jarak = int(jarak) #penggenapan
    return jarak*1000 #harga sebenar

def Main(Username,Admin):
    User = Current_User(Username)
    Beli_Tiket(User,Admin)

def KeMenuUtama(Username,Admin):
    from Main import DariLuar
    DariLuar(Username,Admin)

if __name__ == "__main__":
    clear()
    Main("Ihza",0)
