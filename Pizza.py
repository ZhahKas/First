from Order import *
from Musteri import *

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox

root = tk.Tk()
root.geometry("900x480")
root.title("Pizza Otomasyonu")
root.config(bg="Orange")
operasyon = tk.StringVar()
toptut = tk.StringVar()
c1 = tk.IntVar()
c2 = tk.IntVar()
c3 = tk.IntVar()
c4 = tk.IntVar()
c5 = tk.IntVar()
c6 = tk.IntVar()
c7 = tk.IntVar()
c8 = tk.IntVar()
c9 = tk.IntVar()
c10 = tk.IntVar()
r = tk.IntVar()
toplamtutar = 0
mlzmbilgisi = str()


def PizzaBoyutu():
    if ebat.get() == "Big":
        veri = 50

    elif ebat.get() == "Normal":
        veri = 40

    elif ebat.get() == "Small":
        veri = 30

    return veri


def PizzaTuru(veri):
    if liste.curselection() == (0,):
        veri += 25

    elif liste.curselection() == (1,):
        veri += 20

    elif liste.curselection() == (2,):
        veri += 15

    elif liste.curselection() == (3,):
        veri += 10

    return veri


def KenarTuru(veri):
    veri += r.get()
    return veri


def Malzeme(veri):
    veri += c1.get() + c2.get() + c3.get() + c4.get() + c5.get() + c6.get() + c7.get() + c8.get() + c9.get() + c10.get()
    return veri


def ToplamHesap(veri):
    veri = veri * (int(spin.get()))
    return veri


def GenelHesaplama():
    global geneltoplam
    global malzemeli
    ilkucret = PizzaBoyutu()                # ebatına göre fiyat eklendi
    pizzaturufiyat = PizzaTuru(ilkucret)    # pizza türüne göre fiyat eklendi
    kenarfiyati = KenarTuru(pizzaturufiyat) # kenar türüne göre fiyat eklendi
    malzemeli = Malzeme(kenarfiyati)        # ekstra malzemelere göre fiyat eklendi
    geneltoplam = ToplamHesap(malzemeli)    # adete göre fiyat çarpıldı
    operasyon.set(str(geneltoplam) + " TL") #
    return geneltoplam


def Ekleme1():
    global toplamtutar
    toplamtutar = geneltoplam + toplamtutar

    if liste.curselection() == (0,):
        if r.get() == 8:
            for i in range(int(spin.get())):
                lis2.insert(0,
                            ebat.get() + " İnce Kenar Türk Pizza  " + "Ekstra Malzemeler:  " + mlzmbilgisi + "                                         " + str(
                                malzemeli) + " TL")
                toptut.set(toplamtutar)

        elif r.get() == 5:

            for i in range(int(spin.get())):
                lis2.insert(0,
                            ebat.get() + " Kalın Kenar Türk Pizza  " + "Ekstra Malzemeler:  " + mlzmbilgisi + "                                           " + str(
                                malzemeli) + " TL")
                toptut.set(toplamtutar)

    elif liste.curselection() == (1,):

        if r.get() == 8:

            for i in range(int(spin.get())):
                lis2.insert(0,
                            ebat.get() + " İnce Kenar İtalyan Pizza  " + "Ekstra Malzemeler:  " + mlzmbilgisi + "                                           " + str(
                                malzemeli) + " TL")
                toptut.set(toplamtutar)

        elif r.get() == 5:

            for i in range(int(spin.get())):
                lis2.insert(0,
                            ebat.get() + " Kalın Kenar İtalyan Pizza  " + "Ekstra Malzemeler:" + mlzmbilgisi + "                                           " + str(
                                malzemeli) + " TL")
                toptut.set(toplamtutar)

    elif liste.curselection() == (2,):

        if r.get() == 8:

            for i in range(int(spin.get())):
                lis2.insert(0,
                            ebat.get() + " İnce Kenar Amerikan Pizza  " + "Ekstra Malzemeler:  " + mlzmbilgisi + "                                           " + str(
                                malzemeli) + " TL")
                toptut.set(toplamtutar)

        elif r.get() == 5:

            for i in range(int(spin.get())):
                lis2.insert(0,
                            ebat.get() + " Kalın Kenar Amerikan Pizza  " + "Ekstra Malzemeler:  " + mlzmbilgisi + "                                           " + str(
                                malzemeli) + " TL")
                toptut.set(toplamtutar)

    elif liste.curselection() == (3,):

        if r.get() == 8:

            for i in range(int(spin.get())):
                lis2.insert(0,
                            ebat.get() + " İnce Kenar Fransız Pizza  " + "Ekstra Malzemeler:  " + mlzmbilgisi + "                                           " + str(
                                malzemeli) + " TL")
                toptut.set(toplamtutar)

        elif r.get() == 5:

            for i in range(int(spin.get())):
                lis2.insert(0,
                            ebat.get() + " Kalın Kenar Fransız Pizza  " + "Ekstra Malzemeler:  " + mlzmbilgisi + "                                           " + str(
                                malzemeli) + " TL")
                toptut.set(toplamtutar)


