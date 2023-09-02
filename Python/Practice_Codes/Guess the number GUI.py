from tkinter import *
from random import *
from tkinter import messagebox

main = Tk()
main.title("Guess the number")
height = 600
width = 500
sh = main.winfo_screenheight()
sw = main.winfo_screenwidth()
x = (sw / 2) - (width / 2)
y = (sh / 2) - (height / 2)

main.geometry("%dx%d+%d+%d" % (width, height, x, y))
main.resizable(0, 0)

main.config(bg='#2FFFF1')

def confirm1():
    ran_num.config(text=random_compare)
    guess.set("")
    question = messagebox.askquestion("Loser!", "You lose! Do you want to play again?")

    if question == "yes":
        easy.withdraw()
        main.deiconify()
    else:
        exit()


def confirm():
    ran_num.config(text=random_compare)
    guess.set("")
    question = messagebox.askquestion("Congrats!", "You win! Do you want to play again?")

    if question == "yes":
        if assign == "easy":
            easy.withdraw()
            main.deiconify()
        elif assign == "medium":
            medium.withdraw()
            main.deiconify()
        elif assign == "hard":
            hard.withdraw()
            main.deiconify()
        elif assign == "custom":
            custom.withdraw()
            main.deiconify()
    else:
        exit()


def verify():
    global trials, guess, random_compare

    guess_compare = int(guess.get())
    random_compare = random_number

    if guess_compare < random_compare:
        guide.config(text="Higher")
        trials -= 1
        trial_label.config(text="Trials: " + str(trials))
    elif guess_compare > random_compare:
        guide.config(text="Lower")
        trials -= 1
        trial_label.config(text="Trials: " + str(trials))
    elif guess_compare == random_compare:
        confirm()

    if trials == 0:
        confirm1()


def easy_mode():
    global random_number, trials, guide, ran_num, trial_label, easy, guess, assign

    main.withdraw()
    easy = Toplevel()
    easy.title("Guess the Number (Easy Mode)")
    height = 480
    width = 500
    sh = easy.winfo_screenheight()
    sw = easy.winfo_screenwidth()
    x = (sw / 2) - (width / 2)
    y = (sh / 2) - (height / 2)

    easy.geometry("%dx%d+%d+%d" % (width, height, x, y))
    easy.config(bg='light green')
    easy.resizable(0, 0)

    trials = 3
    random_number = randint(1, 10)
    assign = "easy"

    # ==================== FRAMES ==========================

    title = Frame(easy, bg='light green', width=500, height=100, bd=5, relief=RIDGE)
    title.pack()
    widgets = Frame(easy, bg='light green', width=500, height=380, bd=5, relief=RIDGE)
    widgets.pack()

    # ==================== WIDGETS =========================

    Label(title, fg='white', bg='light green', text="Guess the number", font=('arial', 30, 'bold'), width=500).pack(
        pady=10)
    Label(title, fg='white', bg='light green', text="Easy Mode", font=('arial', 23, 'bold'), width=500).pack()

    Label(widgets, fg='white', bg='light green', text="1 - 10", font=('arial', 25, 'bold')).pack()

    ran_num = Label(widgets, fg='white', bg='light green', text="?", font=('arial', 40, 'bold'), width=500)
    ran_num.pack(pady=10)


    guide = Label(widgets, font=('arial', 15), bg='light green')
    guide.pack()
    trial_label = Label(widgets, text="Trials: " + str(trials), fg='white', bg='light green',
                        font=('arial', 20, 'bold'))
    trial_label.place(y=10, x=350)
    guess_entry = Entry(widgets, width=10, font=('arial', 30), justify=CENTER, textvariable=guess)
    guess_entry.pack(pady=20)
    guess_button = Button(widgets, bd=5, text="   Guess   ", font=('arial', 20, 'bold'), command=verify)
    guess_button.pack(pady=20)


