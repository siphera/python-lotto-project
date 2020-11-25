# Siphenkosi Salman ==> Class 1

# Imports
from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox


class Lotto:
    def __init__(self, master):
        self.master = master
        self.master.title('Lotto Machine: Siphenkosi Salman')
        self.master.geometry("740x500")
        self.master.resizable(False, False)
        self.style = ttk.Style()
        self.style.configure('My.TSpinbox', arrowsize=25)

        # Player details
        self.name_lbl = Label(master, text="Player name:")
        self.name_lbl.place(x=10, y=30)

        self.name_entry = Entry(master)
        self.name_entry.place(x=110, y=30)

        self.number_lbl = Label(master, text="Player Number:")
        self.number_lbl.place(x=350, y=30)

        self.number_entry = Entry(master)
        self.number_entry.place(x=470, y=30)

        # My number entries
        self.en1 = ttk.Spinbox(master, style='My.TSpinbox', from_=1, to=49, width="2", font=("arial", 40, 'bold'),
                               state='readonly')
        self.en1.place(x=10, y=100)
        self.en2 = ttk.Spinbox(master, style='My.TSpinbox', from_=1, to=49, width="2", font=("arial", 40, 'bold'),
                               state='readonly')
        self.en2.place(x=130, y=100)
        self.en3 = ttk.Spinbox(master, style='My.TSpinbox', from_=1, to=49, width="2", font=("arial", 40, 'bold'),
                               state='readonly')
        self.en3.place(x=250, y=100)
        self.en4 = ttk.Spinbox(master, style='My.TSpinbox', from_=1, to=49, width="2", font=("arial", 40, 'bold'),
                               state='readonly')
        self.en4.place(x=370, y=100)
        self.en5 = ttk.Spinbox(master, style='My.TSpinbox', from_=1, to=49, width="2", font=("arial", 40, 'bold'),
                               state='readonly')
        self.en5.place(x=490, y=100)
        self.en6 = ttk.Spinbox(master, style='My.TSpinbox', from_=1, to=49, width="2", font=("arial", 40, 'bold'),
                               state='readonly')
        self.en6.place(x=610, y=100)

        # Randomise button
        self.r_btn = Button(master, text="randomise", fg="white", bg="green", command=self.get_numbers)
        self.r_btn.place(x=320, y=280)

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

        # Exit button
        self.exit_btn = Button(master, text="Exit", bg="red", fg="white", command=self.exit)
        self.exit_btn.place(x=340, y=460)

    # Function to get the numbers from user and convert them to a list
    def get_numbers(self):
        try:
            self.user_list = []
            self.user_list.append(int(self.en1.get()))
            self.user_list.append(int(self.en2.get()))
            self.user_list.append(int(self.en3.get()))
            self.user_list.append(int(self.en4.get()))
            self.user_list.append(int(self.en5.get()))
            self.user_list.append(int(self.en6.get()))
            self.user_list.sort()
            print('user: ', self.user_list)

        except ValueError:
            messagebox.showwarning('Fill all inputs', 'Please make sure that you entered 6 numbers')
        # Generating the random numbers and sorting them in ascending order
        self.r_num = random.sample(range(1, 49), 6)
        self.r_num.sort()
        print('random: ', self.r_num)

        if len(self.user_list) != len(set(self.user_list)):
            self.message_box = messagebox.showerror('Input Error', 'Make sure you do not repeat inputs')

        else:
            try:
                self.r0.config(text=self.r_num[0])
                self.r1.config(text=self.r_num[1])
                self.r2.config(text=self.r_num[2])
                self.r3.config(text=self.r_num[3])
                self.r4.config(text=self.r_num[4])
                self.r5.config(text=self.r_num[5])

                # Compare the two lists and filter the numbers that match
                self.res = list(set(self.user_list).intersection(self.r_num))
                print("matching are: ", self.res)

                self.file = open('lotto_storage.txt', 'a')
                self.player_name = self.name_entry.get()
                self.player_number = self.number_entry.get()

                if len(self.res) == 6:
                    messagebox.showinfo('Winner', f'Congratulations {self.player_name} you have won R10, 000 000.00')
                    self.file.write(f'{self.player_name}: won R10, 000 000.00 \n')
                    self.file.close()
                elif len(self.res) == 5:
                    messagebox.showinfo('Winner', f'Congratulations {self.player_name} you have won R8,584.00')
                    self.file.write(f'{self.player_name}: won R8,584.00 \n')
                    self.file.close()
                elif len(self.res) == 4:
                    messagebox.showinfo('Winner', f'Congratulations {self.player_name} you have won R2,384.00')
                    self.file.write(f'{self.player_name}: won R2,384.00 \n')
                    self.file.close()
                elif len(self.res) == 3:
                    messagebox.showinfo('Winner', f'Congratulations {self.player_name} you have won R100.50')
                    self.file.write(f'{self.player_name}: won R100.50 \n')
                    self.file.close()
                elif len(self.res) == 2:
                    messagebox.showinfo('Winner', f'Congratulations {self.player_name} you have won R20.00')
                    self.file.write(f'{self.player_name}: won R20.00 \n')
                    self.file.close()
                elif len(self.res) < 2:
                    messagebox.showinfo('You lose', 'Try again next time')
                    self.file.write(f'{self.player_name}: Lost \n')
                    self.file.close()

            except ValueError:
                messagebox.showwarning('Fill all inputs',
                                                          'Please make sure that you entered 6 numbers')

    # Method for the exit Button
    def exit(self):
        self.message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application')
        if self.message_box == 'yes':
            self.master.destroy()
        else:
            pass


root = Tk()
app = Lotto(root)
root.mainloop()
