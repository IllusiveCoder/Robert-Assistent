import time
from tkinter import filedialog
from tkinter import *
from tkinter import Frame, Entry, Tk, Listbox
import pygame
from pygame.locals import *
from mutagen.mp3 import MP3
from tkinter import messagebox
import threading
import winsound
import os
import webbrowser
   
pygame.init()

class gal_help():#-----------------------------------------------------------Anleitungen----------------------------------------------------------------------------------------------------------------------------------------------------
     
    def __init__(self):
        self.main = Tk()
        self.main.geometry("230x80")
        self.main.maxsize(230,80)
        self.main.title("Hilfe")
        self.main.configure(bg = "light green")
        self.hilfelabel = Label(self.main, text = "1. Name vom Bild eingeben", font = 30, bg = "light green")
        self.hilfelabel.grid(row = 0, column = 0, sticky = (W))
        self.hilfelabel1 = Label(self.main, text = "2. Button 'Hinzufügen' drücken", font = 30, bg = "light green")
        self.hilfelabel1.grid(row = 1, column = 0, sticky = (W))
        self.hilfelabel2 = Label(self.main, text = "3. Datei auswählen", font = 30, bg = "light green")
        self.hilfelabel2.grid(row = 2, column = 0, sticky = (W))
        self.main.mainloop()

class mus_help():
     
    def __init__(self):
        self.main = Tk()
        self.main.geometry("250x80")
        self.main.maxsize(250,80)
        self.main.title("Hilfe")
        self.main.configure(bg = "light green")
        self.hilfelabel = Label(self.main, text = "1. Name vom Lied eingeben", font = 30, bg = "light green")
        self.hilfelabel.grid(row = 0, column = 0, sticky = (W))
        self.hilfelabel1 = Label(self.main, text = "2. Button 'Lied hinzufügen' drücken", font = 30, bg = "light green")
        self.hilfelabel1.grid(row = 1, column = 0, sticky = (W))
        self.hilfelabel2 = Label(self.main, text = "3. Datei auswählen", font = 30, bg = "light green")
        self.hilfelabel2.grid(row = 2, column = 0, sticky = (W))
        self.main.mainloop()
    
class galerie(): #-------------------------------------------------------------------------------------Galerie--------------------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.bliste = []
        self.main = Tk()
        self.main.geometry("300x175")
        self.main.maxsize(300,175)
        self.main.title("Galerie")
        self.main.configure(bg = "#00cccc")
        self.obererFrame = Frame(self.main, bg = "#00cccc")
        self.obererFrame.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = (N))
        self.bilderliste = Listbox(self.main,  bg = "#ffc266")
        self.obererinnerFrame = Frame(self.obererFrame, bg = "#79EABB")
        self.obererinnerFrame.grid(row = 0, column = 0)
        self.bilderliste.grid(row = 0, column = 0,rowspan = 2, sticky =(N,S))
        self.label = Label(self.obererFrame, text = "Dateiname:", bg = "#00cccc")
        self.label.grid(row = 2, column = 0, columnspan = 2, sticky = (S))
        self.eingabe = Entry(self.obererFrame, bg = "#b3ffff")
        self.eingabe.grid(row=3, column = 0, columnspan = 2, sticky = (S))
        self.galerie_help = Button(self.obererFrame, text = "Anleitung",command = lambda: gal_help(), bg = "#79EABB", relief = "flat",  activebackground = "#79EABB")
        self.galerie_help.grid(row = 4, column = 0, sticky = (S), pady = 20)
        self.einfügenb = Button(self.obererinnerFrame, text = "Anzeigen", command = self.öffne_bild, relief = "flat", bg = "#79EABB", activebackground = "#79EABB")
        self.einfügenb.grid(row = 0, column = 3, sticky = (W))
        self.bild_hb = Button(self.obererinnerFrame, text = "Hinzufügen", command = self.bild_hinzufügen, relief = "flat", bg = "#79EABB", activebackground = "#79EABB")
        self.bild_hb.grid(row=0,column=4, sticky = (W))
        self.bildlb = Button(self.obererinnerFrame, text = "Bild löschen", command = self.bild_löschen, relief = "flat", bg = "#79EABB", activebackground = "#79EABB")
        self.bildlb.grid(row = 1, column = 3)
        self.beendeb = Button(self.obererinnerFrame, text = "Beenden", command = self.beenden, relief = "flat", bg = "#79EABB", activebackground = "#79EABB")
        self.beendeb.grid(row = 1, column = 4)
        self.main.mainloop()
        
    def beenden(self):
        self.main.destroy()

    def öffne_bild(self):
        self.new = Toplevel(self.main)
        self.element = self.bilderliste.index("active")
        self.lbbild = Label(self.new, image = self.bliste[self.element])
        self.lbbild.pack()

    def bild_hinzufügen(self):
        self.directory = filedialog.askopenfilename()
        self.bilderliste.insert("end", self.eingabe.get())
        self.file = PhotoImage(file = self.directory)
        self.bliste.append(self.file)

    def bild_löschen(self):
        if self.bilderliste.curselection():
            self.index = bilderliste.curselection()[0]
            self.bliste.pop(self.index)
            self.bilderliste.delete(self.index)        
            
