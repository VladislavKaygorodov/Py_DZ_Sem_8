from tkinter import *
import controller as c

def click(name, surname, number, second_number, other, window):
    c.name.append(name.get())
    c.surname.append(surname.get())
    c.first_number.append(number.get())
    c.second_number.append(second_number.get())
    c.other.append(other.get())
    c.save_contact(c.name, c.surname, c.first_number, c.second_number, c.other)
    window.destroy()

def add_contact():
    window1 = Tk()
    window1.title("Добавление нового контакта")
    window1.geometry('500x500')

    lbl_name = Label(window1, text="Введите имя контакта", font=("Arial Bold", 10))
    lbl_name.grid(column=0, row=1)
    txt_name = Entry(window1, width=35)
    txt_name.grid(column=1, row=1)
    txt_name.insert(0,"Антон")

    lbl_surname = Label(window1, text="Введите фамилию контакта", font=("Arial Bold", 10))
    lbl_surname.grid(column=0, row=2)
    txt_surname = Entry(window1, width=35)
    txt_surname.grid(column=1, row=2)
    txt_surname.insert(0,"Антонов")

    lbl_number = Label(window1, text="Введите номер контакта", font=("Arial Bold", 10))
    lbl_number.grid(column=0, row=3)
    txt_number = Entry(window1, width=35)
    txt_number.grid(column=1, row=3)
    txt_number.insert(0,"123456")

    lbl_second_number = Label(window1, text="Введите дополнительный номер контакта", font=("Arial Bold", 10))
    lbl_second_number.grid(column=0, row=4)
    txt_second_number = Entry(window1, width=35)
    txt_second_number.grid(column=1, row=4)
    txt_second_number.insert(0,"Дополнительный номер отсутствует")

    lbl_other = Label(window1, text="Примечания", font=("Arial Bold", 10))
    lbl_other.grid(column=0, row=5)
    txt_other = Entry(window1, width=35)
    txt_other.grid(column=1, row=5)
    txt_other.insert(0,"Примечания отсутствуют")

    but = Button(window1, text = "Сохранить", command=lambda: click(txt_name, txt_surname, txt_number, txt_second_number, txt_other, window1))
    but.grid(column=1, row=6)

    window1.mainloop()

def show_all_contacts():
    window = Tk()
    window.geometry('500x500')
    window.title("Телефонный справочник")
    listbox = Listbox(window, width=100, height=80)
    listbox.pack(anchor="center")
    listbox.insert(END, "Список контактов: ")
    with open('Numbers.txt', 'r', encoding="utf-8") as file:
            for line in file:
                list = line.split('\t')
                for i in list:
                    listbox.insert(END,i)
    mainloop()

def start():
    window = Tk()
    window.geometry('300x150')
    window.title("Телефонный справочник")

    lbl = Label(window, text="Добро пожаловать! Выберете действие", font=("Arial Bold", 10))
    lbl.pack(anchor="n")

    btn_add = Button(window, text = "Добавить контакт", command=add_contact)
    btn_add.pack(anchor="center")

    btn_show = Button(window, text = "Список контактов", command=show_all_contacts)
    btn_show.pack(anchor="s")

    window.mainloop()
