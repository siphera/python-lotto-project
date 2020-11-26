# Siphenkosi Salman ==> Class 1

from tkinter import *
from tkinter import messagebox
from datetime import date
from PIL import Image, ImageTk


class Login:
    def __init__(self, master):
        self.master = master
        self.master.title('Lotto Machine: Siphenkosi Salman')
        self.master.geometry("740x500")
        self.master.resizable(False, False)

        self.my_image = ImageTk.PhotoImage(Image.open("lotto.png"))
        self.image_label = Label(image=self.my_image, pady=45, padx=45)
        self.image_label.place(x=280, y=30)

        self.frm = LabelFrame(master)
        self.frm.place(x=50, y=150, width=645, height=300)

        self.lbl1 = Label(self.frm, text="Enter your age", font=("arial", 12))
        self.lbl1.pack()

        self.age_entry = Entry(self.frm)
        self.age_entry.pack()

        self.btn = Button(self.frm, text="Play", font=("arial", 10, "bold"), bg="skyblue", fg="white", padx=50, command=self.login)
        self.btn.place(x=250, y=70)

        # Exit button
        self.exit_btn = Button(self.frm, text="Exit", bg="red", fg="white", command=self.exit)
        self.exit_btn.place(x=340, y=150)

    def login(self):

        try:
            self.age = int(self.age_entry.get())
            self.today = date.today()
            if 18 <= self.age <= 110 and type(self.age) == int:
                messagebox.showinfo("Successful", "Congatulations you qualify to play")
                file = open('lotto_storage.txt', 'w')
                file.write('File created on: ' + str(self.today) + "\n \n")
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

        # Method for the exit Button
    def exit(self):
        self.message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application')
        if self.message_box == 'yes':
            self.master.destroy()
        else:
            pass


root = Tk()
app = Login(root)
root.mainloop()
