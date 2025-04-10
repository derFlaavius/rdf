import mariadb
import tkinter as tk
from tkinter import ttk
import sys

# Connect to MariaDB Platform 
try: 
    conn = mariadb.connect( 
        user="marc", 
        password="marc", 
        host="localhost", 
        port=3306, 
        database="schlumpfshop3" 
    )

except mariadb.Error as e: 
    print(f"Error connecting to MariaDB Platform: {e}") 
    sys.exit(1)

con = conn.cursor()


# SQL Befehl wird ausgeführt, es dürfen auch Variablen aus Python aus vorherigen Eingaben verwendet werden. Rückgabe / Liste wird in dem Objekt "con" gespeichert.
con.execute(f"""SELECT artikel.Artikelname, artikel.Lagerbestand, lieferant.Lieferantenname
FROM artikel JOIN lieferant ON artikel.Lieferant = lieferant.ID_Lieferant
JOIN ort ON lieferant.ID_Ort = ort.ID_Ort
WHERE artikel.Lagerbestand < 18""") #Mindestalter dummy nur zum test

# Fenster erstellen
root = tk.Tk()
root.geometry("300x500")

# Label für Ausgabe
lb_ausgabe = ttk.Label(root, text="Hallo Welt")


for Artikelname, Preise, Lagerbestand in con:
    ausgabe = Artikelname, Preise, Lagerbestand
    lb_ausgabe(root, text=ausgabe)
    lb_ausgabe.pack()