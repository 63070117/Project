from tkinter import *
from datetime import datetime


def record_transaction(menu_item):
    with open("sales.csv", mode='a', newline='', encoding='UTF-8') as f:
        price = menus[menu_item]
        dt = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        f.write(f'{menu_item},{price},{dt}\n')


def show(e):
    menu_item = e.widget.cget("text")
    # print(f"menu = {menu_item}, price = {menus[menu_item]} Baht")
    tv_menu.set(f"MENU = {menu_item}, PRICE = {menus[menu_item]} Baht")
    record_transaction(menu_item)


root = Tk()
root.title("Cash Register")
root.option_add("*Font", "impact 20")
menus = {"Mocha": 30, "latte": 40, "Espresso": 50, "Green Tea": 25, "Tea": 20,
         "Thai Tea": 30, "Coke": 20, "Water": 15, "Black Coffee": 25, "Black Tea": 30,
         "Melon Juice": 30, "Milkshak": 30}
item_per_row = 3

tv_menu = StringVar()

for i, k in enumerate(menus.keys()):
    btn = Button(root, text=k, width=15)
    btn.grid(row=i // item_per_row, column=i % item_per_row)
    btn.bind("<Button-1>", show)
Label(root, text="menu", textvariable=tv_menu, fg="gold3").grid(columnspan=item_per_row)
root.mainloop()