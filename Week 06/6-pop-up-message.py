from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Message')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

# create a function to display pop-up message
def popup():
	response = messagebox.showinfo("Hello Wrold!", "I'm Taimur.")
	Label(root, text=response).pack()

Button(root, text="Popup", command=popup).pack()

mainloop()