def MalzemeBilgisi1():
    global mlzmbilgisi

    if c1.get() != 0:
        mlzmbilgisi += "Dana Jambon,"

        return mlzmbilgisi


def MalzemeBilgisi2():
    global mlzmbilgisi

    if c2.get() != 0:
        mlzmbilgisi += "Sosis,"


def MalzemeBilgisi3():
    global mlzmbilgisi

    if c3.get() != 0:
        mlzmbilgisi += "Mısır,"

        return mlzmbilgisi


def MalzemeBilgisi4():
    global mlzmbilgisi

    if c4.get() != 0:
        mlzmbilgisi += "Ançuez,"

        return mlzmbilgisi


def MalzemeBilgisi5():
    global mlzmbilgisi

    if c5.get() != 0:
        mlzmbilgisi += "Zeytin,"

        return mlzmbilgisi


def MalzemeBilgisi6():
    global mlzmbilgisi

    if c6.get() != 0:
        mlzmbilgisi += "Salam,"

        return mlzmbilgisi


def MalzemeBilgisi7():
    global mlzmbilgisi

    if c7.get() != 0:
        mlzmbilgisi += "Sucuk,"

        return mlzmbilgisi


def MalzemeBilgisi8():
    global mlzmbilgisi

    if c8.get() != 0:
        mlzmbilgisi += "Mantar,"

        return mlzmbilgisi


def MalzemeBilgisi9():
    global mlzmbilgisi

    if c9.get() != 0:
        mlzmbilgisi += "Tonbalığı,"

        return mlzmbilgisi


def MalzemeBilgisi10():
    global mlzmbilgisi

    if c10.get() != 0:
        mlzmbilgisi += "Peynir"

        return mlzmbilgisi


def Silme():
    global mlzmbilgisi
    mlzmbilgisi = str()


def Ekleme():
    MalzemeBilgisi1()
    MalzemeBilgisi2()
    MalzemeBilgisi3()
    MalzemeBilgisi4()
    MalzemeBilgisi5()
    MalzemeBilgisi6()
    MalzemeBilgisi7()
    MalzemeBilgisi8()
    MalzemeBilgisi9()
    MalzemeBilgisi10()

    Ekleme1()


def SiparisOnayla():
    siparis=Siparis()
    siparis.MusteriNo=Musteri.MusteriNo
    print(siparis.MusteriNo)
    siparis.Ebat=ebat.get()
    siparis.Pizza=liste.get(liste.curselection())
    if(r.get()==8):
        siparis.Kenar="İnce Kenar"
    elif(r.get()==5):
        siparis.Kenar="Kalın Kenar"
    siparis.Adet=spin.get()
    siparis.Tutar=tutar2.get()
    global mlzmbilgisi
    siparis.Malzemeler=mlzmbilgisi
    print(siparis.Malzemeler)
    siparis.SiparisAl(siparis)
    Silme()


yazı = tk.Label(root, text="Pizza Otomasyonu", bg="orange", font="Ariel 12", width=97)
yazı.place(x=10, y=10)

frame1 = tk.Frame(root, width=300, height=435)
frame1.place(x=10, y=40)
frame1.config(bg="orange")

frame2 = tk.Frame(root, width=590, height=435)
frame2.place(x=290, y=40)
frame2.config(bg='orange',)

yazı2 = tk.Label(frame1, text="Ebat", font="Consolas 9")
yazı2.place(x=5, y=1)
yazı2.config(bg='orange')

