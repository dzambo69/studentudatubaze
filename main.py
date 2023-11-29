# Instalējiet PyMySQL, ja nepieciešams
#pip install PyMySQL
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

# Savienojums ar phpMyAdmin
def savienojums():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='',
        db='students_db',
    )
    return conn

def atjaunotTabulu():
    for dati in mans_koks.get_children():
        mans_koks.delete(dati)

    for masivs in lasit():
        mans_koks.insert(parent='', index='end', iid=masivs, text="", values=(masivs), tag="orinda")

    mans_koks.tag_configure('orinda', background='#EEEEEE', font=('Arial', 12))
    mans_koks.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

sakne = Tk()
sakne.title("Students Reģistrācijas Sistēma")
sakne.geometry("1080x720")
mans_koks = ttk.Treeview(sakne)

# Ievades laukumiem vietas rezervēšana
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

# Vietas rezervēšanas funkcija
def iestatitVr(vards, num):
    if num ==1:
        ph1.set(vards)
    if num ==2:
        ph2.set(vards)
    if num ==3:
        ph3.set(vards)
    if num ==4:
        ph4.set(vards)
    if num ==5:
        ph5.set(vards)

def lasit():
    conn = savienojums()
    kursors = conn.cursor()
    kursors.execute("SELECT * FROM students")
    rezultati = kursors.fetchall()
    conn.commit()
    conn.close()
    return rezultati

