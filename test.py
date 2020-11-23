'''import random
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
'''


'''def Diff(li1, li2):
    return (list(list(set(li1) - set(li2)) + list(set(li2) - set(li1))))


# Driver Code
li1 = [13, 6, 19, 12, 25, 18]
li2 = [13, 19, 20, 25, 34, 40]
print(Diff(li1, li2))'''

'''list1 = [1,2,3,4,5,6]
list2 = [3, 5, 7, 9]
res = list(set(list1).intersection(list2))
print(len(res))'''


'''def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result

print(common_elements(list1,list2))'''

from tkinter import *
from tkinter.messagebox import showerror

class GUI:
    def __init__(self, parent):
        self.iv = IntVar()
        self.sb = Spinbox(parent, from_=0, to=10, textvariable = self.iv)
        self.sb.pack()
        self.b1 = Button(parent, text="Confirm", command=self.validate)
        self.b1.pack()

    def validate(self):
        nb = self.sb.get()
        try:
            nb = int(nb)
            # do something with the number
            print(nb)
        except Exception:
            showerror('Error', 'Invalid content')


root = Tk()
root.geometry("800x600")
GUI = GUI(root)
root.title("Example")
root.mainloop()