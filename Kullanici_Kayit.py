import sqlite3
vt=sqlite3.connect("pizza.db")
cursor=vt.cursor()


def GetCity():
    komut="Select ILADI from Iller"
    cursor.execute(komut)
    Citys=cursor.fetchall()
    return Citys

cityId=0
districtId=0

def callback(eventObject):
    komut = "Select ID from Iller where ILADI='"+cbxcity.get()+"'"
    cursor.execute(komut)
    Id=cursor.fetchone()
    global cityId
    cityId=int(Id[0])
    komut1="Select ILCEADI from Ilceler where ILID="+str(Id[0])
    cursor.execute(komut1)
    Districts=cursor.fetchall()
    cbxdistrict["values"]=Districts
    cbxdistrict.current(0)




 #def callbackDistrict(eventObject):
     #komut = "Select ID from Ilceler where ILCEADI='" + cbxdistrict.get() + "'"
     #cursor.execute(komut)
     #Id=cursor.fetchone()
     #print(Id)
     #print(Id[0])
     #global districtId
     #districtId = int(Id[0])
     #print(districtId)




from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

pencere = Tk()
pencere.geometry("480x360")
pencere.config(bg="Orange")
from Musteri import Musteri

def Kaydet():
    musteri = Musteri()
    adsoyad=isimgiris.get()
    if(len(musteri.GetUser(adsoyad))==0):
        komut = "Select ID from Ilceler where ILCEADI='" + cbxdistrict.get() + "'"
        cursor.execute(komut)
        Id = cursor.fetchone()
        global districtId
        districtId = int(Id[0])
        print(districtId)
        musteri.Password = parolagiris.get()
        musteri.AdSoyad = isimgiris.get()
        musteri.Il = cityId
        musteri.Ilce = districtId
        musteri.Adres = adresgiris.get("1.0",END)
        musteri.SaveUser(musteri)
        messagebox.showinfo("Kayıt", "Kayıt Oluşturuldu.")
        pencere.destroy()
        import Kullanici_Girisi
        Kullanici_Girisi.pencere.mainloop()
    else:
        messagebox.showerror("HATA","Kayıt Oluşturulamadı.")





isim  = Label(pencere,text = "Name Surename: ",font=("Consolas",12))
isim.grid(row=0, column=0, sticky="W", pady=7)
isim.config(bg="Orange")
isimgiris = Entry(pencere, width=47, bd=3)
isimgiris.grid(row=0, column=1, pady=7, sticky="W")

parola = Label(pencere, text="Password: ", font=("Consolas",12))
parolagiris = Entry(pencere, width=47, show="*", bd=3)
parola.config(bg="Orange")
parola.grid(row=1, column=0, sticky="W", pady=7)
parolagiris.grid(row=1, column=1, pady=7, sticky="W")


city = Label(pencere, text="City: ", font=("Consolas",12))
city.grid(row=2, column=0, sticky="W", pady=7)
city.config(bg="Orange")
liste = GetCity()
cbxcity = Combobox(pencere, values=liste, width=44)
cbxcity.bind("<<ComboboxSelected>>", callback)
cbxcity.grid(row=2, column=1, pady=7, sticky="W")

district = Label(pencere, text="District: ", font=("Consolas",12))
district.grid(row=3, column=0, sticky="W", pady=7)
district.config(bg="Orange")
cbxdistrict = Combobox(pencere, values="", width=44)
cbxdistrict.grid(row=3, column=1, pady=7, sticky="W")

adres = Label(pencere, text="Adress :", font=("Consolas",12))
adresgiris = Text(pencere, font=("Consolas", 12), height=4, width=32)
adres.config(bg="Orange")
adres.grid(row=4, column=0, pady=7, sticky="W")
adresgiris.grid(row=4, column=1, pady=7, sticky="W")

giris = Button(pencere, text="Enter", command=Kaydet, width="17", bd=3)
giris.grid(row=6, column=1)
giris.config(bg="Orange")

pencere.mainloop()