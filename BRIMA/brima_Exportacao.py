import tkinter as tk
from tkinter import messagebox, filedialog
import pyautogui
import time
import pyperclip
import openpyxl
from datetime import datetime

# Dicionário para armazenar as coordenadas de cada campo
coordenadas = {"CPF": None, "AGÊNCIA": None, "CONTA": None} # None no Python representa a ausência de um valor

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

# Função para exibir as coordenadas capturadas
def show_coordinates():
    for field, coord in coordenadas.items():
        coord_label = tk.Label(brima, text=f"Coordenada {field}: {coord}")
        coord_label.pack()

# Função para executar os cliques nas coordenadas capturadas e copiar o conteúdo
def execute_clicks():
    if coordenadas["CPF"]:
        pyautogui.doubleClick(coordenadas["CPF"])
        time.sleep(0.5)  # Tempo para o duplo clique
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)  # Tempo para copiar o conteúdo
        cpf_list.append(pyperclip.paste())

    if coordenadas["AGÊNCIA"]:
        pyautogui.doubleClick(coordenadas["AGÊNCIA"])
        time.sleep(0.5)  # Tempo para o duplo clique
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)  # Tempo para copiar o conteúdo
        agencia_list.append(pyperclip.paste())

    if coordenadas["CONTA"]:
        pyautogui.doubleClick(coordenadas["CONTA"])
        time.sleep(0.5)  # Tempo para o duplo clique
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)  # Tempo para copiar o conteúdo
        conta_list.append(pyperclip.paste())

    # Exibir conteúdo copiado
    messagebox.showinfo("Conteúdo Copiado", f"CPF: {cpf_list}\nAGÊNCIA: {agencia_list}\nCONTA: {conta_list}")

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

# Criar a janela principal
brima = tk.Tk()
brima.iconbitmap(r"C:\PROGRAMACAO\PYTHON\BRIMA\brima.ico")  # Use 'r' para cadeias de caracteres brutas
brima.title("Brima")
brima.geometry("200x300")  # Define o tamanho da janela (largura x altura)
brima.configure(background='blue')

# Adicionar um rótulo para visualizar melhor a cor de fundo
label = tk.Label(brima, text="Automatizador", bg='blue', fg='white', font=("Helvetica", 16, "bold"))
label.pack(pady=15)

# Botão para capturar a posição do clique para CPF
capture_button_cpf = tk.Button(brima, text="Capturar Posição CPF", command=lambda: capture_click("CPF"))
capture_button_cpf.pack(pady=10)

# Botão para capturar a posição do clique para AGÊNCIA
capture_button_agencia = tk.Button(brima, text="Capturar Posição AGÊNCIA", command=lambda: capture_click("AGÊNCIA"))
capture_button_agencia.pack(pady=10)

# Botão para capturar a posição do clique para CONTA
capture_button_conta = tk.Button(brima, text="Capturar Posição CONTA", command=lambda: capture_click("CONTA"))
capture_button_conta.pack(pady=10)

# Botão para exibir as coordenadas capturadas
show_button = tk.Button(brima, text="Mostrar Coordenadas", command=show_coordinates)
show_button.pack(pady=10)

# Botão para executar os cliques
execute_button = tk.Button(brima, text="Iniciar", command=execute_clicks)
execute_button.pack(pady=10)

# Botão para exportar os dados para um arquivo Excel
export_button = tk.Button(brima, text="Exportar Dados", command=export_data)
export_button.pack(pady=10)

# Iniciar a aplicação
brima.mainloop()
