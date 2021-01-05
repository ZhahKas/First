import sqlite3
vt = sqlite3.connect("pizza.db")
cursor = vt.cursor()

class Musteri:
    MusteriNo = 0
    def __init__(self):
        self.NameSurename = ""
        self.Password = ""
        self.Il = 0
        self.Ilce = 0
        self.Adres = ""

    def GetUser(self, adsoyad):
        vt = sqlite3.connect("pizza.db")
        cursor = vt.cursor()
        komut="Select AD_SOYAD from Musteriler where AD_SOYAD='"+adsoyad+"'"
        cursor.execute(komut)
        liste = cursor.fetchall()
        print(len(liste))
        vt.close()
        return liste

    def SaveUser(self, musteri):
        vt = sqlite3.connect("pizza.db")
        cursor = vt.cursor()
        try:
            komut="INSERT INTO Musteriler (AD_SOYAD,PASSWORD,IL,ILCE,ADRES) values (?,?,?,?,?);"
            cursor.execute(komut, (musteri.AdSoyad, musteri.Password, musteri.Il, musteri.Ilce, musteri.Adres))
            vt.commit()
            print("Sign Up Successful")
        except:
            print("Sign Up Failed!!!")
        vt.close()

    def LoginUser(self, adsoyad, password):
        vt = sqlite3.connect("pizza.db")
        cursor = vt.cursor()
        try:
            komut="Select * from Musteriler where AD_SOYAD='"+adsoyad+"' and PASSWORD='"+password+"'"
            cursor.execute(komut)
            liste=cursor.fetchone()
            musteri = Musteri()
            musteri.MusteriNo=liste[0]
            musteri.AdSoyad=liste[1]
            musteri.Password=liste[2]
            musteri.Il=liste[3]
            musteri.Ilce=liste[4]
            musteri.Adres=liste[5]
            return musteri
        except:
            return -1


