from tkinter import *

root= Tk()
root.title('Calculator')
root.configure(bg='#141414')



def button_click(number):
    #entry_bar.delete(0, END)
    current = entry_bar.get()
    entry_bar.delete(0, END)
    entry_bar.insert(0, str(current) + str(number))



def button_clear():
    entry_bar.delete(0, END)



def button_equal():
    second_number = entry_bar.get()
    entry_bar.delete(0, END)
    if math == 'addition':
        entry_bar.insert(0, f_num + int(second_number))
    elif math == 'minus':
        entry_bar.insert(0, f_num - int(second_number))
    elif math == 'times':
        entry_bar.insert(0, f_num * int(second_number))
    elif math == 'divide':
        entry_bar.insert(0, f_num / int(second_number))


def button_add():
    first_number = entry_bar.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    entry_bar.delete(0, END)



def button_minus():
    first_number = entry_bar.get()
    global f_num
    global math
    math = 'minus'
    f_num = int(first_number)
    entry_bar.delete(0, END)



def button_times():
    first_number = entry_bar.get()
    global f_num
    global math
    math = 'times'
    f_num = int(first_number)
    entry_bar.delete(0, END)
    



def button_divide():
    first_number = entry_bar.get()
    global f_num
    global math
    math = 'divide'
    f_num = int(first_number)
    entry_bar.delete(0, END)




entry_bar = Entry(root, width=35)
entry_bar.grid(row=0, column=0, columnspan=3, padx=10, pady=50)
entry_bar.configure(bg='#141414', fg='whitesmoke')


# Define buttons
button1 = Button(root, text=1, padx=40, pady=20, command=lambda: button_click(1), bg='black', fg='whitesmoke')
button2 = Button(root, text=2, padx=40, pady=20, command=lambda: button_click(2), bg='black', fg='whitesmoke')
button3 = Button(root, text=3, padx=40, pady=20, command=lambda: button_click(3), bg='black', fg='whitesmoke')
button4 = Button(root, text=4, padx=40, pady=20, command=lambda: button_click(4), bg='black', fg='whitesmoke')
button5 = Button(root, text=5, padx=40, pady=20, command=lambda: button_click(5), bg='black', fg='whitesmoke')
button6 = Button(root, text=6, padx=40, pady=20, command=lambda: button_click(6), bg='black', fg='whitesmoke')
button7 = Button(root, text=7, padx=40, pady=20, command=lambda: button_click(7), bg='black', fg='whitesmoke')
button8 = Button(root, text=8, padx=40, pady=20, command=lambda: button_click(8), bg='black', fg='whitesmoke')
button9 = Button(root, text=9, padx=40, pady=20, command=lambda: button_click(9), bg='black', fg='whitesmoke')
button0 = Button(root, text=0, padx=40, pady=20, command=lambda: button_click(0), bg='black', fg='whitesmoke')

button_add = Button(root, text='+', padx=39, pady=20, command= button_add, bg='#2c2a2a', fg='whitesmoke')
button_minus = Button(root, text='-', padx=39, pady=20, command= button_minus, bg='#2c2a2a', fg='whitesmoke')
button_divide = Button(root, text='/', padx=39, pady=20, command= button_divide, bg='#2c2a2a', fg='whitesmoke')
button_times = Button(root, text='*', padx=39, pady=20, command= button_times, bg='#2c2a2a', fg='whitesmoke')


button_equal = Button(root, text='=', padx=39, pady=50, command= button_equal, bg='#141414', fg='whitesmoke')
button_clear = Button(root, text='CLS', padx=82.5, pady=20, command= button_clear, bg='#141414', fg='whitesmoke')

# Slap buttons on the screen
button1.grid(row=3,column=2)
button2.grid(row=3,column=1)
button3.grid(row=3,column=0)

button4.grid(row=2,column=2)
button5.grid(row=2,column=1)
button6.grid(row=2,column=0)

button7.grid(row=1,column=2)
button8.grid(row=1,column=1)
button9.grid(row=1,column=0)

button0.grid(row=4,column=0)

button_add.grid(row=5,column=0)
button_divide.grid(row=5,column=1)
button_minus.grid(row=6,column=0)
button_times.grid(row=6, column=1)

button_equal.grid(rowspan=2,row=5,column=2)
button_clear.grid(columnspan=2,row=4,column=1)

root.mainloop()