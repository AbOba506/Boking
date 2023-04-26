# библиотеки
from tkinter import *
from tkinter import messagebox
import re
import tkinter as tk

# шрифты и отступы
font_header = ('Arial', 15)
font_text = ('Arial', 10)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

def main():
    # Функция перехода в главную страницу
    def main_page():
        win.destroy()
        # функция выхода на домашнюю страницу
        def exit_main():
            window_main_page.destroy()
            main()
        # главное окно приложения
        window_main_page = Tk()
        # заголовок окна
        window_main_page.title('Главная')
        # размер окна
        window_main_page.geometry('450x230+400+150')
        # менять размер
        window_main_page.resizable(False, False)

        # настройка
        lk_label = Label(window_main_page, text='Главная страница', font=font_header, justify=CENTER, **header_padding)
        lk_label.grid(row=0, column=1)

        exit_main_menu = Button(window_main_page, text='Выйти', command=exit_main, borderwidth=5, width=10)
        exit_main_menu.grid(row=0, column=2)
        window_main_page.grid_columnconfigure(0, minsize=100)
        window_main_page.grid_columnconfigure(1, minsize=250)
        # главный цикл
        window_main_page.mainloop()

    # Функция перехода в лк
    def lk():
        # Отдельное окно оплаты
        def pay_def():
            window_lk.destroy()
            # функция выхода на домашнюю страницу
            def exit_pay():
                window_pay.destroy()
                main()
            # главное окно приложения
            window_pay = Tk()
            # заголовок окна
            window_pay.title('Оплата')
            # размер окна
            window_pay.geometry('450x230+400+150')
            # менять размер
            window_pay.resizable(False, False)

            # настройка
            pay_label = Label(window_pay, text='Оплата', font=font_header, justify=CENTER, **header_padding)
            pay_label.grid(row=0, column=1)
            pay_button_out = Button(window_pay, text='Выйти', command=exit_pay, borderwidth=5, width=10)
            pay_button_out.grid(row=0, column=2)
            window_pay.grid_columnconfigure(0, minsize=100)
            window_pay.grid_columnconfigure(1, minsize=250)


            # главный цикл
            window_pay.mainloop()

        # Отдельное окно Контактные данные
        def contact_data():
            window_lk.destroy()
            # функция выхода на домашнюю страницу
            def exit_cd():
                window_cd.destroy()
                main()
            # главное окно приложения
            window_cd = Tk()
            # заголовок окна
            window_cd.title('Контактные данные')
            # размер окна
            window_cd.geometry('450x230+400+150')
            # менять размер
            window_cd.resizable(False, False)

            # настройка
            cd_label = Label(window_cd, text='Контактные данные', font=font_header, justify=CENTER, **header_padding)
            cd_label.grid(row=0, column=1)
            cd_button_out = Button(window_cd, text='Выйти', command=exit_cd, borderwidth=5, width=10)
            cd_button_out.grid(row=0, column=2)
            window_cd.grid_columnconfigure(0, minsize=100)
            window_cd.grid_columnconfigure(1, minsize=250)

            # главный цикл
            window_cd.mainloop()

        # Отдельное окно Личные данные
        def personal_data():
            window_lk.destroy()
            # функция выхода на домашнюю страницу
            def exit_pd():
                window_pd.destroy()
                main()

            # главное окно приложения
            window_pd = Tk()
            # заголовок окна
            window_pd.title('Личные данные')
            # размер окна
            window_pd.geometry('450x330+400+150')
            # менять размер
            window_pd.resizable(False, False)
            myusername = open('myusername.txt', '+r')
            # настройка
            pd_label = Label(window_pd, text='Личные данные', font=font_header, justify=CENTER, **header_padding)
            pd_label.grid(row=0, column=1)
            # Имя
            pd_label1 = Label(window_pd, text='Имя', font=font_text, **header_padding)
            pd_label1.grid(row=1, column=0)
            login, password, name, age, driving_experience, criminal = myusername.readline().split()
            pd_label7 = Label(window_pd, text=name, font=font_text, **header_padding)
            pd_label7.grid(row=1, column=1)
            # Логин
            pd_label2 = Label(window_pd, text='Логин', font=font_text, **header_padding)
            pd_label2.grid(row=2, column=0)
            pd_label8 = Label(window_pd, text=login, font=font_text, **header_padding)
            pd_label8.grid(row=2, column=1)
            # Пароль
            pd_label3 = Label(window_pd, text='Пароль', font=font_text, justify=CENTER, **header_padding)
            pd_label3.grid(row=3, column=0)
            pd_label9 = Label(window_pd, text=password, font=font_text, **header_padding)
            pd_label9.grid(row=3, column=1)
            # Возраст
            pd_label4 = Label(window_pd, text='Возраст', font=font_text, justify=CENTER, **header_padding)
            pd_label4.grid(row=4, column=0)
            pd_label9 = Label(window_pd, text=age, font=font_text, **header_padding)
            pd_label9.grid(row=4, column=1)
            # Опыт вождения
            pd_label5 = Label(window_pd, text='Опыт вождения', font=font_text, justify=CENTER, **header_padding)
            pd_label5.grid(row=5, column=0)
            pd_label10 = Label(window_pd, text=driving_experience, font=font_text, **header_padding)
            pd_label10.grid(row=5, column=1)
            # судимость
            pd_label6 = Label(window_pd, text='судимость', font=font_text, justify=CENTER, **header_padding)
            pd_label6.grid(row=6, column=0)
            criminal = "Судимость"
            pd_label9 = Label(window_pd, text=criminal, font=font_text, **header_padding)
            pd_label9.grid(row=6, column=1)
            # Выйти
            pd_button_out = Button(window_pd, text='Выйти', command=exit_pd, borderwidth=5, width=10)
            pd_button_out.grid(row=0, column=2)
            window_pd.grid_rowconfigure(0, minsize=4)
            window_pd.grid_rowconfigure(1, minsize=4)
            window_pd.grid_columnconfigure(0, minsize=90)
            window_pd.grid_columnconfigure(1, minsize=220)
            myusername.close()
            # главный цикл
            window_pd.mainloop()

        win.destroy()
        # функция выхода на домашнюю страницу
        def exit_lk():
            window_lk.destroy()
            main()
        # главное окно приложения
        window_lk = Tk()
        # заголовок окна
        window_lk.title('Личный кабинет')
        # размер окна
        window_lk.geometry('450x230+400+150')
        # менять размер
        window_lk.resizable(False, False)

        # настройка
        lk_label = Label(window_lk, text='Личный кабинет', font=font_header, justify=CENTER, **header_padding)
        lk_label.grid(row=0, column=1)
        pd_button_out = Button(window_lk, text='Выйти', command=exit_lk, borderwidth=5, width=10)
        pd_button_out.grid(row=0, column=2)
        window_lk.grid_columnconfigure(0, minsize=70)
        window_lk.grid_columnconfigure(1, minsize=220)

        # кнопка Личные данные
        pers_data = Button(window_lk, text='Личные данные', command=personal_data, borderwidth=5, width=15)
        pers_data.grid(row=1, column=0)

        # кнопка Контактные данные
        cont_data= Button(window_lk, text='Контактные данные', command=contact_data, borderwidth=5, width=15)
        cont_data.grid(row=2, column=0)

        # кнопка Оплата
        pay = Button(window_lk, text='Оплата', command=pay_def, borderwidth=5, width=15)
        pay.grid(row=3, column=0)

        window_lk.grid_rowconfigure(2, minsize=60)

        # главный цикл
        window_lk.mainloop()
    

    # Домашняя страница
    win = tk.Tk()
    h = 600
    w = 400
    win.geometry(f"{h}x{w}+400+150")
    photo = tk.PhotoImage(file='photo.png')
    win.iconphoto(False, photo)
    win.title("Система Бронирования")
    win.resizable(False, False)

    # Главные кнопки
    btn1 = tk.Button(win, text='Главная', command=main_page, font=('Arial', 15, 'bold'), )
    btn1.grid(row=0, column=0)
    btn2 = tk.Button(win, text='Личный кабинет', command=lk, font=('Arial', 15, 'bold'), )
    btn2.grid(row=0, column=1)
    btn3 = tk.Button(win, text='Ассортимент', font=('Arial', 15, 'bold'), )
    btn3.grid(row=0, column=2)

    win.grid_columnconfigure(0, minsize=100)
    win.grid_columnconfigure(1, minsize=300)


    win.mainloop()

