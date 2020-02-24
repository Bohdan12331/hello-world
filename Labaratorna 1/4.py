from tkinter import *
 
def show_message():
    root.title(message.get())
 
root = Tk()
root.geometry("300x250")
 
message = StringVar()
 
message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")
 
message_button = Button(text="Змінити заголовок", command=show_message)
message_button.place(relx=.5, rely=.5, anchor="c")
 
root.mainloop()