ebat = Combobox(frame1, values=("Büyük", "Orta", "Küçük"), width=37)
ebat.place(x=3, y=20)

yazı3 = tk.Label(frame1, text="Pizzalar", bg='orange', font="Consolas 9")
yazı3.place(x=5, y=52)

liste = tk.Listbox(frame1, height=6, width=40)
liste.insert(0, "Türk")
liste.insert(1, "İtalyan")
liste.insert(2, "Amerikan")
liste.insert(3, "Fransız")
liste.place(x=3, y=82)

R1 = tk.Radiobutton(frame1, text="İnce Kenar", bg='orange', font="Ariel 9", variable=r, value=8)
R1.place(x=5, y=190)

R2 = tk.Radiobutton(frame1, text="Kalın Kenar", bg='orange', font="Ariel 9", variable=r, value=5)
R2.place(x=150, y=190)

yazı4 = tk.Label(frame1, text="Malzemeler", bg='orange', font="Consolas 9")
yazı4.place(x=14, y=213)

buton = tk.Checkbutton(frame1, text="Dana Jambon", bg='orange', font="Ariel 9", variable=c1, onvalue=10, offvalue=0)
buton.place(x=10, y=230)
buton = tk.Checkbutton(frame1, text="Sosis", bg='orange', font="Ariel 9", variable=c2, onvalue=5, offvalue=0)
buton.place(x=10, y=255)
buton = tk.Checkbutton(frame1, text="Mısır", bg='orange', font="Ariel 9", variable=c3, onvalue=4, offvalue=0)
buton.place(x=10, y=280)
buton = tk.Checkbutton(frame1, text="Ançuez", bg='orange', font="Ariel 9", variable=c4, onvalue=6, offvalue=0)
buton.place(x=10, y=305)
buton = tk.Checkbutton(frame1, text="Zeytin", bg='orange', font="Ariel 9", variable=c5, onvalue=5, offvalue=0)
buton.place(x=10, y=330)
buton = tk.Checkbutton(frame1, text="Salam", bg='orange', font="Ariel 9", variable=c6, onvalue=6, offvalue=0)
buton.place(x=120, y=230)
buton = tk.Checkbutton(frame1, text="Sucuk", bg='orange', font="Ariel 9", variable=c7, onvalue=8, offvalue=0)
buton.place(x=120, y=255)
buton = tk.Checkbutton(frame1, text="Mantar", bg='orange', font="Ariel 9", variable=c8, onvalue=6, offvalue=0)
buton.place(x=120, y=280)
buton = tk.Checkbutton(frame1, text="Tonbalığı", bg='orange', font="Ariel 9", variable=c9, onvalue=8, offvalue=0)
buton.place(x=120, y=305)
buton = tk.Checkbutton(frame1, text="Peynir", bg='orange', font="Ariel 9", variable=c10, onvalue=5, offvalue=0)
buton.place(x=120, y=330)

yazı5 = tk.Label(frame1, text="Adet", bg='orange', font="Consolas 10")
yazı5.place(x=14, y=365)

spin = tk.Spinbox(frame1, from_=1, to=10)
spin.place(x=60, y=367, width=70)

hesap1 = tk.Button(frame1, text="Hesapla", font="Consolas 10", width=13, command=GenelHesaplama)
hesap1.place(x=150, y=364)

lis2 = tk.Listbox(frame2, height=19, width=97)
lis2.place(x=1, y=20)


yazı6 = tk.Label(frame2, text="Toplam Tutar :")
yazı6.place(x=340, y=340)
yazı6.config(bg='orange')

yazı7 = tk.Label(frame2, text="Tutar :")
yazı7.place(x=15, y=375)
yazı7.config(bg='orange')

tutar1 = ttk.Entry(frame2, textvariable=operasyon)
tutar1.place(x=65, y=377)


hesap2 = tk.Button(frame2, text="Sepete Ekle", width=13, command=Ekleme)
hesap2.place(x=220, y=375)

tutar2 = ttk.Entry(frame2, textvariable=toptut)
tutar2.place(x=430, y=340)

hesap3 = tk.Button(frame2, text="Siparişi Onayla", width=13, height=3, command=SiparisOnayla)
hesap3.place(x=490, y=365)


root.mainloop()