def pievienot():
    studid = str(studidIevade.get())
    vards = str(vardsIevade.get())
    uzvards = str(uzvardsIevade.get())
    adrese = str(adreseIevade.get())
    telefons = str(telefonsIevade.get())

    if (studid == "" or studid == " ") or (vards == "" or vards == " ") or (uzvards == "" or uzvards == " ") or (adrese == "" or adrese == " ") or (telefons == "" or telefons == " "):
        messagebox.showinfo("Kļūda", "Lūdzu, aizpildiet tukšo ievades lauku")
        return
    else:
        try:
            conn = savienojums()
            kursors = conn.cursor()
            kursors.execute("INSERT INTO students VALUES ('"+studid+"','"+vards+"','"+uzvards+"','"+adrese+"','"+telefons+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Kļūda", "Studenta ID jau eksistē")
            return

    atjaunotTabulu()
    
def resetet():
    lemums = messagebox.askquestion("Brīdinājums!!", "Dzēst visus datus?")
    if lemums != "yes":
        return 
    else:
        try:
            conn = savienojums()
            kursors = conn.cursor()
            kursors.execute("DELETE FROM students")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Kļūda", "Diemžēl radās kļūda")
            return

        atjaunotTabulu()

def dzest():
    lemums = messagebox.askquestion("Brīdinājums!!", "Dzēst atlasītos datus?")
    if lemums != "yes":
        return 
    else:
        atlasitais_viens = mans_koks.selection()[0]
        dzestDati = str(mans_koks.item(atlasitais_viens)['values'][0])
        try:
            conn = savienojums()
            kursors = conn.cursor()
            kursors.execute("DELETE FROM students WHERE STUDID='"+str(dzestDati)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Kļūda", "Diemžēl radās kļūda")
            return

        atjaunotTabulu()

def atlasit():
    try:
        atlasitais_viens = mans_koks.selection()[0]
        studid = str(mans_koks.item(atlasitais_viens)['values'][0])
        vards = str(mans_koks.item(atlasitais_viens)['values'][1])
        uzvards = str(mans_koks.item(atlasitais_viens)['values'][2])
        adrese = str(mans_koks.item(atlasitais_viens)['values'][3])
        telefons = str(mans_koks.item(atlasitais_viens)['values'][4])

        iestatitVr(studid,1)
        iestatitVr(vards,2)
        iestatitVr(uzvards,3)
        iestatitVr(adrese,4)
        iestatitVr(telefons,5)
    except:
        messagebox.showinfo("Kļūda", "Lūdzu, atlasiet datu rindu")

def meklet():
    studid = str(studidIevade.get())
    vards = str(vardsIevade.get())
    uzvards = str(uzvardsIevade.get())
    adrese = str(adreseIevade.get())
    telefons = str(telefonsIevade.get())

    conn = savienojums()
    kursors = conn.cursor()
    kursors.execute("SELECT * FROM students WHERE STUDID='"+
    studid+"' or FNAME='"+
    vards+"' or LNAME='"+
    uzvards+"' or ADDRESS='"+
    adrese+"' or PHONE='"+
    telefons+"' ")
    
    try:
        rezultats = kursors.fetchall()

        for numurs in range(0,5):
            iestatitVr(rezultats[0][numurs],(numurs+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Kļūda", "Nav atrasts neviens dati")

def atjauninat():
    atlasitaisStudid = ""

    try:
        atlasitais_viens = mans_koks.selection()[0]
        atlasitaisStudid = str(mans_koks.item(atlasitais_viens)['values'][0])
    except:
        messagebox.showinfo("Kļūda", "Lūdzu, atlasiet datu rindu")

    studid = str(studidIevade.get())
    vards = str(vardsIevade.get())
    uzvards = str(uzvardsIevade.get())
    adrese = str(adreseIevade.get())
    telefons = str(telefonsIevade.get())

    if (studid == "" or studid == " ") or (vards == "" or vards == " ") or (uzvards == "" or uzvards == " ") or (adrese == "" or adrese == " ") or (telefons == "" or telefons == " "):
        messagebox.showinfo("Kļūda", "Lūdzu, aizpildiet tukšo ievades lauku")
        return
    else:
        try:
            conn = savienojums()
            kursors = conn.cursor()
            kursors.execute("UPDATE students SET STUDID='"+
            studid+"', FNAME='"+
            vards+"', LNAME='"+
            uzvards+"', ADDRESS='"+
            adrese+"', PHONE='"+
            telefons+"' WHERE STUDID='"+
            atlasitaisStudid+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Kļūda", "Studenta ID jau eksistē")
            return

    atjaunotTabulu()

etikete = Label(sakne, text="Studentu Reģistrācijas Sistēma (CRUD MATRICA)", font=('Arial Bold', 30))
etikete.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

studidEtiq = Label(sakne, text="Stud ID", font=('Arial', 15))
vardsEtiq = Label(sakne, text="Vārds", font=('Arial', 15))
uzvardsEtiq = Label(sakne, text="Uzvārds", font=('Arial', 15))
adreseEtiq = Label(sakne, text="Adrese", font=('Arial', 15))
telefonsEtiq = Label(sakne, text="Telefons", font=('Arial', 15))

studidEtiq.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
vardsEtiq.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
uzvardsEtiq.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
adreseEtiq.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
telefonsEtiq.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

studidIevade = Entry(sakne, width=55, bd=5, font=('Arial', 15), textvariable = ph1)
vardsIevade = Entry(sakne, width=55, bd=5, font=('Arial', 15), textvariable = ph2)
uzvardsIevade = Entry(sakne, width=55, bd=5, font=('Arial', 15), textvariable = ph3)
adreseIevade = Entry(sakne, width=55, bd=5, font=('Arial', 15), textvariable = ph4)
telefonsIevade = Entry(sakne, width=55, bd=5, font=('Arial', 15), textvariable = ph5)

studidIevade.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
vardsIevade.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
uzvardsIevade.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
adreseIevade.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
telefonsIevade.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

pievienotBtn = Button(
    sakne, text="Pievienot", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84F894", command=pievienot)
atjauninatBtn = Button(
    sakne, text="Atjaunināt", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84E8F8", command=atjauninat)
dzestBtn = Button(
    sakne, text="Dzēst", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#FF9999", command=dzest)
mekletBtn = Button(
    sakne, text="Meklēt", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F4FE82", command=meklet)
resetetBtn = Button(
    sakne, text="Atiestatīt", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F398FF", command=resetet)
atlasitBtn = Button(
    sakne, text="Atlasīt", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#EEEEEE", command=atlasit)

pievienotBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
atjauninatBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
dzestBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
mekletBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
resetetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
atlasitBtn.grid(row=13, column=5, columnspan=1, rowspan=2)

stils = ttk.Style()
stils.configure("Treeview.Heading", font=('Arial Bold', 15))

mans_koks['columns'] = ("Stud ID","Vārds","Uzvārds","Adrese","Telefons")

mans_koks.column("#0", width=0, stretch=NO)
mans_koks.column("Stud ID", anchor=W, width=170)
mans_koks.column("Vārds", anchor=W, width=150)
mans_koks.column("Uzvārds", anchor=W, width=150)
mans_koks.column("Adrese", anchor=W, width=165)
mans_koks.column("Telefons", anchor=W, width=150)

mans_koks.heading("Stud ID", text="Studenta ID", anchor=W)
mans_koks.heading("Vārds", text="Vārds", anchor=W)
mans_koks.heading("Uzvārds", text="Uzvārds", anchor=W)
mans_koks.heading("Adrese", text="Adrese", anchor=W)
mans_koks.heading("Telefons", text="Telefons", anchor=W)

atjaunotTabulu()

sakne.mainloop()
