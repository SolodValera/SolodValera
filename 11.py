
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkinter.ttk import Combobox

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('500x300')


tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)


tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Загрузить файл')
tab_control.pack(expand=1, fill='both')


#1
def calc():
    try:
        a = float(en1.get())
        b = float(en2.get())
    except:
        messagebox.showerror("Ошибка", "Введите числа!")
        return

    op = combo.get()
    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    elif op == '/':
        if b == 0:
            messagebox.showerror("Ошибка", "Деление на ноль!")
            return
        res = a / b
    lblres.config(text=f"Ответ: {res}")
'''
    messagebox.showinfo("Результат", f"Ответ: {res}")
'''


lbl1 = Label(tab1, text='Калькулятор', padx=5, pady=5, font='Arial 14')


en1 = Entry(tab1, font='Arial 16', width=10)
en2 = Entry(tab1, font='Arial 16', width=10)

combo = Combobox(tab1, values=['+', '-', '*', '/'], width=3, font='Arial 14')
combo.current(0)

but1 = Button(tab1, text='=', width=3, height=1, command=calc, font='Arial 14')

lblres = Label(tab1, text='', padx=5, pady=5, font='Arial 14')


lbl1.grid(column=0, row=0, columnspan=3)
en1.grid(column=0, row=1, padx=5, pady=5)
combo.grid(column=1, row=1, padx=5, pady=5)
en2.grid(column=2, row=1, padx=5, pady=5)
but1.grid(column=3, row=1, padx=10)
lblres.grid(column=0,row=2,padx=5,pady=5)

#2


lbl2 = Label(tab2, text='Чекбоксы (множественный выбор)', padx=5, pady=5, font='Arial 14')
lbl2.grid(column=0, row=0, columnspan=2)

#чекбоксы
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

cb1 = Checkbutton(tab2, text="Первый", variable=var1, font='Arial 12')
cb2 = Checkbutton(tab2, text="Второй", variable=var2, font='Arial 12')
cb3 = Checkbutton(tab2, text="Третий", variable=var3, font='Arial 12')

cb1.grid(column=0, row=1, sticky=W)
cb2.grid(column=0, row=2, sticky=W)
cb3.grid(column=0, row=3, sticky=W)

def vibor():
    vibori = []

    if var1.get():
        vibori.append("первый")
        btn_check.config(bg='orange')
    if var2.get():
        vibori.append("второй")
        btn_check.config(text='Выбор сделан')
    if var3.get():
        vibori.append("третий")
        btn_check.config(fg='blue',font=('bold'))

    if not vibori:
        messagebox.showinfo('Выбор', 'Ничего не выбрано')
    else:
        messagebox.showinfo('Выбор', f'Вы выбрали:{str(vibori)[1:-1]} ')

btn_check = Button(tab2, text='Показать выбор', command=vibor)
btn_check.grid(column=0, row=4, pady=10)






#3

lbl3 = Label(tab3, text='Загрузить файл', padx=5, pady=5, font='Arial 14')
lbl3.grid(column=0, row=0)

text_box = Text(tab3, width=50, height=10)
text_box.grid(column=0, row=2, padx=10, pady=10)

#загрузка файла
def file():
    openf = filedialog.askopenfilename(
        title="Выберите",
        filetypes=[("Текстовые файлы", "*.txt")]
    )
    if openf:
        with open(openf) as file:
            textf = file.read()
            text_box.delete(1.0, END)
            text_box.insert(END, textf)

btn_load = Button(tab3, text="Открыть файл", command=file, font='Arial 12')
btn_load.grid(column=0, row=1, pady=5)



window.mainloop()














