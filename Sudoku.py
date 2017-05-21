import tkinter as tk
from tkinter import Canvas

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
    def __init__(self, master, visina=10,sirina=10):
        self.visina=visina
        self.sirina=sirina
        self.polja=[]
        for _ in range(self.visina):
            vrstica = []
            for _ in range(self.sirina):
                vrstica.append(None)
            self.polja.append(vrstica)

        self.canvas = Canvas(master,width=90,heigh=90,background = "white")
        self.canvas.grid(row=1,column=0,columnspan=2)

        """Vrstice, stolpci, dve tocki(x,y)"""
        self.canvas.create_line(50,0,50,450)
        self.canvas.create_line(100,0,100,450)
        self.canvas.create_line(150,0,150,450,width=2)
        self.canvas.create_line(200,0,200,450)
        self.canvas.create_line(250,0,250,450,width=2)
        self.cavas.create_line(300,0,300,450)
        self.canvas.create_line(350,0,350,450)
        self.canvas.create_line(400,0,400,450)

        self.canvas.create_line(0,50,450,50)
        self.canvas.create_line(0,100,450,100)
        self.canvas.create_line(0,150,450,150,width=2)
        self.canvas.create_line(0,200,450,200)
        self.canvas.create_line(0,250,450,250)
        self.canvas.create_line(0,300,450,300,width=2)
        self.canvas.create_line(0,350,450,350)
        self.canvas.create_line(0,400,450,400)
        
    
                  
    def __repr__(self):
        return "Plosca(visina={},sirina={}".format(
            self.visina, self.sirina)
    
    def dodaj_stevilo(self, master, stevilo,polje):
        return


        
    


