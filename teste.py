import tkinter as tk
from tkinter import messagebox
import pyautogui
import time

# Listas para armazenar as coordenadas de cada campo
coordinates_cpf = []
coordinates_agencia = []
coordinates_conta = []

# Função para capturar a posição do clique para CPF
def capture_click_cpf():
    time.sleep(2)  # Tempo para mover o cursor ao local desejado
    x, y = pyautogui.position()
    coordinates_cpf.append((x, y))
    messagebox.showinfo("Posição Capturada", f"Posição CPF capturada: {x}, {y}")

# Função para capturar a posição do clique para AGÊNCIA
def capture_click_agencia():
    time.sleep(2)  # Tempo para mover o cursor ao local desejado
    x, y = pyautogui.position()
    coordinates_agencia.append((x, y))
    messagebox.showinfo("Posição Capturada", f"Posição AGÊNCIA capturada: {x}, {y}")

# Função para capturar a posição do clique para CONTA
def capture_click_conta():
    time.sleep(2)  # Tempo para mover o cursor ao local desejado
    x, y = pyautogui.position()
    coordinates_conta.append((x, y))
    messagebox.showinfo("Posição Capturada", f"Posição CONTA capturada: {x}, {y}")

# Função para exibir as coordenadas capturadas
def show_coordinates():
    for idx, coord in enumerate(coordinates_cpf):
        coord_label = tk.Label(root, text=f"Coordenada CPF {idx+1}: {coord}")
        coord_label.pack()

    for idx, coord in enumerate(coordinates_agencia):
        coord_label = tk.Label(root, text=f"Coordenada AGÊNCIA {idx+1}: {coord}")
        coord_label.pack()

    for idx, coord in enumerate(coordinates_conta):
        coord_label = tk.Label(root, text=f"Coordenada CONTA {idx+1}: {coord}")
        coord_label.pack()

# Função para executar os cliques nas coordenadas capturadas
def execute_clicks():
    for coord in coordinates_cpf:
        pyautogui.click(coord)
        time.sleep(1)  # Tempo entre os cliques

    for coord in coordinates_agencia:
        pyautogui.click(coord)
        time.sleep(1)  # Tempo entre os cliques

    for coord in coordinates_conta:
        pyautogui.click(coord)
        time.sleep(1)  # Tempo entre os cliques

# Criar a janela principal
root = tk.Tk()
root.title("Capturador de Coordenadas")

# Botão para capturar a posição do clique para CPF
capture_button_cpf = tk.Button(root, text="Capturar Posição CPF", command=capture_click_cpf)
capture_button_cpf.pack(pady=10)

# Botão para capturar a posição do clique para AGÊNCIA
capture_button_agencia = tk.Button(root, text="Capturar Posição AGÊNCIA", command=capture_click_agencia)
capture_button_agencia.pack(pady=10)

# Botão para capturar a posição do clique para CONTA
capture_button_conta = tk.Button(root, text="Capturar Posição CONTA", command=capture_click_conta)
capture_button_conta.pack(pady=10)

# Botão para exibir as coordenadas capturadas
show_button = tk.Button(root, text="Mostrar Coordenadas", command=show_coordinates)
show_button.pack(pady=10)

# Botão para executar os cliques
execute_button = tk.Button(root, text="Executar Cliques", command=execute_clicks)
execute_button.pack(pady=10)

# Iniciar a aplicação
root.mainloop()
