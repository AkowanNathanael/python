# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from tkinter import *
window = Tk()
window.title(" my app calculate your age ")
window.wm_iconbitmap("nat.ico")
window.geometry("1000x580")

"""
All functions are written here 
"""
def answer():
    try:

        current_year = int(current_yearE.get())
        current_birthyr = int(current_yearofbith_E.get())
        global answerB
        answerB = current_year -current_birthyr
        display_label = Label(window, text=answerB)
        display_label.grid(row=4, column=0)
    except ZeroDivisionError:
        print(" 0 cannot be used here ")
    except ValueError:
        warning = " check to see whether  you entered alphabet \n  check to see whether you entered no value "
        lbl = Label(window, text=warning)
        lbl.grid(row=5, column=2)




#Tittle of program
title_label = Label(window, font=("AriaBold", 20), text=" A program to calculate your age " )
title_label.grid(column=0 , row= 0)

#coding of Entry Curent Year
lbl_text=Label(window, text="Enter Curent year")
lbl_text.grid(column=0, row=1)

current_yearE = Entry(window, width=40, background="yellow", foreground="black")
current_yearE.grid(column=1, row=1)


#Coding of entry year of birth
lbl_text2 = Label(window, text=" Enter  year of birth ")
lbl_text2.grid(column=0, row=2)

current_yearofbith_E = Entry(window, width=40, background="yellow", foreground="black")
current_yearofbith_E.grid(column=1, row=2)

#Display answer
display_answer_button = Button(window, text=" Display answer", command=answer)
display_answer_button.grid(row=3, column=0)








window.mainloop()