class musicplayer(): #-----------------------------------------------------Music-Player-----------------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.main = Tk()
        self.main.geometry("400x175")
        self.main.maxsize(400,175)
        self.main.title("Musikplayer")
        self.main.configure(bg = "#00cccc")
        self.pausiert = False
        self.audio = StringVar()
        self.info = StringVar()
        self.lieder = []
        self.ersterframe = Frame(self.main, bg = "#79EABB")
        self.ersterframe.grid(row = 0, column = 1, sticky = (W,N))
        self.zweiterframe = Frame(self.main, bg = "#00cccc")
        self.zweiterframe.grid(row = 0, column = 2, sticky = (W,N))
        self.dritterframe = Frame(self.ersterframe, bg = "#00cccc")
        self.dritterframe.grid(row = 3, column = 0, columnspan = 2)
        self.liederliste = Listbox(self.main, relief = "flat",  bg = "#ffc266")
        self.liederliste.grid(row = 0, column = 0)
        self.skala = Scale(self.zweiterframe,from_ =0, to=100, orient="horizontal", command= self.lregulierung, relief = "flat", bg = "#79EABB", activebackground = "#79EABB")
        self.skala.set(50)  
        pygame.mixer.music.set_volume(0.5)
        self.skala.grid(row=2, column=0, sticky = (S), pady = 10)
        self.labeldateiname = Label(self.zweiterframe, text = "Dateiname:", bg = "#00cccc")
        self.labeldateiname.grid(row = 0, column = 0)
        self.eingabe = Entry(self.zweiterframe, relief = "flat", bg = "#b3ffff")
        self.eingabe.grid(row=1,column=0, sticky = (E,S), padx = 10, pady = 10)
        self.lb1 = Label(self.dritterframe, text = "Länge des Liedes: ---", bg = "#00cccc", bd = 8)
        self.lb1.grid(row = 0, column = 0, columnspan = 2, sticky = (W,S))
        self.lb2 = Label(self.dritterframe, text = "Aktuelle Zeit: ---", bg = "#00cccc", bd = 12)
        self.lb2.grid(row = 1, column = 0, columnspan = 2, sticky = (W,N))
        self.playbutton = Button(self.ersterframe, text = "Abspielen", command = self.play, relief = "flat", bg = "#79EABB", activebackground = "#79EABB")
        self.playbutton.grid(row = 0,column = 0)
        self.stopbutton = Button(self.ersterframe, text = "Pause", command = self.pause, relief = "flat", bg = "#79EABB", activebackground = "#79EABB")
        self.stopbutton.grid(row=0,column=1)
        self.lbutton = Button(self.ersterframe, text = "Lied\nhinzufügen", command = self.lied_hinzufügen, relief = "flat", bg = "#79EABB", activebackground = "#79EABB")
        self.lbutton.grid(row = 1, column = 0)
        self.lösche_b = Button(self.ersterframe, text = "Lied\nlöschen", command = self.lied_löschen, relief = "flat", bg = "#79EABB", activebackground = "#79EABB")
        self.lösche_b.grid(row = 1, column = 1)
        self.dbutton = Button(self.ersterframe, text = "Stopp", command = self.stop, relief = "flat", bg = "#79EABB", activebackground = "#79EABB")
        self.dbutton.grid(row = 2, column = 0)
        self.destroybutton = Button(self.ersterframe, text = "Beenden", command = self.beenden, relief = "flat", bg = "#79EABB", activebackground = "#79EABB")
        self.destroybutton.grid(row = 2, column = 1)
        self.help_button = Button(self.zweiterframe, text = "Anleitung", command = lambda: mus_help(), relief = "flat", bg = "#79EABB", activebackground = "#79EABB")
        self.help_button.grid(row = 3,column = 0, pady = 5, sticky = (S))
        self.liedleiste = Menu(self.main)
        self.ll = Menu(self.liedleiste)
        self.ll.add_command(label = "Lied laden", command = self.liedleiste_lied_hinzufügen)
        self.ll.add_command(label = "Player beenden", command = self.beenden)
        self.ll.add_command(label = "Selbstzerstörung", command = self.lüge)
        self.liedleiste.add_cascade(label = "Dateien", menu = self.ll)
        self.main["menu"] = self.liedleiste
        self.main.mainloop()

        
    def start_count(self, t):
        self.aktuelle_Zeit = 0
        self.minuten = 0
        while self.aktuelle_Zeit <= t and pygame.mixer.music.get_busy():
            if self.pausiert:
                continue
            else:
                self.a_zeit = ' {}'.format(str(self.aktuelle_Zeit))
                self.minuten_Z = ' {}'.format(str(self.minuten))
                self.lb2["text"] = "Aktuelle Zeit:" + self.minuten_Z + " Minuten und " + self.a_zeit + " Sekunden" 
                time.sleep(1)
                self.aktuelle_Zeit += 1
                if self.aktuelle_Zeit > 59:
                    self.minuten += 1
                    self.aktuelle_Zeit = 0
                

    def play(self):
        if self.pausiert:
            pygame.mixer.music.unpause()
            self.pausiert = False
        else:
            self.element = self.liederliste.index("active")
            pygame.mixer.music.load(self.lieder[self.element])
            pygame.mixer.music.play(0,0.0)
            self.musicPlaying = True
            self.audio = MP3(self.lieder[self.element])
            self.info = str(round(self.audio.info.length))
            self.newinfo = int(self.info)
            self.minuten = round(self.newinfo/60)
            self.sekunden = self.newinfo - self.minuten * 60
            self.lb1["text"] = "Länge des Liedes: {0} Minuten  und {1} Sekunden".format(self.minuten,self.sekunden)
            self.t1 = threading.Thread(target=self.start_count, args=(self.newinfo,))
            self.t1.start()

    def pause(self):
            pygame.mixer.music.pause()
            self.pausiert = True

    def lied_hinzufügen(self):
        self.directory = filedialog.askopenfilename()
        self.liederliste.insert("end", self.eingabe.get())
        self.lieder.append(self.directory)
        
    def lied_löschen(self):
         if self.liederliste.curselection():
            self.index = self.liederliste.curselection()[0]
            self.lieder.pop(self.index)
            self.liederliste.delete(self.index)

    def stop(self):
        pygame.mixer.music.stop()

    def beenden(self):
        self.main.destroy()
        pygame.mixer.music.stop()

    def lregulierung(self, lautstärke):
        self.lautstärkewert = float(lautstärke) / 100
        pygame.mixer.music.set_volume(self.lautstärkewert)

    def lüge(self):
        self.frequency = 550
        self.duration = 200
        winsound.Beep(self.frequency, self.duration)
        self.antwort = messagebox.askokcancel("Selbstzerstörung", "Selbstzerstörung wurde eingeleitet!")
        if self.antwort == 1:
            self.box_ = Toplevel()
            self.lb = Label(self.box_, text = "Sie wurden hereingelegt!")
            self.lb.pack()
        else:
            self.box_ = Toplevel()
            self.lb = Label(self.box_, text = "Sie wurden hereingelegt!")
            self.lb.pack()

    def einlesen(self):
        self.datei = filedialog.askopenfilename()
        self.liederliste.insert("end", self.eingabe.get())
        self.lieder.append(self.datei)
        self.einfügen.destroy()

    def liedleiste_lied_hinzufügen(self):
         self.einfügen = Toplevel()

         self.button = Button(self.einfügen, text = "Einlesen", command = self.einlesen)
         self.button.grid(row = 0, column = 3)

         self.eingabe = Entry(self.einfügen)
         self.eingabe.grid(row = 0,column = 0, columnspan = 2, padx = 7)
    

