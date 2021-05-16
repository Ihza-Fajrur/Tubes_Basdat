import SQLnya


alamat = 'ruangan'
PJ_ruangan = ['Suherman','Sumijan','Arnida','Dianto','Supardi']
for i in range (1,5):
    for j in range (1,21):
        a=i*100+j
        ruang = f'F{a:03}'
        nilai = (ruang,PJ_ruangan[i])
        SQLnya.masukin(alamat,nilai)
