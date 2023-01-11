from datetime import datetime
import tkinter as tk
from tkinter import ttk

tarefas = []


def printarTarefaF(tarefa, index):

    print('-' * 36)
    print(f"{index + 1} = {tarefa['nome']}")
    print(f"Data = {tarefa['data']}")


def adicionarTarefa():


    nome = input("Digite sua tarefa:")
    dia = input("Digite o dia:").strip()
    mes = input("Digite o mês:").strip()
    ano = input("Digite o ano:").strip()
    hora = input("Digite a hora:").strip()
    minutos = input("Digite os minutos:").strip()

    datastr = f"{dia}/{mes}/{ano} - {hora}:{minutos}"
    date = datetime.strptime(datastr, "%d/%m/%Y - %H:%M")

    tarefas.append({"nome": nome, "data": date})


def deletarTarefa():

    print('Deletar tarefa')
    lerTarefa()

    delete = int(input("Digite a tarefa que deseja deletar:"))

    del tarefas[delete - 1]


def lerTarefa():

    for index, tarefa in enumerate(tarefas):

        printarTarefaF(tarefa, index)

def tarefaMaisRecente():

    print('Tarefa mais recente')
    tarefas_ordenadas = sorted(tarefas, key=lambda tarefa: tarefa['data'])
    printarTarefaF(tarefas_ordenadas[0], 0)


def ultimaTarefaAdicionada():

    printarTarefaF(tarefas[-1], len(tarefas) - 1)

while True:

    print('-' * 36)
    print('-' * 15, 'Menu', '-' * 15)
    print('Adicionar tarefas (1)')
    print('Deletar tarefas (2)')
    print('Ler tarefas (3)')
    print('Tarefa mais recente (4)')
    print('Ultima tarefa adicionada (5)')
    print('Sair do programa (6)')
    print('-' * 36)
    escolha = input('Digite o que deseja fazer: ')

    match escolha:

        case "1":
            adicionarTarefa()
        case "2":
            deletarTarefa()
        case "3":
            lerTarefa()
        case "4":
            tarefaMaisRecente()
        case "5":
            ultimaTarefaAdicionada()
        case "6":
            break

        case _:
            print('Opção invalida!')

