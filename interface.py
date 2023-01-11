import tkinter
from datetime import datetime
import customtkinter
from tkinter import *
import sys
from operator import itemgetter
import sqlite3





# sqlite3 banco de dados
conn = sqlite3.connect('banco_de_tarefas')
cursor = conn.cursor()
cursor.execute('SELECT * FROM tarefas')

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Janela principal
janela = customtkinter.CTk()
janela.geometry("700x400")
janela.title("Agenda de tarefas")
janela.resizable(False, False)

# imagem
img = PhotoImage(file="agenda.png")
label_img = customtkinter.CTkLabel(master=janela, image=img)
label_img.place(x=5, y=65)
# label
frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)
label = customtkinter.CTkLabel(master=frame, text="Agendador de tarefas")
label.place(x=25, y=5)

# listbox
listbox = Listbox(janela, height=24, width=50)
listbox.pack()



def printarTarefaF(tarefa, index):
    listbox.insert(index, f"{index + 1} = {tarefa['nome']} ││ Data = {tarefa['data']}")

tarefas = []
for row in cursor:
    tarefas.append({"nome": row[0], "data": row[1]})

for i, tarefa in enumerate(tarefas):
    printarTarefaF(tarefa, i)



def adicionar_tarefa_evento():
    while True:
        try:
            nome = customtkinter.CTkInputDialog(text="Digite uma tarefa:").get_input()
            if not nome:
                raise ValueError("O nome da tarefa não pode estar vazio")
            break
        except ValueError as e:
            tkinter.messagebox.showerror(title="Error", message="A tarefa não pode está vazia!")
    while True:
        try:
            dia = customtkinter.CTkInputDialog(text="Digite o dia:").get_input()
            dia = int(dia)
            if dia < 1 or dia > 31:
                raise ValueError("O dia deve ser um número inteiro entre 1 e 31")
            break
        except ValueError as e:
            tkinter.messagebox.showerror(title="Error", message="O dia deve ser um número inteiro entre 1 e 31")
    while True:
        try:
            mes = customtkinter.CTkInputDialog(text="Digite o mês:").get_input()
            mes = int(mes)
            if mes < 1 or mes > 12:
                raise ValueError("O mês deve ser um número inteiro entre 1 e 12")
            break
        except ValueError as e:
            tkinter.messagebox.showerror(title="Error", message="O mês deve ser um número inteiro entre 1 e 12!")
    while True:
        try:
            ano = customtkinter.CTkInputDialog(text="Digite o ano:").get_input()
            ano = int(ano)
            if ano < 0:
                raise ValueError("O ano deve ser um número inteiro positivo")
            break
        except ValueError as e:
            tkinter.messagebox.showerror(title="Error", message="O ano deve ser um número inteiro positivo")
    while True:
        try:
            hora = customtkinter.CTkInputDialog(text="Digite a hora:").get_input()
            hora = int(hora)
            if hora < 0 or hora > 23:
                raise ValueError("A hora deve ser um número inteiro entre 0 e 23")
            break
        except ValueError as e:
            tkinter.messagebox.showerror(title="Error", message="A hora deve ser um número inteiro entre 0 e 23")
    while True:
        try:
            minutos = customtkinter.CTkInputDialog(text="Digite os minutos:").get_input()
            minutos = int(minutos)
            if minutos < 0 or minutos > 59:
                raise ValueError("Os minutos devem ser um número inteiro entre 0 e 59")
            break
        except ValueError as e:
            tkinter.messagebox.showerror(title="Error", message="Os minutos devem ser um número inteiro entre 0 e 59")

    datastr = f"{dia}/{mes}/{ano} - {hora}:{minutos}"
    date = datetime.strptime(datastr, "%d/%m/%Y - %H:%M")
    cursor.execute('INSERT INTO tarefas (nome, data) VALUES (?, ?)', (nome, date))
    conn.commit()
    tarefas.append({"nome": nome, "data": date})
    printarTarefaF(tarefas[len(tarefas) - 1], len(tarefas) - 1)


def lerTarefa():
    listbox.delete(0, END)
    for index, tarefa in enumerate(tarefas):
        printarTarefaF(tarefa, index)


def deletar_tarefa_evento():
    index = listbox.curselection()[0]
    listbox.delete(index, index + 1)
    task_index = index // 2
    del tarefas[task_index]


def tarefaMaisRecente():
    listbox.delete(0, END)
    tarefas_ordenadas = sorted(tarefas, key=itemgetter('data'))
    printarTarefaF(tarefas_ordenadas[0], 0)


def ultimaTarefa():
    listbox.delete(0, END)
    printarTarefaF(tarefas[-1], 0)


def sair_do_programa():
    sys.exit()


# botoes
button = customtkinter.CTkButton(master=frame, text="Adicionar tarefa", width=300,
                                 command=lambda: adicionar_tarefa_evento()).place(x=25, y=50)
button = customtkinter.CTkButton(master=frame, text="Deletar tarefa", width=300,
                                 command=lambda: deletar_tarefa_evento()).place(x=25, y=90)
button = customtkinter.CTkButton(master=frame, text="Ler tarefas", width=300, command=lambda: lerTarefa()).place(x=25,
                                                                                                                 y=130)
button = customtkinter.CTkButton(master=frame, text="Tarefa mais recente", width=300,
                                 command=lambda: tarefaMaisRecente()).place(x=25, y=170)
button = customtkinter.CTkButton(master=frame, text="Ultima tarefa adicionada", width=300,
                                 command=lambda: ultimaTarefa()).place(x=25, y=210)
button = customtkinter.CTkButton(master=frame, text="Sair do programa", width=300,
                                 command=lambda: sair_do_programa()).place(x=25, y=350)


def button_click_event():
    dialog = customtkinter.CTkInputDialog(text="Digite uma tarefa:")
    print("Sua tarefa:", dialog.get_input())


print(tarefas)
janela.mainloop()
