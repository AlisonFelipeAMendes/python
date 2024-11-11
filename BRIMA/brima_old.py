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
    "CPF_DESTINO": None,
    "AGÊNCIA_DESTINO": None,
    "CONTA_DESTINO": None,
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
    while cpf_list and agencia_list and conta_list:
        # Selecionar a aba do navegador
        if coordenadas["ABA"]:
            pyautogui.click(coordenadas["ABA"])
            time.sleep(0.5)  # Tempo para selecionar a aba
        
        # Variáveis locais para armazenar os dados copiados
        cpf = cpf_list.pop(0)
        agencia = agencia_list.pop(0)
        conta = conta_list.pop(0)
        
        # Colar o conteúdo de CPF
        if coordenadas["CPF_DESTINO"]:
            pyautogui.click(coordenadas["CPF_DESTINO"])
            time.sleep(0.5)
            pyperclip.copy(cpf)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
        
        # Colar o conteúdo de Agência
        if coordenadas["AGÊNCIA_DESTINO"]:
            pyautogui.click(coordenadas["AGÊNCIA_DESTINO"])
            time.sleep(0.5)
            pyperclip.copy(agencia)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
        
        # Colar o conteúdo de Conta
        if coordenadas["CONTA_DESTINO"]:
            pyautogui.click(coordenadas["CONTA_DESTINO"])
            time.sleep(0.5)
            pyperclip.copy(conta)
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
    coords_window.geometry("300x500")
    coords_window.resizable(False, False)
    coords_window.iconbitmap(r"C:/Projetos/python/BRIMA/brima.ico")  # Use 'r' para cadeias de caracteres brutas

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

    # Botão para capturar a posição do clique para CPF DESTINO
    capture_button_cpf_destino = tk.Button(coords_window, text="Capturar Destino CPF", command=lambda: capture_click("CPF_DESTINO"), relief="solid", borderwidth=1)
    capture_button_cpf_destino.pack(pady=10)

    # Botão para capturar a posição do clique para AGÊNCIA DESTINO
    capture_button_agencia_destino = tk.Button(coords_window, text="Capturar Destino AGÊNCIA", command=lambda: capture_click("AGÊNCIA_DESTINO"), relief="solid", borderwidth=1)
    capture_button_agencia_destino.pack(pady=10)

    # Botão para capturar a posição do clique para CONTA DESTINO
    capture_button_conta_destino = tk.Button(coords_window, text="Capturar Destino CONTA", command=lambda: capture_click("CONTA_DESTINO"), relief="solid", borderwidth=1)
    capture_button_conta_destino.pack(pady=10)

    # Botão para capturar a posição do clique para AVANÇAR
    capture_button_avancar = tk.Button(coords_window, text="Capturar Posição AVANÇAR", command=lambda: capture_click("AVANÇAR"), relief="solid", borderwidth=1)
    capture_button_avancar.pack(pady=10)

# Criar a janela principal
brima = tk.Tk()
brima.iconbitmap(r"C:/Projetos/python/BRIMA/brima.ico")  # Use 'r' para cadeias de caracteres brutas
brima.title("Brima")
brima.geometry("300x400")
brima.resizable(False, False)

# Carregar a imagem do rótulo
logo_image = Image.open("C:/Projetos/python/BRIMA/brima.png")
logo_photo = ImageTk.PhotoImage(logo_image)

# Criar uma frame transparente para adicionar os widgets
frame = tk.Frame(brima, bg='white', highlightbackground='white', highlightthickness=0, bd=0)
frame.place(relwidth=1, relheight=1)

# Adicionar a imagem como rótulo
logo_label = tk.Label(frame, image=logo_photo, bg='white')
logo_label.pack(pady=15)

# Botão para abrir a janela de captura de coordenadas
coords_button = tk.Button(frame, text="Coordenadas", command=open_coordinates_window, relief="solid", borderwidth=1)
coords_button.pack(pady=10)

# Comentada - Botão para exibir as coordenadas capturadas
# show_button = tk.Button(frame, text="Mostrar Coordenadas", command=show_coordinates)
# show_button.pack(pady=10)

# Botão para executar os cliques
execute_button = tk.Button(frame, text="Iniciar", command=execute_clicks, relief="solid", borderwidth=1)
execute_button.pack(pady=10)

# Botão para exportar os dados para um arquivo Excel
export_button = tk.Button(frame, text="Exportar Dados", command=export_data, relief="solid", borderwidth=1)
export_button.pack(pady=10)

version_label = tk.Label(frame, text="Versão 1.0\nSetor de Tecnologia Brima", bg='white', fg='black', font=("Helvetica", 8), anchor='center')
version_label.pack(side="bottom", pady=10, fill='x')

# Iniciar a aplicação
brima.mainloop()