def medium_mode():
    global random_number, trials, guide, ran_num, trial_label, medium, guess, assign

    main.withdraw()
    medium = Toplevel()
    medium.title("Guess the Number (Medium Mode)")
    height = 480
    width = 500
    sh = medium.winfo_screenheight()
    sw = medium.winfo_screenwidth()
    x = (sw / 2) - (width / 2)
    y = (sh / 2) - (height / 2)

    medium.geometry("%dx%d+%d+%d" % (width, height, x, y))
    medium.config(bg='light green')
    medium.resizable(0, 0)

    trials = 6
    random_number = randint(1, 20)
    assign = "medium"

    # ==================== FRAMES ==========================

    title = Frame(medium, bg='light blue', width=500, height=100, bd=5, relief=RIDGE)
    title.pack()
    widgets = Frame(medium, bg='light blue', width=500, height=380, bd=5, relief=RIDGE)
    widgets.pack()

    # ==================== WIDGETS =======================

    Label(title, fg='white', bg='light blue', text="Guess the number", font=('arial', 30, 'bold'), width=500).pack(
        pady=10)
    Label(title, fg='white', bg='light blue', text="Medium Mode", font=('arial', 23, 'bold'), width=500).pack()

    Label(widgets, fg='white', bg='light blue', text="1 - 20", font=('arial', 25, 'bold')).pack()

    ran_num = Label(widgets, fg='white', bg='light blue', text="?", font=('arial', 40, 'bold'), width=500)
    ran_num.pack(pady=10)

    guide = Label(widgets, font=('arial', 15), bg='light blue')
    guide.pack()
    trial_label = Label(widgets, text="Trials: " + str(trials), fg='white', bg='light blue',
                        font=('arial', 20, 'bold'))
    trial_label.place(y=10, x=350)
    guess_entry = Entry(widgets, width=10, font=('arial', 30), justify=CENTER, textvariable=guess)
    guess_entry.pack(pady=20)
    guess_button = Button(widgets, bd=5, text="   Guess   ", font=('arial', 20, 'bold'), command=verify)
    guess_button.pack(pady=20)


def hard_mode():
    global random_number, trials, guide, ran_num, trial_label, hard, guess, assign

    main.withdraw()
    hard = Toplevel()
    hard.title("Guess the Number (Hard Mode)")
    height = 480
    width = 500
    sh = hard.winfo_screenheight()
    sw = hard.winfo_screenwidth()

    x = (sw / 2) - (width / 2)
    y = (sh / 2) - (width / 2)

    hard.geometry("%dx%d+%d+%d" % (width, height, x, y))
    hard.resizable(0, 0)

    trials = 10
    random_number = randint(1, 40)
    assign = "hard"

    # ==================== FRAMES ==========================

    title = Frame(hard, bg='#F94E62', width=500, height=100, bd=5, relief=RIDGE)
    title.pack()
    widgets = Frame(hard, bg='#F94E62', width=500, height=380, bd=5, relief=RIDGE)
    widgets.pack()

    # ==================== WIDGETS =======================

    Label(title, fg='white', bg='#F94E62', text="Guess the number", font=('arial', 30, 'bold'), width=500).pack(
        pady=10)
    Label(title, fg='white', bg='#F94E62', text="Medium Mode", font=('arial', 23, 'bold'), width=500).pack()

    Label(widgets, fg='white', bg='#F94E62', text="1 - 40", font=('arial', 25, 'bold')).pack()

    ran_num = Label(widgets, fg='white', bg='#F94E62', text="?", font=('arial', 40, 'bold'), width=500)
    ran_num.pack(pady=10)

    guide = Label(widgets, font=('arial', 15), bg='#F94E62')
    guide.pack()
    trial_label = Label(widgets, text="Trials: " + str(trials), fg='white', bg='#F94E62',
                        font=('arial', 20, 'bold'))
    trial_label.place(y=10, x=350)
    guess_entry = Entry(widgets, width=10, font=('arial', 30), justify=CENTER, textvariable=guess)
    guess_entry.pack(pady=20)
    guess_button = Button(widgets, bd=5, text="   Guess   ", font=('arial', 20, 'bold'), command=verify)
    guess_button.pack(pady=20)