class internetlink():#-----------------------------------------Internetlink öffnen-----------------------------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.main = Tk()
        self.main.geometry("270x100")
        self.main.configure(bg = "#0099cc")
        self.main.title("Link-Öffner")
        self.main.maxsize(270,100)
        self.frame = Frame(self.main, bg = "#ff6633", bd = 5)
        self.frame.grid(row = 0, column = 0, sticky = (W,E), padx = 20, pady = 20)
        self.entry = Entry(self.frame, relief = "flat")
        self.entry.grid(row = 0, column = 0)
        self.startbutton = Button(self.frame, text= "Starten", command = self.verbinden, relief = "flat")
        self.startbutton.grid(row = 0, column = 1, padx = 10)
        self.ausgabe = Label(self.main, text = "Bitte etwas eingeben!", font = 20, bg = "#0099cc", anchor = "n")
        self.ausgabe.grid(row = 1, column = 0)

    def verbinden(self):
        self.eingabe = self.entry.get()
        webbrowser.get("windows-default")
        webbrowser.open_new_tab(self.eingabe)

class timer(): #------------------------------------------------------------Timer-------------------------------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.sekunden = 0
        self.minuten = 0
        self.gesamtlänge = 0
        self.main = Tk()
        self.main.geometry("400x100")
        self.main.title("Timer")
        self.main.maxsize(400,100)
        self.main.configure(bg = "#0099cc")
        self.obererFrame = Frame(self.main, bg = "#0099cc", bd = 5)
        self.obererFrame.grid(row = 0, column = 0, sticky = (N,S), padx = 10, pady = 10)
        self.obererinnererFrame = Frame(self.obererFrame, bg = "#ff6633", bd = 5)
        self.obererinnererFrame.grid(row = 0, column = 0)
        self.eingabe = Entry(self.obererinnererFrame, relief = "flat")
        self.eingabe.grid(row = 0, column = 0)
        self.eingabe1 = Entry(self.obererinnererFrame, relief = "flat")
        self.eingabe1.grid(row = 0, column = 1, padx = 10)
        self.start_b = Button(self.obererinnererFrame, text = "Start", command = self.starten, relief = "flat")
        self.start_b.grid(row = 0, column = 2, padx = 15)
        self.timelabel = Label(self.obererFrame, text = "---", bg = "#0099cc", fg  = "white")
        self.timelabel.grid(row = 1, column = 0, columnspan = 3, pady = 20)
        self.main.mainloop()

    def timer_count(self,t):
        self.zeitvariable = self.gesamtlänge
        while self.zeitvariable > 0:
                self.a_sec = ' {}'.format(str(self.sekunden))
                self.a_min = ' {}'.format(str(self.minuten))
                self.timelabel.config(text = "{0} : {1} Min.".format(str(self.a_min), str(self.a_sec)))
                time.sleep(1)                   
                self.sekunden -= 1
                self.zeitvariable -= 1
                if self.sekunden == 0:
                    self.minuten -= 1
                    self.sekunden = 59
                    self.zeitvariable -= 1
        else:
            self.timelabel.config(text = "gesetzter Punkt wurde erreicht!") 
            self.frequency = 200
            self.duration = 5000
            winsound.Beep(self.frequency, self.duration)

    def starten(self):
        self.minuten = int(self.eingabe.get())
        self.sekunden = int(self.eingabe1.get())
        self.gesamtlänge = (self.minuten*60) + self.sekunden
        self.timerthread = threading.Thread(target=self.timer_count, args=(self.gesamtlänge,))
        self.timerthread.start()


