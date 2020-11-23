# Siphenkosi Salman

# Imports
from tkinter import *
import random
from tkinter import messagebox


class Lotto:
    def __init__(self, master):
        self.master = master
        self.master.title('Lotto Machine: Siphenkosi Salman')
        self.master.geometry("740x500")

        # My number entries
        self.en1 = Text(master, width=5, height=2, bd=8, relief=RIDGE, font=("arial", 25, 'bold'))
        self.en1.place(x=10, y=30)
        self.en2 = Text(master, width=5, height=2, bd=8, relief=RIDGE, font=("arial", 25, 'bold'))
        self.en2.place(x=130, y=30)
        self.en3 = Text(master, width=5, height=2, bd=8, relief=RIDGE, font=("arial", 25, 'bold'))
        self.en3.place(x=250, y=30)
        self.en4 = Text(master, width=5, height=2, bd=8, relief=RIDGE, font=("arial", 25, 'bold'))
        self.en4.place(x=370, y=30)
        self.en5 = Text(master, width=5, height=2, bd=8, relief=RIDGE, font=("arial", 25, 'bold'))
        self.en5.place(x=490, y=30)
        self.en6 = Text(master, width=5, height=2, bd=8, relief=RIDGE, font=("arial", 25, 'bold'))
        self.en6.place(x=610, y=30)

        # Randomise button
        self.r_btn = Button(master, text="randomise", command=self.r_numbers)
        self.r_btn.place(x=250, y=280)

        # Out put of random numbers
        self.r0 = Label(master, font=("arial", 25, "bold"), bg="yellow", width=5, height=2, bd=8, relief=RIDGE)
        self.r0.place(x=10, y=350)
        self.r1 = Label(master, font=("arial", 25, "bold"), bg="green", width=5, height=2, bd=8, relief=RIDGE)
        self.r1.place(x=130, y=350)
        self.r2 = Label(master, font=("arial", 25, "bold"), bg="blue", width=5, height=2, bd=8, relief=RIDGE)
        self.r2.place(x=250, y=350)
        self.r3 = Label(master, font=("arial", 25, "bold"), bg="tan", width=5, height=2, bd=8, relief=RIDGE)
        self.r3.place(x=370, y=350)
        self.r4 = Label(master, font=("arial", 25, "bold"), bg="magenta", width=5, height=2, bd=8, relief=RIDGE)
        self.r4.place(x=490, y=350)
        self.r5 = Label(master, font=("arial", 25, "bold"), bg="red", width=5, height=2, bd=8, relief=RIDGE)
        self.r5.place(x=610, y=350)

    def r_numbers(self):
        self.r_num = random.sample(range(1, 49), 6)
        self.r_num.sort()
        print(self.r_num)
        self.r0.config(text=self.r_num[0])
        self.r1.config(text=self.r_num[1])
        self.r2.config(text=self.r_num[2])
        self.r3.config(text=self.r_num[3])
        self.r4.config(text=self.r_num[4])
        self.r5.config(text=self.r_num[5])



root = Tk()
app = Lotto(root)
root.mainloop()
