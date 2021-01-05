import sqlite3
vt = sqlite3.connect("pizza.db")
cursor = vt.cursor()

komut = "CREATE TABLE Siparisler (ID INTEGER PRIMARY KEY AUTOINCREMENT, MUSTERI_NO INTEGER, EBAT NVARCHAR(20), PIZZA NVARCHAR(20), KENAR NVARCHAR(20), MALZEMELER NVARCHAR(250), ADET INTEGER, TUTAR INTEGER )"
cursor.execute(komut)

komut = "CREATE TABLE Musteriler (ID INTEGER PRIMARY KEY AUTOINCREMENT, AD_SOYAD NVARCHAR(50),PASSWORD NVARCHAR(10), IL INTEGER, IlCE INTEGER, ADRES NVARCHAR(200))"
cursor.execute(komut)



komut = "CREATE TABLE Iller (ID PRIMARY KEY, ILADI NVARCHAR(30))"
cursor.execute(komut)

for i in range(5):
     plaka=int(input("Plaka:"))
     il=input("İl Adı:")
     komut ="INSERT INTO Iller (ID,ILADI) values (?,?)"
     cursor.execute(komut,(plaka,il))
     vt.commit()

komut = "CREATE TABLE Ilceler (ID  INTEGER PRIMARY KEY AUTOINCREMENT, ILCEADI NVARCHAR(30), ILID INTEGER)"
cursor.execute(komut)

for i in range(5):
     ID=int(input("İl Plaka No:"))
     ilce=input("İlce Adı:")
     komut ="INSERT INTO Ilceler (ILCEADI,ILID) values (?,?)"
     cursor.execute(komut,(ilce,ID))
     vt.commit()



def GetUser():
     komut="Select * from Musteriler"
     cursor.execute(komut)
     Users=cursor.fetchall()
     print(Users)
     return Users
def SaveUser(musteri):
     Users = list()
     Users=GetUser()
     for user in Users:
         print(user)

SaveUser()
vt.close()