class hilfe(): #----------------------------------------------------------------------Hilfelabel---------------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.main = Tk()
        self.main.geometry("500x200")
        self.main.maxsize(500,200)
        self.main.title("Hilfe")
        self.main.configure(bg = "light green")
        self.hilfelabel = Label(self.main, text = "- Robert Info: zeigt alle Infos zum persönlichen Assistenten", font = 30, bg = "light green")
        self.hilfelabel.grid(row = 0, column = 0, sticky = (W))
        self.hilfelabel1 = Label(self.main, text = "- aktuelle Zeit: Robert zeigt dir das aktuelle Datum und die Uhrzeit", font = 30, bg = "light green")
        self.hilfelabel1.grid(row = 1, column = 0, sticky = (W))
        self.hilfelabel2 = Label(self.main, text = "- Öffne Galerie: Öffnet die Galerie", font = 30, bg = "light green")
        self.hilfelabel2.grid(row = 2, column = 0, sticky = (W))
        self.hilfelabel3 = Label(self.main, text = " - Öffne Player: Öffnet den Musikmediathek", font = 30, bg = "light green")
        self.hilfelabel3.grid(row = 3, column = 0, sticky = (W))
        self.hilfelabel4 = Label(self.main, text = "- Hilfe: Öffnet dieses Label", font = 30, bg = "light green")
        self.hilfelabel4.grid(row = 4, column = 0, sticky = (W))
        self.hilfelabel5 = Label(self.main, text = "- Timer: Öffnet einen Timer", font = 30, bg = "light green")
        self.hilfelabel5.grid(row = 5, column = 0, sticky = (W))
        self.hilfelabel6 = Label(self.main, text = "- Internet: Öffnet ein Programm zum eingeben von Internetlinks", font = 30, bg = "light green")
        self.hilfelabel6.grid(row = 6, column = 0, sticky = (W))
        self.hilfelabel7 = Label(self.main, text = "- Rechner: Öffnet einen kleinen Taschenrechner", font = 30, bg = "light green")
        self.hilfelabel7.grid(row = 7, column = 0, sticky = (W))
        self.main.mainloop()
        
