# библиотеки
from tkinter import *
from tkinter import messagebox
import re
import tkinter as tk
from PIL import Image, ImageTk

# шрифты и отступы
font_header = ('Arial', 15)
font_text = ('Arial', 10)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title('Система Бронирования')
        self.root.geometry('450x230+400+150')
        self.root.resizable=(False, False)
        self.photo = tk.PhotoImage(file='photo.png')
        self.root.iconphoto(False, self.photo)

        self.bron_label = Label(self.root, text='Бронирование', font=('Arial', 15, 'bold'), justify=CENTER, **header_padding)
        self.btn1 = tk.Button(self.root, text='Главная', command=self.main_page, font=('Arial', 15, 'bold'), borderwidth=5, width=15)
        self.btn2 = tk.Button(self.root, text='Личный кабинет', command=self.lk, font=('Arial', 15, 'bold'), borderwidth=5, width=15)
        self.btn3 = tk.Button(self.root, text='Ассортимент', command=self.def_assortiment,font=('Arial', 15, 'bold'), borderwidth=5, width=15)

    def draw_widjets(self):
        self.bron_label.grid(row=0, column=1)
        self.btn1.grid(row=1, column=0)
        self.btn2.grid(row=2, column=0)
        self.btn3.grid(row=3, column=0)
    
    def run(self):
        self.draw_widjets()
        self.root.mainloop()
    
    # Функция перехода в главную страницу
    def main_page(self):
        self.root.destroy()
        # функция выхода на домашнюю страницу
        def exit_main():
            window_main_page.destroy()
            main = Main()
            main.run()
        # главное окно приложения
        window_main_page = Tk()
        # заголовок окна
        window_main_page.title('Главная')
        # размер окна
        window_main_page.geometry('900x400+300+150')
        # менять размер
        window_main_page.resizable(False, False)

        # настройка
        lk_label = Label(window_main_page, text='Главная страница', font=font_header, justify=CENTER, **header_padding)
        lk_label.grid(row=0, column=1)
        lk_label = Label(window_main_page, text='Добро пожаловать в наше приложение для бронирования автомобилей!', font=font_header, justify=CENTER, **header_padding)
        lk_label.grid(row=1, column=1)
        lk_label = Label(window_main_page, text='В нашем приложении вы можете забронировать такие машины как:', font=font_header, justify=CENTER, **header_padding)
        lk_label.grid(row=2, column=1)
        lk_label = Label(window_main_page, text='Honda Civic, Porshe 911, Nissan Skyline, Toyota Supra, Toyota Trueno', font=font_header, justify=CENTER, **header_padding)
        lk_label.grid(row=3, column=1)
        exit_main_menu = Button(window_main_page, text='Выйти', command=exit_main, borderwidth=5, width=10)
        exit_main_menu.grid(row=0, column=2)

        window_main_page.grid_columnconfigure(0, minsize=100)
        window_main_page.grid_columnconfigure(1, minsize=250)
        # главный цикл
        window_main_page.mainloop()
    
    # Функция перехода в лк
    def lk(self):
        # Отдельное окно оплаты
        def pay_def():
            window_lk.destroy()
            # функция выхода на домашнюю страницу
            def exit_pay():
                window_pay.destroy()
                main = Main()
                main.run()
            # главное окно приложения
            window_pay = Tk()
            # заголовок окна
            window_pay.title('Оплата')
            # размер окна
            window_pay.geometry('450x230+400+150')
            # менять размер
            window_pay.resizable(False, False)

            myusername = open('myusername.txt', '+r')
            header_padding_1 = {'padx': 10, 'pady': 7}
            line = myusername.readline()
            username_in_file, password_in_file, name, age, driving_experience, criminal, phone, email, card = line.split()

            # настройка
            pay_label = Label(window_pay, text='Оплата', font=font_header, justify=CENTER, **header_padding)
            pay_label.grid(row=0, column=1)

            # метка номер карты
            card_label = Label(window_pay, text='Номер карты', font=('Arial', 12), **header_padding_1)
            card_label.grid(row=1, column=0)
            # номер карты
            card_entry = Label(window_pay, text=card, font=('Arial', 12), **header_padding_1)
            card_entry.grid(row=1, column=1)

            pay_button_out = Button(window_pay, text='Выйти', command=exit_pay, borderwidth=5, width=10)
            pay_button_out.grid(row=0, column=2)

            window_pay.grid_columnconfigure(0, minsize=80)
            window_pay.grid_columnconfigure(1, minsize=200)


            # главный цикл
            window_pay.mainloop()

        # Отдельное окно Контактные данные
        def contact_data():
            window_lk.destroy()
            # функция выхода на домашнюю страницу
            def exit_cd():
                window_cd.destroy()
                main = Main()
                main.run()
            # главное окно приложения
            window_cd = Tk()
            # заголовок окна
            window_cd.title('Контактные данные')
            # размер окна
            window_cd.geometry('450x230+400+150')
            # менять размер
            window_cd.resizable(False, False)
            myusername = open('myusername.txt', '+r')
            header_padding_1 = {'padx': 10, 'pady': 7}

            line = myusername.readline()
            username_in_file, password_in_file, name, age, driving_experience, criminal, phone, email, card = line.split() 

            # настройка
            cd_label = Label(window_cd, text='Контактные данные', font=font_header, justify=CENTER, **header_padding)
            cd_label.grid(row=0, column=1)
            cd_button_out = Button(window_cd, text='Выйти', command=exit_cd, borderwidth=5, width=10)
            cd_button_out.grid(row=0, column=2)

            # метка номер телефона
            phone_label = Label(window_cd, text='Номер телефона', font=('Arial', 12), **header_padding_1)
            phone_label.grid(row=1, column=0)

            # номер телефона
            phone_entry = Label(window_cd, text=phone, font=('Arial', 12), **header_padding_1)
            phone_entry.grid(row=1, column=1)

            # метка E-mail
            email_label = Label(window_cd, text='E-mail', font=('Arial', 12), **header_padding_1)
            email_label.grid(row=2, column=0)

            # E-mail
            email_entry = Label(window_cd, text=email, font=('Arial', 12), **header_padding_1)
            email_entry.grid(row=2, column=1)

            window_cd.grid_columnconfigure(0, minsize=80)
            window_cd.grid_columnconfigure(1, minsize=200)

            # главный цикл
            window_cd.mainloop()

        # Отдельное окно Личные данные
        def personal_data():
            window_lk.destroy()
            # функция выхода на домашнюю страницу
            def exit_pd():
                window_pd.destroy()
                main = Main()
                main.run()

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
            login, password, name, age, driving_experience, criminal, phone, email, card = myusername.readline().split()
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
            pd_label6 = Label(window_pd, text='Cудимость', font=font_text, justify=CENTER, **header_padding)
            pd_label6.grid(row=6, column=0)
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

        self.root.destroy()
        # функция выхода на домашнюю страницу
        def exit_lk():
            window_lk.destroy()
            main = Main()
            main.run()
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
    
    # Функция перехода в Ассортимент
    def def_assortiment(self):
        self.root.destroy()
        # функция выхода на домашнюю страницу
        def exit_asortiment():
            window_assortiment.destroy()
            main = Main()
            main.run()
        # главное окно приложения
        window_assortiment = Tk()
        # заголовок окна
        window_assortiment.title('Ассортимент')
        # размер окна
        window_assortiment.geometry('450x230+400+150')
        # менять размер
        window_assortiment.resizable(False, False)

        # настройка
        lk_label = Label(window_assortiment, text='Ассортимент', font=font_header, justify=CENTER, **header_padding)
        lk_label.place(x = 150, y = 10)

        exit_main_menu = Button(window_assortiment, text='Выйти', command=exit_asortiment, borderwidth=5, width=10)
        exit_main_menu.place(x = 335, y = 20)
        
        # функция перехода на Honda
        def honda():
            window_assortiment.destroy()
            def exit_honda():
                window_honda.destroy()
                main = Main()
                main.run()
            window_honda = Tk()
            window_honda.title('Honda')
            window_honda.geometry('350x230+400+150')
            window_honda.resizable(False, False)
            # настройка
            lk_label = Label(window_honda, text='Honda', font=font_header, justify=CENTER, **header_padding)
            lk_label.place(x = 120, y = 10)

            exit_main_menu = Button(window_honda, text='Выйти', command=exit_honda, borderwidth=5, width=10)
            exit_main_menu.place(x = 250, y = 20)
            
            def civic():
                window_honda.destroy()
                def exit_civic():
                    window_civic.destroy()
                    main = Main()
                    main.run()
                window_civic = Tk()
                window_civic.title('Honda Civic')
                window_civic.geometry('900x650+300+20')
                window_civic.resizable(False, False)
                # настройка
                honda_civic_label = Label(window_civic, text='Honda Civic', font=('Arial',20), justify=CENTER, **header_padding)
                honda_civic_label.place(x = 390, y = 10)
                exit_honda_civic = Button(window_civic, text='Выйти', command=exit_civic, borderwidth=5,font=('Arial',16), width=10)
                exit_honda_civic.place(x = 750, y = 20)
                civic_photo = Image.open("data\\civic.png")
                civic_photo = civic_photo.resize((440, 350), Image.ANTIALIAS)
                civic_photo = ImageTk.PhotoImage(civic_photo)
                civic_label = Label(image = civic_photo, borderwidth=0)
                civic_label.image = civic_photo
                civic_label.place(x = 240, y = 70)
                honda_civic_label = Label(window_civic, text='Производитель: Honda', font=font_header, justify=CENTER)
                honda_civic_label.place(x = 240, y = 420)
                honda_civic_label = Label(window_civic, text='Модель: Civic type R', font=font_header, justify=CENTER)
                honda_civic_label.place(x = 240, y = 450)
                honda_civic_label = Label(window_civic, text='Тип кузова: 5-и дверная', font=font_header, justify=CENTER)
                honda_civic_label.place(x = 240, y = 480)
                honda_civic_label = Label(window_civic, text='Компоновка: переднеприводная', font=font_header, justify=CENTER)
                honda_civic_label.place(x = 240, y = 510)
                honda_civic_label = Label(window_civic, text='Стоимость за час: 3500 рублей', font=font_header, justify=CENTER)
                honda_civic_label.place(x = 240, y = 540)
                def book_civic():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Honda Civic')
                book_honda_civic = Button(window_civic, text='Забронировать', command=book_civic, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_honda_civic.place(x = 350, y = 570)
                # главный цикл
                window_civic.mainloop()
            # Фото Civic
            civic_photo = Image.open("data\\civic.png")
            civic_photo = civic_photo.resize((80, 70), Image.ANTIALIAS)
            civic_photo = ImageTk.PhotoImage(civic_photo)
            civic_label = Button(image = civic_photo, borderwidth=0, command=civic)
            civic_label.image = civic_photo
            civic_label.place(x = 5, y = 70)

            civic_name = Label(window_honda, text='Honda Civic', font=('Arial',10), justify=CENTER, width=10)
            civic_name.place(x=5, y=140)
            
            def nsx():
                window_honda.destroy()
                def exit_nsx():
                    window_nsx.destroy()
                    main = Main()
                    main.run()
                window_nsx = Tk()
                window_nsx.title('Honda NSX')
                window_nsx.geometry('900x650+300+20')
                window_nsx.resizable(False, False)
                # настройка
                honda_nsx_label = Label(window_nsx, text='Honda NSX', font=('Arial',20), justify=CENTER, **header_padding)
                honda_nsx_label.place(x = 390, y = 10)
                exit_honda_nsx = Button(window_nsx, text='Выйти', command=exit_nsx, borderwidth=5,font=('Arial',16), width=10)
                exit_honda_nsx.place(x = 750, y = 20)
                nsx_photo = Image.open("data\\nsx.png")
                nsx_photo = nsx_photo.resize((440, 350), Image.ANTIALIAS)
                nsx_photo = ImageTk.PhotoImage(nsx_photo)
                nsx_label = Label(image = nsx_photo, borderwidth=0)
                nsx_label.image = nsx_photo
                nsx_label.place(x = 240, y = 70)
                honda_nsx_label = Label(window_nsx, text='Производитель: Honda', font=font_header, justify=CENTER)
                honda_nsx_label.place(x = 240, y = 420)
                honda_nsx_label = Label(window_nsx, text='Модель: NSX', font=font_header, justify=CENTER)
                honda_nsx_label.place(x = 240, y = 450)
                honda_nsx_label = Label(window_nsx, text='Тип кузова: 2-х дверная', font=font_header, justify=CENTER)
                honda_nsx_label.place(x = 240, y = 480)
                honda_nsx_label = Label(window_nsx, text='Компоновка: полноприводная', font=font_header, justify=CENTER)
                honda_nsx_label.place(x = 240, y = 510)
                honda_nsx_label = Label(window_nsx, text='Стоимость за час: 7000 рублей', font=font_header, justify=CENTER)
                honda_nsx_label.place(x = 240, y = 540)
                def book_nsx():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Honda NSX')
                book_honda_nsx = Button(window_nsx, text='Забронировать', command=book_nsx, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_honda_nsx.place(x = 350, y = 570)
                # главный цикл
                window_nsx.mainloop()
            # Фото NSX
            nsx_photo = Image.open("data\\nsx.png")
            nsx_photo = nsx_photo.resize((80, 70), Image.ANTIALIAS)
            nsx_photo = ImageTk.PhotoImage(nsx_photo)
            nsx_label = Button(image = nsx_photo, borderwidth=0, command=nsx)
            nsx_label.image = nsx_photo
            nsx_label.place(x = 90, y = 70)

            nsx_name = Label(window_honda, text='Honda NSX', font=('Arial',10), justify=CENTER, width=10)
            nsx_name.place(x=90, y=140)
            
            def s2000():
                window_honda.destroy()
                def exit_s2000():
                    window_s2000.destroy()
                    main = Main()
                    main.run()
                window_s2000 = Tk()
                window_s2000.title('Honda S2000')
                window_s2000.geometry('900x650+300+20')
                window_s2000.resizable(False, False)
                # настройка
                honda_s2000_label = Label(window_s2000, text='Honda S2000', font=('Arial',20), justify=CENTER, **header_padding)
                honda_s2000_label.place(x = 390, y = 10)
                exit_honda_s2000 = Button(window_s2000, text='Выйти', command=exit_s2000, borderwidth=5,font=('Arial',16), width=10)
                exit_honda_s2000.place(x = 750, y = 20)
                s2000_photo = Image.open("data\\s2000.png")
                s2000_photo = s2000_photo.resize((440, 350), Image.ANTIALIAS)
                s2000_photo = ImageTk.PhotoImage(s2000_photo)
                s2000_label = Label(image = s2000_photo, borderwidth=0)
                s2000_label.image = s2000_photo
                s2000_label.place(x = 240, y = 70)
                honda_s2000_label = Label(window_s2000, text='Производитель: Honda', font=font_header, justify=CENTER)
                honda_s2000_label.place(x = 240, y = 420)
                honda_s2000_label = Label(window_s2000, text='Модель: S2000', font=font_header, justify=CENTER)
                honda_s2000_label.place(x = 240, y = 450)
                honda_s2000_label = Label(window_s2000, text='Тип кузова: 2-х дверная', font=font_header, justify=CENTER)
                honda_s2000_label.place(x = 240, y = 480)
                honda_s2000_label = Label(window_s2000, text='Компоновка: заднеприводная', font=font_header, justify=CENTER)
                honda_s2000_label.place(x = 240, y = 510)
                honda_s2000_label = Label(window_s2000, text='Стоимость за час: 4000 рублей', font=font_header, justify=CENTER)
                honda_s2000_label.place(x = 240, y = 540)
                def book_s2000():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Honda S2000')
                book_honda_s2000 = Button(window_s2000, text='Забронировать', command=book_s2000, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_honda_s2000.place(x = 350, y = 570)
                # главный цикл
                window_s2000.mainloop()
            # Фото S2000
            s2000_photo = Image.open("data\\s2000.png")
            s2000_photo = s2000_photo.resize((80, 70), Image.ANTIALIAS)
            s2000_photo = ImageTk.PhotoImage(s2000_photo)
            s2000_label = Button(image = s2000_photo, borderwidth=0, command=s2000)
            s2000_label.image = s2000_photo
            s2000_label.place(x = 175, y = 70)

            s2000_name = Label(window_honda, text='Honda S2000', font=('Arial',10), justify=CENTER, width=10)
            s2000_name.place(x = 175, y = 140)
            
            def prelude():
                window_honda.destroy()
                def exit_prelude():
                    window_prelude.destroy()
                    main = Main()
                    main.run()
                window_prelude = Tk()
                window_prelude.title('Honda Prelude')
                window_prelude.geometry('900x650+300+20')
                window_prelude.resizable(False, False)
                # настройка
                honda_prelude_label = Label(window_prelude, text='Honda Prelude', font=('Arial',20), justify=CENTER, **header_padding)
                honda_prelude_label.place(x = 390, y = 10)
                exit_honda_prelude = Button(window_prelude, text='Выйти', command=exit_prelude, borderwidth=5,font=('Arial',16), width=10)
                exit_honda_prelude.place(x = 750, y = 20)
                prelude_photo = Image.open("data\\prelude.png")
                prelude_photo = prelude_photo.resize((440, 350), Image.ANTIALIAS)
                prelude_photo = ImageTk.PhotoImage(prelude_photo)
                prelude_label = Label(image = prelude_photo, borderwidth=0)
                prelude_label.image = prelude_photo
                prelude_label.place(x = 240, y = 70)
                honda_prelude_label = Label(window_prelude, text='Производитель: Honda', font=font_header, justify=CENTER)
                honda_prelude_label.place(x = 240, y = 420)
                honda_prelude_label = Label(window_prelude, text='Модель: Prelude', font=font_header, justify=CENTER)
                honda_prelude_label.place(x = 240, y = 450)
                honda_prelude_label = Label(window_prelude, text='Тип кузова: 2-х дверная', font=font_header, justify=CENTER)
                honda_prelude_label.place(x = 240, y = 480)
                honda_prelude_label = Label(window_prelude, text='Компоновка: заднеприводная', font=font_header, justify=CENTER)
                honda_prelude_label.place(x = 240, y = 510)
                honda_prelude_label = Label(window_prelude, text='Стоимость за час: 2500 рублей', font=font_header, justify=CENTER)
                honda_prelude_label.place(x = 240, y = 540)
                def book_prelude():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Honda Prelude')
                book_honda_prelude = Button(window_prelude, text='Забронировать', command=book_prelude, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_honda_prelude.place(x = 350, y = 570)
                # главный цикл
                window_prelude.mainloop()
            # Фото Prelude
            prelude_photo = Image.open("data\\prelude.png")
            prelude_photo = prelude_photo.resize((80, 70), Image.ANTIALIAS)
            prelude_photo = ImageTk.PhotoImage(prelude_photo)
            prelude_label = Button(image = prelude_photo, borderwidth=0, command=prelude)
            prelude_label.image = prelude_photo
            prelude_label.place(x = 260, y = 70)

            prelude_name = Label(window_honda, text='Honda Prelude', font=('Arial',10), justify=CENTER, width=10)
            prelude_name.place(x = 260, y = 140)
    
        # Фото Honda
        honda_photo = Image.open("data\\HondaLogo.png")
        honda_photo = honda_photo.resize((80, 70), Image.ANTIALIAS)
        honda_photo = ImageTk.PhotoImage(honda_photo)
        honda_label = Button(image = honda_photo, borderwidth=0, command=honda)
        honda_label.image = honda_photo
        honda_label.place(x = 5, y = 70)

        honda_name = Label(window_assortiment, text='Honda', font=('Arial',10), justify=CENTER, width=10)
        honda_name.place(x=5, y=140)
        
        def nissan():
            window_assortiment.destroy()
            def exit_nissan():
                window_nissan.destroy()
                main = Main()
                main.run()
            window_nissan = Tk()
            window_nissan.title('Nissan')
            window_nissan.geometry('350x230+400+150')
            window_nissan.resizable(False, False)
            # настройка
            lk_label = Label(window_nissan, text='Nissan', font=font_header, justify=CENTER, **header_padding)
            lk_label.place(x = 120, y = 10)

            exit_main_menu = Button(window_nissan, text='Выйти', command=exit_nissan, borderwidth=5, width=10)
            exit_main_menu.place(x = 250, y = 20)
            
            def stagea():
                window_nissan.destroy()
                def exit_stagea():
                    window_stagea.destroy()
                    main = Main()
                    main.run()
                window_stagea = Tk()
                window_stagea.title('Nissan Stagea')
                window_stagea.geometry('900x650+300+20')
                window_stagea.resizable(False, False)
                # настройка
                stagea_label = Label(window_stagea, text='Nissan Stagea', font=('Arial',20), justify=CENTER, **header_padding)
                stagea_label.place(x = 390, y = 10)
                exit_stagea = Button(window_stagea, text='Выйти', command=exit_stagea, borderwidth=5,font=('Arial',16), width=10)
                exit_stagea.place(x = 750, y = 20)
                stagea_photo = Image.open("data\\stagea.png")
                stagea_photo = stagea_photo.resize((440, 350), Image.ANTIALIAS)
                stagea_photo = ImageTk.PhotoImage(stagea_photo)
                stagea_label = Label(image = stagea_photo, borderwidth=0)
                stagea_label.image = stagea_photo
                stagea_label.place(x = 240, y = 70)
                stagea_label = Label(window_stagea, text='Производитель: Nissan', font=font_header, justify=CENTER)
                stagea_label.place(x = 240, y = 420)
                stagea_label = Label(window_stagea, text='Модель: Stagea', font=font_header, justify=CENTER)
                stagea_label.place(x = 240, y = 450)
                stagea_label = Label(window_stagea, text='Тип кузова: 5-ти дверная', font=font_header, justify=CENTER)
                stagea_label.place(x = 240, y = 480)
                stagea_label = Label(window_stagea, text='Компоновка: заднеприводная', font=font_header, justify=CENTER)
                stagea_label.place(x = 240, y = 510)
                stagea_label = Label(window_stagea, text='Стоимость за час: 1500 рублей', font=font_header, justify=CENTER)
                stagea_label.place(x = 240, y = 540)
                def book_stagea():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Nissan Stagea')
                book_stagea = Button(window_stagea, text='Забронировать', command=book_stagea, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_stagea.place(x = 350, y = 570)
                # главный цикл
                window_stagea.mainloop()

            # Фото Stagea
            stagea_photo = Image.open("data\\stagea.png")
            stagea_photo = stagea_photo.resize((80, 70), Image.ANTIALIAS)
            stagea_photo = ImageTk.PhotoImage(stagea_photo)
            stagea_label = Button(image = stagea_photo, borderwidth=0, command=stagea)
            stagea_label.image = stagea_photo
            stagea_label.place(x = 5, y = 70)

            stagea_name = Label(window_nissan, text='Nissan\nStagea', font=('Arial',10), justify=CENTER, width=10)
            stagea_name.place(x = 3, y = 140)
            
            def skyline():
                window_nissan.destroy()
                def exit_skyline():
                    window_skyline.destroy()
                    main = Main()
                    main.run()
                window_skyline = Tk()
                window_skyline.title('Nissan Skyline')
                window_skyline.geometry('900x650+300+20')
                window_skyline.resizable(False, False)
                # настройка
                skyline_label = Label(window_skyline, text='Nissan Skyline', font=('Arial',20), justify=CENTER, **header_padding)
                skyline_label.place(x = 390, y = 10)
                exit_skyline = Button(window_skyline, text='Выйти', command=exit_skyline, borderwidth=5,font=('Arial',16), width=10)
                exit_skyline.place(x = 750, y = 20)
                skyline_photo = Image.open("data\\skyline.png")
                skyline_photo = skyline_photo.resize((440, 350), Image.ANTIALIAS)
                skyline_photo = ImageTk.PhotoImage(skyline_photo)
                skyline_label = Label(image = skyline_photo, borderwidth=0)
                skyline_label.image = skyline_photo
                skyline_label.place(x = 240, y = 70)
                skyline_label = Label(window_skyline, text='Производитель: Nissan', font=font_header, justify=CENTER)
                skyline_label.place(x = 240, y = 420)
                skyline_label = Label(window_skyline, text='Модель: Skyline GT-R R34', font=font_header, justify=CENTER)
                skyline_label.place(x = 240, y = 450)
                skyline_label = Label(window_skyline, text='Тип кузова: 2-x дверная', font=font_header, justify=CENTER)
                skyline_label.place(x = 240, y = 480)
                skyline_label = Label(window_skyline, text='Компоновка: полноприводная', font=font_header, justify=CENTER)
                skyline_label.place(x = 240, y = 510)
                skyline_label = Label(window_skyline, text='Стоимость за час: 6000 рублей', font=font_header, justify=CENTER)
                skyline_label.place(x = 240, y = 540)
                def book_skyline():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Nissan Skyline')
                book_skyline = Button(window_skyline, text='Забронировать', command=book_skyline, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_skyline.place(x = 350, y = 570)
                # главный цикл
                window_skyline.mainloop()
                
            # Фото Skyline
            skyline_photo = Image.open("data\\skyline.png")
            skyline_photo = skyline_photo.resize((80, 70), Image.ANTIALIAS)
            skyline_photo = ImageTk.PhotoImage(skyline_photo)
            skyline_label = Button(image = skyline_photo, borderwidth=0, command=skyline)
            skyline_label.image = skyline_photo
            skyline_label.place(x = 90, y = 70)

            skyline_name = Label(window_nissan, text='Nissan\nSkyline', font=('Arial',10), justify=CENTER, width=10)
            skyline_name.place(x = 90, y=140)
            
            def silvia():
                window_nissan.destroy()
                def exit_silvia():
                    window_silvia.destroy()
                    main = Main()
                    main.run()
                window_silvia = Tk()
                window_silvia.title('Nissan Silvia s15')
                window_silvia.geometry('900x650+300+20')
                window_silvia.resizable(False, False)
                # настройка
                silvia_label = Label(window_silvia, text='Nissan Silvia s15', font=('Arial',20), justify=CENTER, **header_padding)
                silvia_label.place(x = 390, y = 10)
                exit_silvia = Button(window_silvia, text='Выйти', command=exit_silvia, borderwidth=5,font=('Arial',16), width=10)
                exit_silvia.place(x = 750, y = 20)
                silvia_photo = Image.open("data\\silvia.png")
                silvia_photo = silvia_photo.resize((440, 350), Image.ANTIALIAS)
                silvia_photo = ImageTk.PhotoImage(silvia_photo)
                silvia_label = Label(image = silvia_photo, borderwidth=0)
                silvia_label.image = silvia_photo
                silvia_label.place(x = 240, y = 70)
                silvia_label = Label(window_silvia, text='Производитель: Nissan', font=font_header, justify=CENTER)
                silvia_label.place(x = 240, y = 420)
                silvia_label = Label(window_silvia, text='Модель: Silvia s15', font=font_header, justify=CENTER)
                silvia_label.place(x = 240, y = 450)
                silvia_label = Label(window_silvia, text='Тип кузова: 2-х дверная', font=font_header, justify=CENTER)
                silvia_label.place(x = 240, y = 480)
                silvia_label = Label(window_silvia, text='Компоновка: заднеприводная', font=font_header, justify=CENTER)
                silvia_label.place(x = 240, y = 510)
                silvia_label = Label(window_silvia, text='Стоимость за час: 5000 рублей', font=font_header, justify=CENTER)
                silvia_label.place(x = 240, y = 540)
                def book_silvia():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Nissan Silvia s15')
                book_silvia = Button(window_silvia, text='Забронировать', command=book_silvia, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_silvia.place(x = 350, y = 570)
                # главный цикл
                window_silvia.mainloop()

            # Фото Silvia
            silvia_photo = Image.open("data\\silvia.png")
            silvia_photo = silvia_photo.resize((80, 70), Image.ANTIALIAS)
            silvia_photo = ImageTk.PhotoImage(silvia_photo)
            silvia_label = Button(image = silvia_photo, borderwidth=0, command=silvia)
            silvia_label.image = silvia_photo
            silvia_label.place(x = 175, y = 70)

            silvia_name = Label(window_nissan, text='Nissan\nSilvia s15', font=('Arial',10), justify=CENTER, width=10)
            silvia_name.place(x = 175, y = 140)
            
            def GTR():
                window_nissan.destroy()
                def exit_GTR():
                    window_GTR.destroy()
                    main = Main()
                    main.run()
                window_GTR = Tk()
                window_GTR.title('Nissan GTR')
                window_GTR.geometry('900x650+300+20')
                window_GTR.resizable(False, False)
                # настройка
                GTR_label = Label(window_GTR, text='Nissan GTR', font=('Arial',20), justify=CENTER, **header_padding)
                GTR_label.place(x = 390, y = 10)
                exit_GTR = Button(window_GTR, text='Выйти', command=exit_GTR, borderwidth=5,font=('Arial',16), width=10)
                exit_GTR.place(x = 750, y = 20)
                GTR_photo = Image.open("data\\gtr.png")
                GTR_photo = GTR_photo.resize((440, 350), Image.ANTIALIAS)
                GTR_photo = ImageTk.PhotoImage(GTR_photo)
                GTR_label = Label(image = GTR_photo, borderwidth=0)
                GTR_label.image = GTR_photo
                GTR_label.place(x = 240, y = 70)
                GTR_label = Label(window_GTR, text='Производитель: Nissan', font=font_header, justify=CENTER)
                GTR_label.place(x = 240, y = 420)
                GTR_label = Label(window_GTR, text='Модель: GTR', font=font_header, justify=CENTER)
                GTR_label.place(x = 240, y = 450)
                GTR_label = Label(window_GTR, text='Тип кузова: 5-ти дверная', font=font_header, justify=CENTER)
                GTR_label.place(x = 240, y = 480)
                GTR_label = Label(window_GTR, text='Компоновка: заднеприводная', font=font_header, justify=CENTER)
                GTR_label.place(x = 240, y = 510)
                GTR_label = Label(window_GTR, text='Стоимость за час: 6500 рублей', font=font_header, justify=CENTER)
                GTR_label.place(x = 240, y = 540)
                def book_GTR():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Nissan GTR')
                book_GTR = Button(window_GTR, text='Забронировать', command=book_GTR, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_GTR.place(x = 350, y = 570)
                # главный цикл
                window_GTR.mainloop()

            # Фото GTR
            GTR_photo = Image.open("data\\gtr.png")
            GTR_photo = GTR_photo.resize((80, 70), Image.ANTIALIAS)
            GTR_photo = ImageTk.PhotoImage(GTR_photo)
            GTR_label = Button(image = GTR_photo, borderwidth=0, command=GTR)
            GTR_label.image = GTR_photo
            GTR_label.place(x = 260, y = 70)

            GTR_name = Label(window_nissan, text='Nissan GTR', font=('Arial',10), justify=CENTER, width=10)
            GTR_name.place(x = 260, y = 140)
            
        # Фото Nissan
        nissan_photo = Image.open("data\\NissanLogo.png")
        nissan_photo = nissan_photo.resize((80, 70), Image.ANTIALIAS)
        nissan_photo = ImageTk.PhotoImage(nissan_photo)
        nissan_label = Button(image = nissan_photo, borderwidth=0, command=nissan)
        nissan_label.image = nissan_photo
        nissan_label.place(x = 90, y = 70)

        nissan_name = Label(window_assortiment, text='Nissan', font=('Arial',10), justify=CENTER, width=10)
        nissan_name.place(x = 90, y=140)

        def porsche():
            window_assortiment.destroy()
            def exit_porsche():
                window_porsche.destroy()
                main = Main()
                main.run()
            window_porsche = Tk()
            window_porsche.title('Porsche')
            window_porsche.geometry('350x230+400+150')
            window_porsche.resizable(False, False)
            # настройка
            lk_label = Label(window_porsche, text='Porsche', font=font_header, justify=CENTER, **header_padding)
            lk_label.place(x = 120, y = 10)

            exit_main_menu = Button(window_porsche, text='Выйти', command=exit_porsche, borderwidth=5, width=10)
            exit_main_menu.place(x = 250, y = 20)
            
            def p911():
                window_porsche.destroy()
                def exit_p911():
                    window_p911.destroy()
                    main = Main()
                    main.run()
                window_p911 = Tk()
                window_p911.title('Porsche 911')
                window_p911.geometry('900x650+300+20')
                window_p911.resizable(False, False)
                # настройка
                p911_label = Label(window_p911, text='Porsche 911', font=('Arial',20), justify=CENTER, **header_padding)
                p911_label.place(x = 390, y = 10)
                exit_p911 = Button(window_p911, text='Выйти', command=exit_p911, borderwidth=5,font=('Arial',16), width=10)
                exit_p911.place(x = 750, y = 20)
                p911_photo = Image.open("data\\911.png")
                p911_photo = p911_photo.resize((440, 350), Image.ANTIALIAS)
                p911_photo = ImageTk.PhotoImage(p911_photo)
                p911_label = Label(image = p911_photo, borderwidth=0)
                p911_label.image = p911_photo
                p911_label.place(x = 240, y = 70)
                p911_label = Label(window_p911, text='Производитель: Porsche', font=font_header, justify=CENTER)
                p911_label.place(x = 240, y = 420)
                p911_label = Label(window_p911, text='Модель: 911', font=font_header, justify=CENTER)
                p911_label.place(x = 240, y = 450)
                p911_label = Label(window_p911, text='Тип кузова: 2-x дверная', font=font_header, justify=CENTER)
                p911_label.place(x = 240, y = 480)
                p911_label = Label(window_p911, text='Компоновка: заднеприводная', font=font_header, justify=CENTER)
                p911_label.place(x = 240, y = 510)
                p911_label = Label(window_p911, text='Стоимость за час: 5000 рублей', font=font_header, justify=CENTER)
                p911_label.place(x = 240, y = 540)
                def book_p911():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Porsche 911')
                book_p911 = Button(window_p911, text='Забронировать', command=book_p911, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_p911.place(x = 350, y = 570)
                # главный цикл
                window_p911.mainloop()
                
            # Фото 911
            p911_photo = Image.open("data\\911.png")
            p911_photo = p911_photo.resize((80, 70), Image.ANTIALIAS)
            p911_photo = ImageTk.PhotoImage(p911_photo)
            p911_label = Button(image = p911_photo, borderwidth=0, command=p911)
            p911_label.image = p911_photo
            p911_label.place(x = 5, y = 70)

            p911_name = Label(window_porsche, text='Porsche 911', font=('Arial',10), justify=CENTER, width=10)
            p911_name.place(x = 5, y = 140)
            
            def cayenne():
                window_porsche.destroy()
                def exit_cayenne():
                    window_cayenne.destroy()
                    main = Main()
                    main.run()
                window_cayenne = Tk()
                window_cayenne.title('Porsche Cayenne')
                window_cayenne.geometry('900x650+300+20')
                window_cayenne.resizable(False, False)
                # настройка
                cayenne_label = Label(window_cayenne, text='Porsche Cayenne', font=('Arial',20), justify=CENTER, **header_padding)
                cayenne_label.place(x = 390, y = 10)
                exit_cayenne = Button(window_cayenne, text='Выйти', command=exit_cayenne, borderwidth=5,font=('Arial',16), width=10)
                exit_cayenne.place(x = 750, y = 20)
                cayenne_photo = Image.open("data\\cayenne.png")
                cayenne_photo = cayenne_photo.resize((440, 350), Image.ANTIALIAS)
                cayenne_photo = ImageTk.PhotoImage(cayenne_photo)
                cayenne_label = Label(image = cayenne_photo, borderwidth=0)
                cayenne_label.image = cayenne_photo
                cayenne_label.place(x = 240, y = 70)
                cayenne_label = Label(window_cayenne, text='Производитель: Porsche', font=font_header, justify=CENTER)
                cayenne_label.place(x = 240, y = 420)
                cayenne_label = Label(window_cayenne, text='Модель: Cayenne', font=font_header, justify=CENTER)
                cayenne_label.place(x = 240, y = 450)
                cayenne_label = Label(window_cayenne, text='Тип кузова: 5-ти дверная', font=font_header, justify=CENTER)
                cayenne_label.place(x = 240, y = 480)
                cayenne_label = Label(window_cayenne, text='Компоновка: полноприводный', font=font_header, justify=CENTER)
                cayenne_label.place(x = 240, y = 510)
                cayenne_label = Label(window_cayenne, text='Стоимость за час: 5000 рублей', font=font_header, justify=CENTER)
                cayenne_label.place(x = 240, y = 540)
                def book_cayenne():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Porsche Cayenne')
                book_cayenne = Button(window_cayenne, text='Забронировать', command=book_cayenne, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_cayenne.place(x = 350, y = 570)
                # главный цикл
                window_cayenne.mainloop()

            # Фото Cayenne
            cayenne_photo = Image.open("data\\cayenne.png")
            cayenne_photo = cayenne_photo.resize((80, 70), Image.ANTIALIAS)
            cayenne_photo = ImageTk.PhotoImage(cayenne_photo)
            cayenne_label = Button(image = cayenne_photo, borderwidth=0, command=cayenne)
            cayenne_label.image = cayenne_photo
            cayenne_label.place(x = 90, y = 70)

            cayenne_name = Label(window_porsche, text='Porsche\nCayenne', font=('Arial',10), justify=CENTER, width=10)
            cayenne_name.place(x = 90, y = 140)
            
            def panamera():
                window_porsche.destroy()
                def exit_panamera():
                    window_panamera.destroy()
                    main = Main()
                    main.run()
                window_panamera = Tk()
                window_panamera.title('Porsche panamera')
                window_panamera.geometry('900x650+300+20')
                window_panamera.resizable(False, False)
                # настройка
                panamera_label = Label(window_panamera, text='Porsche Panamera', font=('Arial',20), justify=CENTER, **header_padding)
                panamera_label.place(x = 390, y = 10)
                exit_panamera = Button(window_panamera, text='Выйти', command=exit_panamera, borderwidth=5,font=('Arial',16), width=10)
                exit_panamera.place(x = 750, y = 20)
                panamera_photo = Image.open("data\\panamera.png")
                panamera_photo = panamera_photo.resize((440, 350), Image.ANTIALIAS)
                panamera_photo = ImageTk.PhotoImage(panamera_photo)
                panamera_label = Label(image = panamera_photo, borderwidth=0)
                panamera_label.image = panamera_photo
                panamera_label.place(x = 240, y = 70)
                panamera_label = Label(window_panamera, text='Производитель: Porsche', font=font_header, justify=CENTER)
                panamera_label.place(x = 240, y = 420)
                panamera_label = Label(window_panamera, text='Модель: Panamera', font=font_header, justify=CENTER)
                panamera_label.place(x = 240, y = 450)
                panamera_label = Label(window_panamera, text='Тип кузова: 5-ти дверная', font=font_header, justify=CENTER)
                panamera_label.place(x = 240, y = 480)
                panamera_label = Label(window_panamera, text='Компоновка: полноприводный', font=font_header, justify=CENTER)
                panamera_label.place(x = 240, y = 510)
                panamera_label = Label(window_panamera, text='Стоимость за час: 5000 рублей', font=font_header, justify=CENTER)
                panamera_label.place(x = 240, y = 540)
                def book_panamera():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Porsche Panamera')
                book_panamera = Button(window_panamera, text='Забронировать', command=book_panamera, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_panamera.place(x = 350, y = 570)
                # главный цикл
                window_panamera.mainloop()

            # Фото Panamera
            panamera_photo = Image.open("data\\panamera.png")
            panamera_photo = panamera_photo.resize((80, 70), Image.ANTIALIAS)
            panamera_photo = ImageTk.PhotoImage(panamera_photo)
            panamera_label = Button(image = panamera_photo, borderwidth=0, command=panamera)
            panamera_label.image = panamera_photo
            panamera_label.place(x = 175, y = 70)

            panamera_name = Label(window_porsche, text='Porsche\nPanamera', font=('Arial',10), justify=CENTER, width=10)
            panamera_name.place(x = 175, y = 140)
            
            def taycan():
                window_porsche.destroy()
                def exit_taycan():
                    window_taycan.destroy()
                    main = Main()
                    main.run()
                window_taycan = Tk()
                window_taycan.title('Porsche Taycan')
                window_taycan.geometry('900x650+300+20')
                window_taycan.resizable(False, False)
                # настройка
                taycan_label = Label(window_taycan, text='Porsche Taycan', font=('Arial',20), justify=CENTER, **header_padding)
                taycan_label.place(x = 390, y = 10)
                exit_taycan = Button(window_taycan, text='Выйти', command=exit_taycan, borderwidth=5,font=('Arial',16), width=10)
                exit_taycan.place(x = 750, y = 20)
                taycan_photo = Image.open("data\\taycan.png")
                taycan_photo = taycan_photo.resize((440, 350), Image.ANTIALIAS)
                taycan_photo = ImageTk.PhotoImage(taycan_photo)
                taycan_label = Label(image = taycan_photo, borderwidth=0)
                taycan_label.image = taycan_photo
                taycan_label.place(x = 240, y = 70)
                taycan_label = Label(window_taycan, text='Производитель: Porsche', font=font_header, justify=CENTER)
                taycan_label.place(x = 240, y = 420)
                taycan_label = Label(window_taycan, text='Модель: Taycan', font=font_header, justify=CENTER)
                taycan_label.place(x = 240, y = 450)
                taycan_label = Label(window_taycan, text='Тип кузова: 4-х дверная', font=font_header, justify=CENTER)
                taycan_label.place(x = 240, y = 480)
                taycan_label = Label(window_taycan, text='Компоновка: полноприводный', font=font_header, justify=CENTER)
                taycan_label.place(x = 240, y = 510)
                taycan_label = Label(window_taycan, text='Стоимость за час: 5000 рублей', font=font_header, justify=CENTER)
                taycan_label.place(x = 240, y = 540)
                def book_taycan():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Porsche Taycan')
                book_taycan = Button(window_taycan, text='Забронировать', command=book_taycan, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_taycan.place(x = 350, y = 570)
                # главный цикл
                window_taycan.mainloop()

            # Фото Porsche taycan
            taycan_photo = Image.open("data\\taycan.png")
            taycan_photo = taycan_photo.resize((80, 70), Image.ANTIALIAS)
            taycan_photo = ImageTk.PhotoImage(taycan_photo)
            taycan_label = Button(image = taycan_photo, borderwidth=0, command=taycan)
            taycan_label.image = taycan_photo
            taycan_label.place(x = 260, y = 70)

            taycan_name = Label(window_porsche, text='Porsche\nTaycan', font=('Arial',10), justify=CENTER, width=10)
            taycan_name.place(x = 260, y = 140)

        # Фото Porsche
        porsche_photo = Image.open("data\\PorscheLogo.png")
        porsche_photo = porsche_photo.resize((80, 70), Image.ANTIALIAS)
        porsche_photo = ImageTk.PhotoImage(porsche_photo)
        porsche_label = Button(image = porsche_photo, borderwidth=0, command=porsche)
        porsche_label.image = porsche_photo
        porsche_label.place(x = 175, y = 70)

        porsche_name = Label(window_assortiment, text='Porsche', font=('Arial',10), justify=CENTER, width=10)
        porsche_name.place(x = 175, y=140)
        
        def toyota():
            window_assortiment.destroy()
            def exit_toyota():
                window_toyota.destroy()
                main = Main()
                main.run()
            window_toyota = Tk()
            window_toyota.title('Toyota')
            window_toyota.geometry('350x230+400+150')
            window_toyota.resizable(False, False)
            # настройка
            lk_label = Label(window_toyota, text='Toyota', font=font_header, justify=CENTER, **header_padding)
            lk_label.place(x = 120, y = 10)

            exit_main_menu = Button(window_toyota, text='Выйти', command=exit_toyota, borderwidth=5, width=10)
            exit_main_menu.place(x = 250, y = 20)
            
            def trueno():
                window_toyota.destroy()
                def exit_trueno():
                    window_trueno.destroy()
                    main = Main()
                    main.run()
                window_trueno = Tk()
                window_trueno.title('Toyota Trueno')
                window_trueno.geometry('900x650+300+20')
                window_trueno.resizable(False, False)
                # настройка
                trueno_label = Label(window_trueno, text='Toyota Trueno', font=('Arial',20), justify=CENTER, **header_padding)
                trueno_label.place(x = 390, y = 10)
                exit_trueno = Button(window_trueno, text='Выйти', command=exit_trueno, borderwidth=5,font=('Arial',16), width=10)
                exit_trueno.place(x = 750, y = 20)
                trueno_photo = Image.open("data\\trueno.png")
                trueno_photo = trueno_photo.resize((440, 350), Image.ANTIALIAS)
                trueno_photo = ImageTk.PhotoImage(trueno_photo)
                trueno_label = Label(image = trueno_photo, borderwidth=0)
                trueno_label.image = trueno_photo
                trueno_label.place(x = 240, y = 70)
                trueno_label = Label(window_trueno, text='Производитель: Toyota', font=font_header, justify=CENTER)
                trueno_label.place(x = 240, y = 420)
                trueno_label = Label(window_trueno, text='Модель: Trueno AE86', font=font_header, justify=CENTER)
                trueno_label.place(x = 240, y = 450)
                trueno_label = Label(window_trueno, text='Тип кузова: 3-x дверная', font=font_header, justify=CENTER)
                trueno_label.place(x = 240, y = 480)
                trueno_label = Label(window_trueno, text='Компоновка: заднеприводная', font=font_header, justify=CENTER)
                trueno_label.place(x = 240, y = 510)
                trueno_label = Label(window_trueno, text='Стоимость за час: 3000 рублей', font=font_header, justify=CENTER)
                trueno_label.place(x = 240, y = 540)
                def book_trueno():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Toyota Trueno')
                book_trueno = Button(window_trueno, text='Забронировать', command=book_trueno, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_trueno.place(x = 350, y = 570)
                # главный цикл
                window_trueno.mainloop()
                
            # Фото Trueno
            trueno_photo = Image.open("data\\trueno.png")
            trueno_photo = trueno_photo.resize((80, 70), Image.ANTIALIAS)
            trueno_photo = ImageTk.PhotoImage(trueno_photo)
            trueno_label = Button(image = trueno_photo, borderwidth=0, command=trueno)
            trueno_label.image = trueno_photo
            trueno_label.place(x = 5, y = 70)

            trueno_name = Label(window_toyota, text='Toyota Trueno', font=('Arial',10), justify=CENTER, width=10)
            trueno_name.place(x = 5, y = 140)
            
            def supra():
                window_toyota.destroy()
                def exit_supra():
                    window_supra.destroy()
                    main = Main()
                    main.run()
                window_supra = Tk()
                window_supra.title('Toyota Supra')
                window_supra.geometry('900x650+300+20')
                window_supra.resizable(False, False)
                # настройка
                supra_label = Label(window_supra, text='Toyota Supra', font=('Arial',20), justify=CENTER, **header_padding)
                supra_label.place(x = 390, y = 10)
                exit_supra = Button(window_supra, text='Выйти', command=exit_supra, borderwidth=5,font=('Arial',16), width=10)
                exit_supra.place(x = 750, y = 20)
                supra_photo = Image.open("data\\supra.png")
                supra_photo = supra_photo.resize((440, 350), Image.ANTIALIAS)
                supra_photo = ImageTk.PhotoImage(supra_photo)
                supra_label = Label(image = supra_photo, borderwidth=0)
                supra_label.image = supra_photo
                supra_label.place(x = 240, y = 70)
                supra_label = Label(window_supra, text='Производитель: Toyota', font=font_header, justify=CENTER)
                supra_label.place(x = 240, y = 420)
                supra_label = Label(window_supra, text='Модель: Supra A80', font=font_header, justify=CENTER)
                supra_label.place(x = 240, y = 450)
                supra_label = Label(window_supra, text='Тип кузова: 2-x дверная', font=font_header, justify=CENTER)
                supra_label.place(x = 240, y = 480)
                supra_label = Label(window_supra, text='Компоновка: заднеприводная', font=font_header, justify=CENTER)
                supra_label.place(x = 240, y = 510)
                supra_label = Label(window_supra, text='Стоимость за час: 4000 рублей', font=font_header, justify=CENTER)
                supra_label.place(x = 240, y = 540)
                def book_supra():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Toyota Supra')
                book_supra = Button(window_supra, text='Забронировать', command=book_supra, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_supra.place(x = 350, y = 570)
                # главный цикл
                window_supra.mainloop()
                
            # Фото Supra
            supra_photo = Image.open("data\\supra.png")
            supra_photo = supra_photo.resize((80, 70), Image.ANTIALIAS)
            supra_photo = ImageTk.PhotoImage(supra_photo)
            supra_label = Button(image = supra_photo, borderwidth=0, command=supra)
            supra_label.image = supra_photo
            supra_label.place(x = 90, y = 70)

            supra_name = Label(window_toyota, text='Toyota Supra', font=('Arial',10), justify=CENTER, width=10)
            supra_name.place(x = 90, y = 140)
            
            def mark_II():
                window_toyota.destroy()
                def exit_mark_II():
                    window_mark_II.destroy()
                    main = Main()
                    main.run()
                window_mark_II = Tk()
                window_mark_II.title('Toyota Mark II')
                window_mark_II.geometry('900x650+300+20')
                window_mark_II.resizable(False, False)
                # настройка
                mark_II_label = Label(window_mark_II, text='Toyota Mark II', font=('Arial',20), justify=CENTER, **header_padding)
                mark_II_label.place(x = 390, y = 10)
                exit_mark_II = Button(window_mark_II, text='Выйти', command=exit_mark_II, borderwidth=5,font=('Arial',16), width=10)
                exit_mark_II.place(x = 750, y = 20)
                mark_II_photo = Image.open("data\\mark2.png")
                mark_II_photo = mark_II_photo.resize((440, 350), Image.ANTIALIAS)
                mark_II_photo = ImageTk.PhotoImage(mark_II_photo)
                mark_II_label = Label(image = mark_II_photo, borderwidth=0)
                mark_II_label.image = mark_II_photo
                mark_II_label.place(x = 240, y = 70)
                mark_II_label = Label(window_mark_II, text='Производитель: Toyota', font=font_header, justify=CENTER)
                mark_II_label.place(x = 240, y = 420)
                mark_II_label = Label(window_mark_II, text='Модель: Mark II', font=font_header, justify=CENTER)
                mark_II_label.place(x = 240, y = 450)
                mark_II_label = Label(window_mark_II, text='Тип кузова: 4-х дверная', font=font_header, justify=CENTER)
                mark_II_label.place(x = 240, y = 480)
                mark_II_label = Label(window_mark_II, text='Компоновка: полноприводный', font=font_header, justify=CENTER)
                mark_II_label.place(x = 240, y = 510)
                mark_II_label = Label(window_mark_II, text='Стоимость за час: 5000 рублей', font=font_header, justify=CENTER)
                mark_II_label.place(x = 240, y = 540)
                def book_mark_II():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Toyota Mark II')
                book_mark_II = Button(window_mark_II, text='Забронировать', command=book_mark_II, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_mark_II.place(x = 350, y = 570)
                # главный цикл
                window_mark_II.mainloop()

            # Фото Toyota mark_II
            mark_II_photo = Image.open("data\\mark2.png")
            mark_II_photo = mark_II_photo.resize((80, 70), Image.ANTIALIAS)
            mark_II_photo = ImageTk.PhotoImage(mark_II_photo)
            mark_II_label = Button(image = mark_II_photo, borderwidth=0, command=mark_II)
            mark_II_label.image = mark_II_photo
            mark_II_label.place(x = 175, y = 70)

            mark_II_name = Label(window_toyota, text='Toyota Mark II', font=('Arial',10), justify=CENTER, width=10)
            mark_II_name.place(x=175, y=140)
            
            def crown():
                window_toyota.destroy()
                def exit_crown():
                    window_crown.destroy()
                    main = Main()
                    main.run()
                window_crown = Tk()
                window_crown.title('Toyota Crown')
                window_crown.geometry('900x650+300+20')
                window_crown.resizable(False, False)
                # настройка
                crown_label = Label(window_crown, text='Toyota Crown', font=('Arial',20), justify=CENTER, **header_padding)
                crown_label.place(x = 390, y = 10)
                exit_crown = Button(window_crown, text='Выйти', command=exit_crown, borderwidth=5,font=('Arial',16), width=10)
                exit_crown.place(x = 750, y = 20)
                crown_photo = Image.open("data\\crown.png")
                crown_photo = crown_photo.resize((440, 350), Image.ANTIALIAS)
                crown_photo = ImageTk.PhotoImage(crown_photo)
                crown_label = Label(image = crown_photo, borderwidth=0)
                crown_label.image = crown_photo
                crown_label.place(x = 240, y = 70)
                crown_label = Label(window_crown, text='Производитель: Toyota', font=font_header, justify=CENTER)
                crown_label.place(x = 240, y = 420)
                crown_label = Label(window_crown, text='Модель: Crown', font=font_header, justify=CENTER)
                crown_label.place(x = 240, y = 450)
                crown_label = Label(window_crown, text='Тип кузова: 4-х дверная', font=font_header, justify=CENTER)
                crown_label.place(x = 240, y = 480)
                crown_label = Label(window_crown, text='Компоновка: полноприводный', font=font_header, justify=CENTER)
                crown_label.place(x = 240, y = 510)
                crown_label = Label(window_crown, text='Стоимость за час: 5000 рублей', font=font_header, justify=CENTER)
                crown_label.place(x = 240, y = 540)
                def book_crown():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Toyota Crown')
                book_crown = Button(window_crown, text='Забронировать', command=book_crown, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_crown.place(x = 350, y = 570)
                # главный цикл
                window_crown.mainloop()

            # Фото Toyota crown
            crown_photo = Image.open("data\\crown.png")
            crown_photo = crown_photo.resize((80, 70), Image.ANTIALIAS)
            crown_photo = ImageTk.PhotoImage(crown_photo)
            crown_label = Button(image = crown_photo, borderwidth=0, command=crown)
            crown_label.image = crown_photo
            crown_label.place(x = 260, y = 70)

            crown_name = Label(window_toyota, text='Toyota Crown', font=('Arial',10), justify=CENTER, width=10)
            crown_name.place(x=260, y=140)
            
        # Фото Toyota
        toyota_photo = Image.open("data\\ToyotaLogo.png")
        toyota_photo = toyota_photo.resize((80, 70), Image.ANTIALIAS)
        toyota_photo = ImageTk.PhotoImage(toyota_photo)
        toyota_label = Button(image = toyota_photo, borderwidth=0, command=toyota)
        toyota_label.image = toyota_photo
        toyota_label.place(x = 260, y = 70)

        toyota_name = Label(window_assortiment, text='Toyota', font=('Arial',10), justify=CENTER, width=10)
        toyota_name.place(x = 260, y=140)
        
        def mazda():
            window_assortiment.destroy()
            def exit_mazda():
                window_mazda.destroy()
                main = Main()
                main.run()
            window_mazda = Tk()
            window_mazda.title('Mazda')
            window_mazda.geometry('350x230+400+150')
            window_mazda.resizable(False, False)
            # настройка
            lk_label = Label(window_mazda, text='Mazda', font=font_header, justify=CENTER, **header_padding)
            lk_label.place(x = 120, y = 10)

            exit_main_menu = Button(window_mazda, text='Выйти', command=exit_mazda, borderwidth=5, width=10)
            exit_main_menu.place(x = 250, y = 20)

            def rx_7():
                window_mazda.destroy()
                def exit_rx_7():
                    window_rx_7.destroy()
                    main = Main()
                    main.run()
                window_rx_7 = Tk()
                window_rx_7.title('Mazda RX-7')
                window_rx_7.geometry('900x650+300+20')
                window_rx_7.resizable(False, False)
                # настройка
                rx_7_label = Label(window_rx_7, text='Mazda RX-7', font=('Arial',20), justify=CENTER, **header_padding)
                rx_7_label.place(x = 390, y = 10)
                exit_rx_7 = Button(window_rx_7, text='Выйти', command=exit_rx_7, borderwidth=5,font=('Arial',16), width=10)
                exit_rx_7.place(x = 750, y = 20)
                rx_7_photo = Image.open("data\\rx7.png")
                rx_7_photo = rx_7_photo.resize((440, 350), Image.ANTIALIAS)
                rx_7_photo = ImageTk.PhotoImage(rx_7_photo)
                rx_7_label = Label(image = rx_7_photo, borderwidth=0)
                rx_7_label.image = rx_7_photo
                rx_7_label.place(x = 240, y = 70)
                rx_7_label = Label(window_rx_7, text='Производитель: Mazda', font=font_header, justify=CENTER)
                rx_7_label.place(x = 240, y = 420)
                rx_7_label = Label(window_rx_7, text='Модель: RX-7', font=font_header, justify=CENTER)
                rx_7_label.place(x = 240, y = 450)
                rx_7_label = Label(window_rx_7, text='Тип кузова: 2-х дверная', font=font_header, justify=CENTER)
                rx_7_label.place(x = 240, y = 480)
                rx_7_label = Label(window_rx_7, text='Компоновка: заднеприводный', font=font_header, justify=CENTER)
                rx_7_label.place(x = 240, y = 510)
                rx_7_label = Label(window_rx_7, text='Стоимость за час: 5000 рублей', font=font_header, justify=CENTER)
                rx_7_label.place(x = 240, y = 540)
                def book_rx_7():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Mazda RX-7')
                book_rx_7 = Button(window_rx_7, text='Забронировать', command=book_rx_7, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_rx_7.place(x = 350, y = 570)
                # главный цикл
                window_rx_7.mainloop()

            # Фото Mazda rx_7
            rx_7_photo = Image.open("data\\rx7.png")
            rx_7_photo = rx_7_photo.resize((80, 70), Image.ANTIALIAS)
            rx_7_photo = ImageTk.PhotoImage(rx_7_photo)
            rx_7_label = Button(image = rx_7_photo, borderwidth=0, command=rx_7)
            rx_7_label.image = rx_7_photo
            rx_7_label.place(x = 5, y = 70)

            rx_7_name = Label(window_mazda, text='Mazda RX-7', font=('Arial',10), justify=CENTER, width=10)
            rx_7_name.place(x=5, y=140)
            
            def miata():
                window_mazda.destroy()
                def exit_miata():
                    window_miata.destroy()
                    main = Main()
                    main.run()
                window_miata = Tk()
                window_miata.title('Mazda Miata')
                window_miata.geometry('900x650+300+20')
                window_miata.resizable(False, False)
                # настройка
                miata_label = Label(window_miata, text='Mazda Miata', font=('Arial',20), justify=CENTER, **header_padding)
                miata_label.place(x = 390, y = 10)
                exit_miata = Button(window_miata, text='Выйти', command=exit_miata, borderwidth=5,font=('Arial',16), width=10)
                exit_miata.place(x = 750, y = 20)
                miata_photo = Image.open("data\\miata.png")
                miata_photo = miata_photo.resize((440, 350), Image.ANTIALIAS)
                miata_photo = ImageTk.PhotoImage(miata_photo)
                miata_label = Label(image = miata_photo, borderwidth=0)
                miata_label.image = miata_photo
                miata_label.place(x = 240, y = 70)
                miata_label = Label(window_miata, text='Производитель: Mazda', font=font_header, justify=CENTER)
                miata_label.place(x = 240, y = 420)
                miata_label = Label(window_miata, text='Модель: Miata', font=font_header, justify=CENTER)
                miata_label.place(x = 240, y = 450)
                miata_label = Label(window_miata, text='Тип кузова: 2-х дверная', font=font_header, justify=CENTER)
                miata_label.place(x = 240, y = 480)
                miata_label = Label(window_miata, text='Компоновка: заднеприводный', font=font_header, justify=CENTER)
                miata_label.place(x = 240, y = 510)
                miata_label = Label(window_miata, text='Стоимость за час: 5000 рублей', font=font_header, justify=CENTER)
                miata_label.place(x = 240, y = 540)
                def book_miata():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Mazda Miata')
                book_miata = Button(window_miata, text='Забронировать', command=book_miata, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_miata.place(x = 350, y = 570)
                # главный цикл
                window_miata.mainloop()

            # Фото Mazda miata
            miata_photo = Image.open("data\\miata.png")
            miata_photo = miata_photo.resize((80, 70), Image.ANTIALIAS)
            miata_photo = ImageTk.PhotoImage(miata_photo)
            miata_label = Button(image = miata_photo, borderwidth=0, command=miata)
            miata_label.image = miata_photo
            miata_label.place(x = 90, y = 70)

            miata_name = Label(window_mazda, text='Mazda miata', font=('Arial',10), justify=CENTER, width=10)
            miata_name.place(x=90, y=140)
            
            def roadster():
                window_mazda.destroy()
                def exit_roadster():
                    window_roadster.destroy()
                    main = Main()
                    main.run()
                window_roadster = Tk()
                window_roadster.title('Mazda Roadster')
                window_roadster.geometry('900x650+300+20')
                window_roadster.resizable(False, False)
                # настройка
                roadster_label = Label(window_roadster, text='Mazda Roadster', font=('Arial',20), justify=CENTER, **header_padding)
                roadster_label.place(x = 390, y = 10)
                exit_roadster = Button(window_roadster, text='Выйти', command=exit_roadster, borderwidth=5,font=('Arial',16), width=10)
                exit_roadster.place(x = 750, y = 20)
                roadster_photo = Image.open("data\\roadster.png")
                roadster_photo = roadster_photo.resize((440, 350), Image.ANTIALIAS)
                roadster_photo = ImageTk.PhotoImage(roadster_photo)
                roadster_label = Label(image = roadster_photo, borderwidth=0)
                roadster_label.image = roadster_photo
                roadster_label.place(x = 240, y = 70)
                roadster_label = Label(window_roadster, text='Производитель: Mazda', font=font_header, justify=CENTER)
                roadster_label.place(x = 240, y = 420)
                roadster_label = Label(window_roadster, text='Модель: Roadster', font=font_header, justify=CENTER)
                roadster_label.place(x = 240, y = 450)
                roadster_label = Label(window_roadster, text='Тип кузова: 2-х дверная', font=font_header, justify=CENTER)
                roadster_label.place(x = 240, y = 480)
                roadster_label = Label(window_roadster, text='Компоновка: заднеприводный', font=font_header, justify=CENTER)
                roadster_label.place(x = 240, y = 510)
                roadster_label = Label(window_roadster, text='Стоимость за час: 5000 рублей', font=font_header, justify=CENTER)
                roadster_label.place(x = 240, y = 540)
                def book_roadster():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Mazda Roadster')
                book_roadster = Button(window_roadster, text='Забронировать', command=book_roadster, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_roadster.place(x = 350, y = 570)
                # главный цикл
                window_roadster.mainloop()

            # Фото Mazda roadster
            roadster_photo = Image.open("data\\roadster.png")
            roadster_photo = roadster_photo.resize((80, 70), Image.ANTIALIAS)
            roadster_photo = ImageTk.PhotoImage(roadster_photo)
            roadster_label = Button(image = roadster_photo, borderwidth=0, command=roadster)
            roadster_label.image = roadster_photo
            roadster_label.place(x = 175, y = 70)

            roadster_name = Label(window_mazda, text='Mazda\nRoadster', font=('Arial',10), justify=CENTER, width=10)
            roadster_name.place(x=175, y=140)
            
            def rx_8():
                window_mazda.destroy()
                def exit_rx_8():
                    window_rx_8.destroy()
                    main = Main()
                    main.run()
                window_rx_8 = Tk()
                window_rx_8.title('Mazda RX-8')
                window_rx_8.geometry('900x650+300+20')
                window_rx_8.resizable(False, False)
                # настройка
                rx_8_label = Label(window_rx_8, text='Mazda RX-8', font=('Arial',20), justify=CENTER, **header_padding)
                rx_8_label.place(x = 390, y = 10)
                exit_rx_8 = Button(window_rx_8, text='Выйти', command=exit_rx_8, borderwidth=5,font=('Arial',16), width=10)
                exit_rx_8.place(x = 750, y = 20)
                rx_8_photo = Image.open("data\\rx8.png")
                rx_8_photo = rx_8_photo.resize((440, 350), Image.ANTIALIAS)
                rx_8_photo = ImageTk.PhotoImage(rx_8_photo)
                rx_8_label = Label(image = rx_8_photo, borderwidth=0)
                rx_8_label.image = rx_8_photo
                rx_8_label.place(x = 240, y = 70)
                rx_8_label = Label(window_rx_8, text='Производитель: Mazda', font=font_header, justify=CENTER)
                rx_8_label.place(x = 240, y = 420)
                rx_8_label = Label(window_rx_8, text='Модель: RX-8', font=font_header, justify=CENTER)
                rx_8_label.place(x = 240, y = 450)
                rx_8_label = Label(window_rx_8, text='Тип кузова: 3-х дверная', font=font_header, justify=CENTER)
                rx_8_label.place(x = 240, y = 480)
                rx_8_label = Label(window_rx_8, text='Компоновка: заднеприводный', font=font_header, justify=CENTER)
                rx_8_label.place(x = 240, y = 510)
                rx_8_label = Label(window_rx_8, text='Стоимость за час: 5000 рублей', font=font_header, justify=CENTER)
                rx_8_label.place(x = 240, y = 540)
                def book_rx_8():
                    messagebox.showinfo('Информация','Вы успешно забронировали машину Mazda RX-8')
                book_rx_8 = Button(window_rx_8, text='Забронировать', command=book_rx_8, borderwidth=5, width=20, height=1, font=('Arial',16))
                book_rx_8.place(x = 350, y = 570)
                # главный цикл
                window_rx_8.mainloop()

            # Фото Mazda rx_8
            rx_8_photo = Image.open("data\\rx8.png")
            rx_8_photo = rx_8_photo.resize((80, 70), Image.ANTIALIAS)
            rx_8_photo = ImageTk.PhotoImage(rx_8_photo)
            rx_8_label = Button(image = rx_8_photo, borderwidth=0, command=rx_8)
            rx_8_label.image = rx_8_photo
            rx_8_label.place(x = 260, y = 70)

            rx_8_name = Label(window_mazda, text='Mazda RX-8', font=('Arial',10), justify=CENTER, width=10)
            rx_8_name.place(x=260, y=140)
            
        # Фото Mazda
        mazda_photo = Image.open("data\\MazdaLogo.png")
        mazda_photo = mazda_photo.resize((80, 70), Image.ANTIALIAS)
        mazda_photo = ImageTk.PhotoImage(mazda_photo)
        mazda_label = Button(image = mazda_photo, borderwidth=0, command=mazda)
        mazda_label.image = mazda_photo
        mazda_label.place(x = 345, y = 70)

        mazda_name = Label(window_assortiment, text='Mazda', font=('Arial',10), justify=CENTER, width=10)
        mazda_name.place(x = 345, y=140)
        
        # главный цикл
        window_assortiment.mainloop()