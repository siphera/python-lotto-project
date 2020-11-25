# Siphenkosi Salman ==> Class 1

from tkinter import *
from tkinter import messagebox
from datetime import date


class Login:
    def __init__(self, master):
        self.master = master
        self.master.title('Lotto Machine: Siphenkosi Salman')
        self.master.geometry("740x500")
        self.master.resizable(False, False)

        self.lbl1 = Label(master, text="Enter your age", font=("arial", 20))
        self.lbl1.place(x=290, y=30)

        self.age_entry = Entry(master)
        self.age_entry.place(x=300, y=70)

        self.btn = Button(master, text="Play", font=("arial", 10), bg="skyblue", fg="white", command=self.login)
        self.btn.place(x=300, y=150)

    def login(self):

        try:
            self.age = int(self.age_entry.get())
            self.today = date.today()
            if 18 <= self.age <= 110 and type(self.age) == int:
                messagebox.showinfo("Successful", "Congatulations you qualify to play")
                file = open('lotto_storage.txt', 'w')
                file.write('File created on: ' + str(self.today) + "\n")
                file.close()
                self.master.destroy()
                import lotto
                lotto.Lotto
            elif type(self.age) == str:
                messagebox.showerror("Invalid Input", "Please make sure you enter valid input")
            else:
                messagebox.showwarning("Warning", "Sorry you can't play")
                self.age_entry.delete(0, END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please make sure you enter valid input")


root = Tk()
app = Login(root)
root.mainloop()
