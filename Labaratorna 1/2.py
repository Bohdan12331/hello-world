from tkinter import *
 

 
 
def click_button():
   return label1.pack()
 
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")
label1 = Label(text="Hello Python", fg="#eee", bg="#333")
label1.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)


btn2 = Button(text="Привіт", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn2.place(relx=.7, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)

 
btn = Button(text="Вихід", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=exit)
btn.place(relx=.3, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)
 
root.mainloop()
 

 
