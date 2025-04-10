import mariadb
import tkinter as tk
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
    #sys.exit(1)

con = conn.cursor()


# SQL Befehl wird ausgeführt, es dürfen auch Variablen aus Python aus vorherigen Eingaben verwendet werden. Rückgabe / Liste wird in dem Objekt "con" gespeichert.
con.execute()

# Fenster erstellen
root = tk.Tk()
root.geometry("300x500")

# Buttons erstellen
bt_artikel = tk.Button(root, text="Artikel")
bt_preise = tk.Button(root, text="Preise")
bt_lbestand = tk.Button(root, text="Lagerbestand")
bt_lfrntname= tk.Button(root, text="Lieferantennamen")

# Label erstellen
lb_info = tk.Label(root, text="Bitte Option zur Ausgabe auswählen:")
lb_ausgabe = tk.Label(root, text="Ausgabe")

# Textbox erstellen
tb_insert = tk.Entry(root)


# Fenster mit Elementen füllen
lb_info.pack()
tb_insert.pack()
bt_artikel.pack()
bt_preise.pack()
bt_lbestand.pack()
bt_lfrntname.pack()
root.mainloop()