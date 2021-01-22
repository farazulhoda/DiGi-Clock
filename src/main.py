# Digital Clock Using Python
# @farazul : imfaraz730@outlook.com

from tkinter import *
import time

win = Tk()
win.title("DiGi Clock : @MR-BiNARY")
win.geometry("350x200")

def digital_clock():
    time1 = time.strftime("%H:%M:%S")
    current_time.config(text=time1)
    current_time.after(720,digital_clock)

digi_clock = Label(win,text="DiGi Clock",font=("times new roman",35,'italic'),bg="white")
digi_clock.grid(row=0,column=0)

current_time = Label(win,font=("ariel",45,' bold italic'),bg="White")
current_time.grid(row=1,column=0,padx=60,pady=30)
digital_clock()



win.mainloop()

