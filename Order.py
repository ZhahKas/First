import sqlite3
vt=sqlite3.connect("pizza.db")
cursor=vt.cursor()

class Siparis:
    def __init__(self):
        self.MusteriNo=0
        self.Ebat=""
        self.Pizza=""
        self.Kenar=""
        self.Malzemeler=""
        self.Adet=0
        self.Tutar=0

    def SiparisAl(self,siparis):
        vt = sqlite3.connect("pizza.db")
        cursor = vt.cursor()
        komut="Insert into Siparisler (MUSTERI_NO,EBAT,PIZZA,KENAR,MALZEMELER,ADET,TUTAR) values (?,?,?,?,?,?,?)"
        cursor.execute(komut,(siparis.MusteriNo,siparis.Ebat,siparis.Pizza,siparis.Kenar,siparis.Malzemeler,siparis.Adet,siparis.Tutar))
        vt.commit()
        vt.close()

    @staticmethod
    def GetSiparis():
        vt = sqlite3.connect("pizza.db")
        cursor = vt.cursor()
        komut = """Select Musteriler.AD_SOYAD,EBAT,PIZZA,KENAR,MALZEMELER,ADET,TUTAR,Iller.ILADI,Ilceler.ILCEADI,Musteriler.ADRES from Siparisler 
        INNER JOIN Musteriler on Musteriler.ID=Siparisler.MUSTERI_NO
        INNER JOIN Iller ON Iller.ID=Musteriler.IL
        INNER JOIN Ilceler ON Ilceler.ID=Musteriler.ILCE"""
        cursor.execute(komut)
        liste = cursor.fetchall()
        vt.close()
        return liste



