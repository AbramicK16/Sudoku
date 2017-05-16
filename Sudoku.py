import tkinter as tk

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
    def __init__(self, visina=10,sirina=10):
        self.visina=visina
        self.sirina=sirina
        self.polja=[]
        for _ in range(self.visina):
            vrstica = []
            for _ in range(self.sirina):
                vrstica.append(None)
            self.polja.append(vrstica)
            
       

        
        
    def __repr__(self):
        return "Plosca(visina={},sirina={}".format(
            self.visina, self.sirina)
    
    def dodaj_stevilo(self, stevilo,polje):
        return




