import tkinter as tk

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print("Empty entry")

def delete_name():
    name.delete(0, 'end')

def delete_password():
    password.delete(0, 'end')

win = tk.Tk()
h = 600
w = 500
win.geometry(f"{h}x{w}+350+40")
photo = tk.PhotoImage(file='photo.png')
win.iconphoto(False, photo)
win.title("Система Бронирования")
win.resizable(False, False)

#Главные кнопки
# btn1 = tk.Button(win, text='Главная', font=('Arial', 15, 'bold'), )
# btn1.grid(row=0, column=0)
# btn2 = tk.Button(win, text='Личный кабинет', font=('Arial', 15, 'bold'), )
# btn2.grid(row=0, column=1)
# btn3 = tk.Button(win, text='Ассортимент', font=('Arial', 15, 'bold'), )
# btn3.grid(row=0, column=2)

#Вход
label_1 = tk.Label(win, text='Вход')
label_1.grid(row=0, column=0)
#Логин и пароль
tk.Label(win, text='Логин').grid(row=1, column=0, stick='w')
tk.Label(win, text='Пароль').grid(row=2, column=0, stick='w')
name = tk.Entry(win)
password = tk.Entry(win, show='*')
name.grid(row=1, column=1)
password.grid(row=2, column=1)


#кнопки delete
tk.Button(win, text='delete', command=delete_name).grid(row=1, column=2, stick='we')
tk.Button(win, text='delete', command=delete_password).grid(row=2, column=2, stick='we')


win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)


win.mainloop()

