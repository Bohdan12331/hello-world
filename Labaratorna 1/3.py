from tkinter import *
from random import *
 
 
def click_button():
    ran=randint(1,100)
    global clicks
    clicks = Label(text="Вам випало : "+str(ran), fg="#eee", bg="#333")
    clicks.place(relx=.5, rely=.2, anchor="c", height=30, width=130, bordermode=OUTSIDE)

 
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")




btn2 = Button(text="Привіт", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn2.place(relx=.7, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)

 
btn = Button(text="Вихід", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=exit)
btn.place(relx=.3, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)
 
root.mainloop()
 