def custom_mode():
    global custom, trials, random_number, trials, guide, ran_num, trial_label, guess, assign, trial_range

    main.withdraw()
    edit.withdraw()
    custom = Toplevel()
    custom.title("Guess the Number (Custom Mode)")

    height = 480
    width = 500
    sh = custom.winfo_screenheight()
    sw = custom.winfo_screenwidth()

    x = (sw / 2) - (width / 2)
    y = (sh / 2) - (width / 2)

    custom.geometry("%dx%d+%d+%d" % (width, height, x, y))
    custom.resizable(0, 0)
    custom.config(bg='#FFD600')

    trials = int(trial_range.get())
    random_number = randint(1, range.get())
    assign = 'custom'

    # ==================== FRAMES ==========================

    title = Frame(custom, bg='#FFD600', width=500, height=100, bd=5, relief=RIDGE)
    title.pack()
    widgets = Frame(custom, bg='#FFD600', width=500, height=380, bd=5, relief=RIDGE)
    widgets.pack()

    # ==================== WIDGETS ==========================

    Label(title, fg='white', bg='#FFD600', text="Guess the number", font=('arial', 30, 'bold'), width=500).pack(
        pady=10)
    Label(title, fg='white', bg='#FFD600', text="Medium Mode", font=('arial', 23, 'bold'), width=500).pack()

    Label(widgets, fg='white', bg='#FFD600', text="1 - " + str(range.get()), font=('arial', 25, 'bold')).pack()

    ran_num = Label(widgets, fg='white', bg='#FFD600', text="?", font=('arial', 40, 'bold'), width=500)
    ran_num.pack(pady=10)

    guide = Label(widgets, font=('arial', 15), bg='#FFD600')
    guide.pack()
    trial_label = Label(widgets, text="Trials: " + str(trials), fg='white', bg='#FFD600',
                        font=('arial', 20, 'bold'))
    trial_label.place(y=10, x=350)
    guess_entry = Entry(widgets, width=10, font=('arial', 30), justify=CENTER, textvariable=guess)
    guess_entry.pack(pady=20)
    guess_button = Button(widgets, bd=5, text="   Guess   ", font=('arial', 20, 'bold'), command=verify)
    guess_button.pack(pady=20)


def custom_edit():
    global edit, range, trial_range

    main.withdraw()
    edit = Toplevel()
    edit.title("Custom Mode")
    height = 400
    width = 350
    sh = edit.winfo_screenheight()
    sw = edit.winfo_screenwidth()

    x = (sw / 2) - (width / 2)
    y = (sh / 2) - (height / 2)

    edit.geometry("%dx%d+%d+%d" % (width, height, x, y))
    edit.resizable(0, 0)

    edit.config(bg='#FFD600')

    Label(edit, text="Custom Mode", font=('arial', 27, 'bold'), bg='#FFD600').pack(pady=5)
    Label(edit, text="Range:", font=('arial', 23, 'bold'), bg='#FFD600').pack(pady=25)
    ran_lab = Label(edit, text='1 - ', font=('arial', 21, 'bold'), bg='#FFD600')
    ran_lab.place(x=130, y=135)
    ran_entry = Entry(edit, width=5, font=('arial', 15, 'bold'), justify=CENTER, textvariable=range)
    ran_entry.place(x=175, y=140)
    Label(edit, text='Trials:', font=('arial', 23, 'bold'), bg='#FFD600').pack(pady=45)
    trial_entry = Entry(edit, width=7, font=('arial', 15), justify=CENTER, textvariable=trial_range)
    trial_entry.place(x=135, y=250)

    Button(edit, width=7, text="Set", font=('arial', 18, 'bold'), command=custom_mode).place(x=120, y=320)


# =================== VARIABLES ========================

trials = IntVar()
trial_range = StringVar()
guess = StringVar()
assign = StringVar()
range = IntVar()

# =================== WIDGETS ===========================

Label(main, text="Guess the number", bg='#2FFFF1', font=('arial', 35, 'bold')).pack(pady=20)

Button(main, bd=3, bg='green', fg='white', text="        Easy        \n 1 - 10", font=('arial', 20, 'bold'),
       command=easy_mode).pack(pady=15)
Button(main, bd=3, bg='blue', fg='white', text="      Medium     \n 1 - 20", font=('arial', 20, 'bold'),
       command=medium_mode).pack(pady=10)
Button(main, bd=3, bg='red', fg='white', text="        Hard        \n 1 - 40", font=('arial', 20, 'bold'),
       command=hard_mode).pack(pady=10)
Button(main, bd=3, bg='#FFD600', fg='white', text="     Custom      ", font=('arial', 20, 'bold'), height=2, command=custom_edit).pack(pady=10)

mainloop()
