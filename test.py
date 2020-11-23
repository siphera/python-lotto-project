import random
from tkinter import *

root = Tk()


lb = Label(root)
lb2 = Label(root)
r_number = random.sample(range(1, 49), 6)
r_number.sort()
print(r_number)
lb.config(text=r_number[0])
lb2.config(text=r_number[1])
#
# for x in r_number:
#     print(x)
#     lb.config(text=x)
lb.pack()
lb2.pack()
# from tkinter import *  # from tkinter import *
#
# lst = ['a', 'b', 'c', 'd']
#
# root = Tk()
# t = Text(root)
# for x in lst:
#     t.insert(END, x + '\n')
# t.pack()
root.mainloop()
