from tkinter import *
import requests
import json

def zapros():

    name = en.get()
    url = f"https://api.github.com/repos/{name}"
    response = requests.get(url)
    data = response.json()
    polya = ['company', 'created_at', 'email', 'id', 'name', 'url']
    bigstroka = {field: data.get(field) for field in polya}

   
    filename = f"{name.replace('/', ' ')}.json"
   
    with open(filename, 'w') as fileo:
        json.dump(bigstroka, fileo)

root=Tk()

root.title("Запрос на GIT")

label1=Label(root, text="Введите имя репозитория (owner/repo):")
en=Entry(root, width=50)
but1=Button(root, text="Получить данные", command=zapros)

label1.grid(column=0, row=0, columnspan=3)
en.grid(column=0, row=1, padx=5, pady=5)
but1.grid(column=3, row=1, padx=10)


root.mainloop()

