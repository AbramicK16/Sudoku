import tkinter as tk
from tkinter import Canvas
from tkinter import Entry
import random

master = tk.Tk()

okno=tk.Tk()
zgoraj=tk.Frame(okno)
zgoraj.pack()
spodaj=tk.Frame(okno)
spodaj.pack()
gumb1=tk.Button(zgoraj,text="ZAČNI").pack()
gumb2=tk.Button(spodaj,text="SHRANI").grid(row=0,column=0)
gumb3=tk.Button(spodaj,text="REŠITEV").grid(row=0,column=1)
gumb4=tk.Button(spodaj,text="NOVA IGRA").grid(row=0,column=2)


class Plosca:
    def __init__(self, master):
        
        self.vnosna_polja = []
        for _ in range(9):
            vrstica = []
            for _ in range(9):
                vrstica.append(None)
            self.vnosna_polja.append(vrstica)
        
        for i in range(9):
            for j in range(9):
                e = Entry(master, width=7)
                self.vnosna_polja[i][j] = e
                e.grid(row = i, column = j)
                  
    def __repr__(self):
        return "Plosca"
    
    def dodaj_stevilo(self, master, stevilo, x, y):
        self.vnosna_polja[x][y].insert(0, stevilo)
            


p = Plosca(master)        
p.dodaj_stevilo(master, 7, 2, 3)