class Robert: #-------------------------------------------------------------------Klasse Robert(seine Persönlichkeit)-----------------------------------------------------------------------------------------------------------------------
    
    def __init__(self):
        self.höhe = 80
        self.breite = 200
        self.benutzername = ""
        self.geburtsdatum = "17.6.19 um 22:48"
        self.name = "Robert"
        self.main = Tk()
        self.main.config(width = self.breite, height = self.höhe, bg = "light green")
        self.main.title("Service Assistent")
        self.main.maxsize(500,300)
        self.obererBlock = Frame(self.main, width = 300, height = 200, bg="light green")
        self.obererBlock.grid(row = 0, column = 0, rowspan = 2, columnspan = 1, sticky = (W,E), padx = 5, pady = 5)
        self.eingabe = Entry(self.obererBlock, bg = "light cyan")
        self.eingabe.grid(row = 1, column = 0, sticky = (W))
        self.hauptüberschrift = Label(self.obererBlock, text = "Robert, dein Assistent!", font = "30", bg = "light green")
        self.hauptüberschrift.grid(row = 0,column = 0, sticky = (W))
        self.robertlabel = Label(self.obererBlock, text = "Robert: ", font = "20", bg = "light green", relief = "flat")
        self.robertlabel.grid(row = 2, column = 0, sticky = (W))
        self.searchbutton = Button(self.obererBlock, text = "Suchen", command = lambda: self.search(""), relief = "flat", activebackground = "light cyan", activeforeground = "black", fg = "black", bg = "light cyan")
        self.searchbutton.grid(row = 1, column = 1)
        self.eingabe.bind("<Return>", self.search)
        self.main.mainloop()
        
    def search(self, enter):
        if "galerie" in self.eingabe.get().lower():
            Galerie = galerie()
        elif "musik" in self.eingabe.get().lower():
            Player = musicplayer()
        elif "internet" in self.eingabe.get().lower():
            Linkseite = internetlink()
        elif "timer" in self.eingabe.get().lower():
            Zähler = timer()
        elif "hilfe" in self.eingabe.get().lower():
            Hilfe = hilfe()
        elif "rechner" in self.eingabe.get().lower():
            os.system("Taschenrechner.pyw")
        elif "willst du mit mir ausgehen?" in self.eingabe.get().lower():
            self.robertlabel["text"] = "Robert: Wenn du bezahlst gerne :)"
        elif "wie schlau bist du?" in self.eingabe.get().lower():
            self.robertlabel["text"] = "Robert: Auf jeden Fall kann ich mehr als eine Kartoffel:)"
        elif "zeit" in self.eingabe.get().lower():
            self.zeit = StringVar()
            self.zeit = time.strftime("Wir haben den %d.%m.%Y  um: %H:%M:%S Uhr")
            self.robertlabel["text"] = "Robert: " + self.zeit
        elif "info" in self.eingabe.get().lower():
            self.robertlabel["text"]  = "Robert:\nName des Assistenten:\n" + self.name + "\nGeburtsdatum:\n " + self.geburtsdatum
        else:
            self.robertlabel["text"] = "Robert: Falsche Eingabe!"

Assistent = Robert()



    
    
        
