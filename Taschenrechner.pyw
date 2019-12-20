from tkinter import *
from tkinter import ttk

class taschenrechner():

    def __init__(self):
        self.eingabe_ = ""
        self.main = Tk()
        self.main.geometry("174x160")
        self.main.maxsize(174,160)
        self.main.title("Taschenrechner")
        self.eingabestring = StringVar()
        self.of = Frame(self.main, bg = "#00cccc")
        self.of.grid(row = 0, column = 0)
        self.anzeige = Entry(self.of, textvariable = self.eingabestring, relief = "flat", bg = "#b3ffff")
        self.anzeige.grid(row = 0, column = 0, columnspan = 4, rowspan = 2, padx = 8)
        self.tastatur = Frame(self.of, bg = "#79EABB")
        self.tastatur.grid(row = 3, column = 0, columnspan = 6, padx = 2, sticky = (W,E))
        self.r1 = Frame(self.tastatur, bg = "#79EABB")
        self.r1.grid(row = 0, column = 0, padx = 10)
        self.r2 = Frame(self.tastatur, bg = "#79EABB")
        self.r2.grid(row = 0, column = 1, padx = 10)
        self.r3 = Frame(self.tastatur, bg = "#79EABB")
        self.r3.grid(row = 0, column = 2, padx = 10)
        self.r4 = Frame(self.tastatur, bg = "#79EABB")
        self.r4.grid(row = 0, column = 3, padx = 10)
        self.nullb = Button(self.r2, text = "0",command= lambda: self.eingabe("0"), relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.nullb.grid(row =3, column = 0)
        self.einsb = Button( self.r1, text = "1",command= lambda: self.eingabe("1"), relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.einsb.grid(row =2, column = 0)
        self.zweib = Button( self.r2, text = "2",command= lambda: self.eingabe("2"), relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.zweib.grid(row =2, column = 0)
        self.dreib = Button(self.r3, text = "3",command= lambda: self.eingabe("3"), relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.dreib.grid(row =2, column = 0)
        self.vierb = Button( self.r1, text = "4",command= lambda: self.eingabe("4"), relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.vierb.grid(row =1, column = 0)
        self.fünfb = Button( self.r2, text = "5",command= lambda: self.eingabe("5"), relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.fünfb.grid(row =1, column = 0)
        self.sechsb = Button(self.r3, text = "6",command= lambda: self.eingabe("6"), relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.sechsb.grid(row =1, column = 0)
        self.siebenb = Button( self.r1, text = "7",command= lambda: self.eingabe("7"), relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.siebenb.grid(row =0, column = 0)
        self.achtb = Button( self.r2, text = "8",command= lambda: self.eingabe("8"), relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.achtb.grid(row =0, column = 0)
        self.neunb = Button(self.r3, text = "9",command= lambda: self.eingabe("9"), relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.neunb.grid(row =0, column = 0)
        self.kommab = Button(self.r3, text = ",",command= lambda: self.eingabe("."), relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.kommab.grid(row =3, column = 0)
        self.plusb = Button(self.r4, text = "+",command= lambda: self.eingabe("+"), relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.plusb.grid(row =2, column = 0)
        self.minusb = Button(self.r4, text = "-",command= lambda: self.eingabe("-"), relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.minusb.grid(row =1, column = 0)
        self.divideb = Button( self.r1, text = "/",command= lambda: self.eingabe("/"), relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.divideb.grid(row =3, column = 0)
        self.malb = Button(self.r4, text = "*",command= lambda: self.eingabe("*"), relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.malb.grid(row =0, column = 0)
        self.istgleichb = Button(self.r4, text = "=", command = self.istgleich, relief = "flat", font = 20, bg = "#79EABB", activebackground = "#79EABB")
        self.istgleichb.grid(row =3, column = 0)
        self.löscheb = Button(self.of, text = "del", command = self.löschen, relief = "flat", font = 15, bg = "#79EABB", activebackground = "#79EABB")
        self.löscheb.grid(row =0, column = 4, sticky = (W))
        self.main.mainloop()

    def eingabe(self, zeichen):
        self.eingabe_ = self.eingabe_ + str(zeichen)
        self.eingabestring.set(self.eingabe_)

    def istgleich(self): 
        try: 
            self.total = str(eval(self.eingabe_)) 
            self.eingabestring.set(self.total) 
            self.eingabe_ = "" 
        except: 
            self.eingabestring.set("Falsche Eingabe!") 
            self.eingabe_ = "" 

    def löschen(self):  
        self.eingabe_ = "" 
        self.eingabestring.set("")     

taschenrechner()
