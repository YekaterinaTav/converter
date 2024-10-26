from tkinter import *
from tkinter import messagebox as mb
import requests
from tkinter import ttk


def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()

    if t_code and b_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            data = response.json()
            print(data)
            if t_code in data['rates']:
                exchange_rates = data['rates'][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]
                mb.showinfo('Курс обмена', f'Курс к доллару{exchange_rates:.1f} {t_name} за 1 {b_name}')
        except Exception as error:
            mb.showerror('Ошибка', f'Произошла ошибка{error}')


def update_cur_label(event):
    code = t_combobox.get()
    name_ru = cur[code]
    cur_label.config(text=name_ru)


window = Tk()
window.title('Конвертер валюты')
window.geometry('400x500')

popular_cur = ["EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "RUB", "KZT", "UZS"]

cur = {
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "USD": "Американский доллар",
    "UZS": "Узбекский сум"
}

Label(text='Выберите код валюты').pack(pady=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
# b_combobox.bind('<<ComboboxSelected>>', update_cur_label)
b_combobox.pack(pady=10)

Label(text='Выберите код валюты').pack(pady=20)
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.bind('<<ComboboxSelected>>', update_cur_label)
t_combobox.pack(pady=10)

cur_label = Label()
cur_label.pack()

Button(text='Получить курс обмена', command=exchange).pack(pady=10)

window.mainloop()
