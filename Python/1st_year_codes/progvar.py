from tkinter import  *
import sqlite3



window = Tk()
window.geometry("500x500")

conn = sqlite3.connect('r1g1db.db')
print("open database succesfully")

i =1
cursor = conn.execute("select dataentry, temp, light, device name from tblr1g1")
for row in cursor:
    print(str(i) + "Temp = ", row[1], "\n")
    i= i + 1


window.mainloop()