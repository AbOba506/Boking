# библиотеки
from tkinter import *
from tkinter import messagebox
import re
import tkinter as tk

# главное окно приложения
window = Tk()
# заголовок окна
window.title('Авторизация')
# размер окна
window.geometry('450x230')
# менять размер
window.resizable(False, False)

# шрифты и отступы
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

# кнопка Войти
def clicked():
    output=open('logins.txt','a')
    # логин и пароль
    username = username_entry.get()
    password = password_entry.get()
    flag = 0
    while True:
        if (len(password)<3):
            flag = -1
            messagebox.showerror('Ошибка','B пароле должно быть не менее 3 трёх символов')
            break
        elif (len(password)>20):
            flag = -1
            messagebox.showerror('Ошибка','B пароле должно быть не более 20 символов')
            break
        elif not re.search("[a-z]", password):
            flag = -1
            messagebox.showerror('Ошибка','В пароле нет строчных латинских букв')
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            messagebox.showerror('Ошибка','В пароле нет заглавных латинских букв')
            break
        elif not re.search("[0-9]", password):
            flag = -1
            messagebox.showerror('Ошибка','В пароле нет цифр')
            break
        elif re.search("\s" , password):
            flag = -1
            messagebox.showerror('Ошибка','В пароле есть пробел')
            break
        elif (len(username)<=2):
            flag = -1
            messagebox.showerror('Ошибка','B логине должно быть не менее 3 трёх символов')
            break
        elif (len(username)>=21):
            flag = -1
            messagebox.showerror('Ошибка','B логине должно быть не более 20 символов')
            break
        elif not re.search("[a-z]", username):
            flag = -1
            messagebox.showerror('Ошибка','В логине нет строчных латинских букв')
            break
        elif not re.search("[A-Z]", username):
            flag = -1
            messagebox.showerror('Ошибка','В логине нет заглавных латинских букв')
            break
        elif re.search("[0-9]", username):
            flag = -1
            messagebox.showerror('Ошибка','В логине не должны быть цифры')
            break
        elif re.search("\s" , username):
            flag = -1
            messagebox.showerror('Ошибка','В логине не должно быть пробелов')
            break
        else:
            flag = 0
            s = ("Login: "+username+' '+"Password: "+password+"\n")
            output.write(s)
            output.close()
            window.destroy()
            break
    
        






# настройка
main_label = Label(window, text='Регистрация', font=font_header, justify=CENTER, **header_padding)
main_label.pack()

# метка для логина
username_label = Label(window, text='Имя пользователя', font=label_font , **base_padding)
username_label.pack()

# логин
username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

# метка пароля
password_label = Label(window, text='Пароль', font=label_font , **base_padding)
password_label.pack()

# пароль
password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry, show='*')
password_entry.pack()

# кнопка Войти
send_btn = Button(window, text='Войти', command=clicked)
send_btn.pack(**base_padding)


# главный цикл
window.mainloop()
