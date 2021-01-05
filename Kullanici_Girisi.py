from Musteri import *
from tkinter import *
from tkinter import messagebox

pencere = Tk()
pencere.geometry("500x500")
pencere.config(bg="Orange")
def girisyapma():
    parola = parolagiris.get()
    isim = isimgiris.get()
    if(parola!="" and isim!=""):
        musteri = Musteri()
        musteri=musteri.LoginUser(isim,parola)
        if (parola == str(musteri.Password) and isim == musteri.AdSoyad):
            messagebox.showinfo("OKEY","GİRİŞ BAŞARILI")
            pencere.destroy()
            import PizzaciOtomasyonu
            PizzaciOtomasyonu.root.mainloop()
        else:
            messagebox.showerror("HATA", "GİRİŞ BAŞARISIZ")
    else:
        messagebox.showwarning("Uyarı","Adınız ve Şifreniz alanlarını boş geçemezsiniz!!!")

def kayityapma():
    pencere.withdraw()
    import Kullanici_Kayit
    Kullanici_Kayit.pencere.mainloop()


isim = Label(pencere, text = "Name  : ", font=("Times",14))
isim.grid(row=0, column=0, sticky="W")
isim.config(bg="Orange")
isimgiris = Entry(pencere, width="40", bd=3)
isimgiris.grid(row=0, column=1, columnspan=2)

parola = Label(pencere, text="Password: ", font=("Consolas",14))
parolagiris = Entry(pencere, width="40", show="*", bd=3)
parola.config(bg="Orange`")
parola.grid(row=1, column=0, sticky="W")
parolagiris.grid(row=1, column=1, columnspan=2)

giris = Button(pencere, text="Enter", command=girisyapma, width="16", bd=3)
giris.grid(row=5, column=1)

kayit = Button(pencere, text="Sign Up", command=kayityapma, width="16", bd=3)
kayit.grid(row=5, column=2)

pencere.mainloop()