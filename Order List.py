from Order import *
from Musteri import *

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox

def siparisGetir():
    liste=Siparis.GetSiparis()
    for i in liste:
        lis2.insert(0,i)


root = tk.Tk()
root.geometry("900x480")
root.title("Pizza Otomasyonu")


yazı = tk.Label(root, text="Pizza Otomasyonu", bg="darkgray", font="Ariel 12", width=97)
yazı.place(x=10, y=10)

frame2 = tk.Frame(root, width=900, height=480)
frame2.place(x=20, y=40)

lis2 = tk.Listbox(frame2, height=19, width=142)
lis2.place(x=1, y=20)

btn = tk.Button(root, text="Siparişler", font="Consolas 10", width=13, command=siparisGetir)
btn.place(x=20, y=400)
root.mainloop()