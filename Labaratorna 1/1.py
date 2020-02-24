from tkinter import *
 
 
 

 
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")
label1 = Label(text="Моя перша програма", fg="#eee", bg="#333")
label1.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)
label1.pack()
 
btn = Button(text="Закрити", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=exit)
btn.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)
 
root.mainloop()
 

 
