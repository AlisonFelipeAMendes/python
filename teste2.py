import tkinter as tk
from tkinter import messagebox, filedialog, Toplevel
import pyautogui
import time
import pyperclip
import openpyxl
from datetime import datetime
from PIL import Image, ImageTk
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\felipe.mendes\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'

# Dicionário para armazenar as coordenadas de cada campo
coordenadas = {
    "CPF": None, 
    "AGÊNCIA": None, 
    "CONTA": None, 
    "ABA": None, 
    "DESTINO_CPF": None, 
    "DESTINO_AGENCIA": None, 
    "DESTINO_CONTA": None, 
    "AVANÇAR": None
}

# Listas para armazenar os conteúdos copiados
cpf_list = []
agencia_list = []
conta_list = []

# Função para capturar a posição do clique
def capture_click(field):
    time.sleep(2)  # Tempo para mover o cursor ao local desejado
    x, y = pyautogui.position()
    coordenadas[field] = (x, y)
    messagebox.showinfo("Posição Capturada", f"Posição {field} capturada: {x}, {y}")

# Função para executar os cliques nas coordenadas capturadas e copiar o conteúdo
def execute_clicks():
    for _ in range(len(cpf_list)):
        # Selecionar a aba do navegador
        if coordenadas["ABA"]:
            pyautogui.click(coordenadas["ABA"])
            time.sleep(0.5)  # Tempo para selecionar a aba
        
        # Colar o conteúdo de CPF, Agência e Conta em seus respectivos destinos
        if coordenadas["DESTINO_CPF"]:
            pyautogui.click(coordenadas["DESTINO_CPF"])
            time.sleep(0.5)
            pyperclip.copy(cpf_list.pop(0))
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
        
        if coordenadas["DESTINO_AGENCIA"]:
            pyautogui.click(coordenadas["DESTINO_AGENCIA"])
            time.sleep(0.5)
            pyperclip.copy(agencia_list.pop(0))
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
        
        if coordenadas["DESTINO_CONTA"]:
            pyautogui.click(coordenadas["DESTINO_CONTA"])
            time.sleep(0.5)
            pyperclip.copy(conta_list.pop(0))
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
        
        # Avançar
        if coordenadas["AVANÇAR"]:
            pyautogui.click(coordenadas["AVANÇAR"])
            time.sleep(0.5)

# Função para exportar os dados para um arquivo Excel
def export_data():
    # Obtendo a data atual
    today = datetime.today().strftime('%Y-%m-%d')
    suggested_filename = f"dados_exportados_{today}.xlsx"
    
    # Abrindo a caixa de diálogo para salvar o arquivo com a data sugerida
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")], initialfile=suggested_filename)
    
    if file_path:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Dados Exportados"

        # Escrevendo os dados nas colunas
        sheet["A1"] = "CPF"
        sheet["B1"] = "AGÊNCIA"
        sheet["C1"] = "CONTA"

        for i, (cpf, agencia, conta) in enumerate(zip(cpf_list, agencia_list, conta_list), start=2):
            sheet[f"A{i}"] = cpf
            sheet[f"B{i}"] = agencia
            sheet[f"C{i}"] = conta

        workbook.save(file_path)
        messagebox.showinfo("Exportação", f"Dados exportados com sucesso para '{file_path}'!")

# Função para abrir a janela de captura de coordenadas
def open_coordinates_window():
    coords_window = Toplevel(brima)
    coords_window.title("Capturar Coordenadas")
    coords_window.geometry("200x400")
    brima.resizable(False, False)
    brima.iconbitmap(r"C:/Projetos/python/BRIMA/brima.ico")  # Use 'r' para cadeias de caracteres brutas

    # Botão para capturar a posição do clique para CPF
    capture_button_cpf = tk.Button(coords_window, text="Capturar Posição CPF", command=lambda: capture_click("CPF"), relief="solid", borderwidth=1)
    capture_button_cpf.pack(pady=10)

    # Botão para capturar a posição do clique para AGÊNCIA
    capture_button_agencia = tk.Button(coords_window, text="Capturar Posição AGÊNCIA", command=lambda: capture_click("AGÊNCIA"), relief="solid", borderwidth=1)
    capture_button_agencia.pack(pady=10)

    # Botão para capturar a posição do clique para CONTA
    capture_button_conta = tk.Button(coords_window, text="Capturar Posição CONTA", command=lambda: capture_click("CONTA"), relief="solid", borderwidth=1)
    capture_button_conta.pack(pady=10)
    
    # Botão para capturar a posição do clique para ABA
    capture_button_aba = tk.Button(coords_window, text="Capturar Posição ABA", command=lambda: capture_click("ABA"), relief="solid", borderwidth=1)
    capture_button_aba.pack(pady=10)

    # Botão para capturar a posição do clique para DESTINO_CPF
    capture_button_destino_cpf = tk.Button(coords_window, text="Capturar Posição DESTINO CPF", command=lambda: capture_click("DESTINO_CPF"), relief="solid", borderwidth=1