from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as msb
import os
window=Tk()
window.title(" editor")
window.wm_iconbitmap("nat.ico")
window.geometry("1000x580")

"""
function commands  for the file menu drop down
"""

def open():
    #the open function for the open menu widget has bugs to fix
    text_file = filedialog.askopenfilename(initialdir="c:/", title= "Open text", filetypes=(("Text files", "*.txt"),) )
    text_file =text_file[2:]
    text_file = open(text_file, "r+" )
    textfiles = text_file.read()

    text.insert(END, textfiles)
    text_file.close()
    """text.delete
    newfile = filedialog.askopenfilename()
    locationLabel =Label(frame, text=newfile)
    locationLabel.grid(row=0, column=2 )
    os.system(newfile)
    frame.config(text=newfile)
    text.update(newfile)
    frame.grid(row=1, column=0)"""


def save():
    savefile = open("sample.txt", "w")
    #the save function is not working here
    savefile.write(text.get(1.0, END))


def new():
    frame.destroy()
    newframe = Frame(window, )
    newframe.grid(row=1, column=0)
    text = Text(newframe, undo=True, font=("Helvetica", 16) )
    text.grid(row=2, column=0)

    redo = Button(newframe, text="Redo", command=text.edit_redo)
    redo.grid(row=0, column=0)

    undo = Button(newframe, text="Undo", command=text.edit_undo)
    undo.grid(row=0, column=1)



def aboutus():
    label =msb.showinfo("About us", "This is just a text  editor clone,\n that i created some how there are bugs i need you to help me fix ")




#defining and developing
#the menu items

my_menu =Menu(window)
window.config(menu=my_menu)

#file menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.destroy)

#Edit Menu
edit_menu =Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Open" , command=open)
edit_menu.add_separator()
edit_menu.add_command(label="save", command=save)

#About Menu
about_menu = Menu(my_menu)
my_menu.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="About Us", command=aboutus)



#main frame widget embeded onto the window  that is window=Tk()
frame = Frame(window, )
frame.grid(row=1, column=0 , )

#Text  widget embeded onto the  frame above with a default font family Helvetica and font size 16(normal font size) for the program
text = Text(frame,  undo=True, font=("Helvetica",16))
text.grid(row=2, column=0,)

#Redo button for the text editor
redo = Button(frame, text="Redo", command=text.edit_redo)
redo.grid(row=0, column=0)

#Undo button for the text editor
undo = Button(frame, text="Undo", command=text.edit_undo)
undo.grid(row=0, column=1)







window.mainloop()