from tkinter import *

main = Tk()
main.title("Basic Calculator")
height = 500
width = 500

screen_height = main.winfo_screenheight()
screen_width = main.winfo_screenwidth()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

main.geometry("%dx%d+%d+%d" % (width, height, x, y))
main.resizable(0, 0)

# ==================== FRAMES ==========================

Display = Frame(main, width=500, height=80, bd=4, relief=RAISED)
Display.pack(side=TOP)

Entry_number = Frame(main, width=300, height=420, bd=5, relief=RAISED)
Entry_number.pack(side=LEFT)

Entry_operation = Frame(main, width=200, height=420, bd=5, relief=RAISED)
Entry_operation.pack(side=RIGHT)

# ===================== WIDGETS =========================

display_number = Label(Display, text="YAWA", font=("arial", 20))
display_number.pack(side=RIGHT)


Enter_number = Entry(Entry_number, bd=5, width=50, textvariable=display_number)
Enter_number.pack()






mainloop()