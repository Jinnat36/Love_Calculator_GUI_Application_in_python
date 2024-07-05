# The tkinter  module  is import here.
from tkinter import *

# The random module is import here.
import random

# To create main window.
root=Tk()

# set geometry
root.geometry('300x200')

# This is title
root.title("Love Calculator GUI application in Python")

# Fonts
f=("Comic Sans MS",10,"bold")
font_for_names=("Times",10,"bold")

# It is main function ,which is calculate love % .
def love_calculator():
    st='0123456789'
    d=2
    temp="".join(random.sample(st,d))
    result_label.config(text=temp+"%")

# It is heading part.
heading=Label(root,text="\U0001F970 LOVE CALCULATOR \U0001F970",fg='red',font=f)
heading.pack()

# Your name part .
f_name=Label(root,text="YOUR NAME :",font=font_for_names,)
f_name.pack()
name1=Entry(root,)
name1.pack()

# partner name part
l_name=Label(root,text="PARTNER'S NAME :",font=font_for_names)
l_name.pack()
name2=Entry(root,)
name2.pack()

# Calculate button part
b=Button(root,text="Calculate Love %",command=love_calculator,background="red")
b.pack(pady=10)

# Here ,display the outpur
result_label=Label(root,text="")
result_label.pack()

# Application is ready to run.
root.mainloop()
