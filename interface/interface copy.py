import tkinter as tk
from tkinter import filedialog
import pandas as pd

def carregar_arquivo(): #Função responsavel por realizar a captura do arquivo em excel
    # Abre uma janela para selecionar o arquivo
    filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")]) # Metodo responsavel por abrir a caixa de dialogoCarrega o arquivo excel para dentro do codigo
    if filepath: #Verifica se o arquivo foi selecionado 
        # Carrega o arquivo Excel
        df = pd.read_excel(filepath) # Cria o data frame
        # Exibe o conteúdo do DataFrame no console
        print(df)

# Cria a janela principal
root = tk.Tk()
root.title("Carregar Arquivo Excel")

# Define o tamanho da janela (largura x altura)
root.geometry("800x600")

# Cria um botão para carregar o arquivo
btn_carregar = tk.Button(root, text="Carregar Arquivo Excel", command=carregar_arquivo)
btn_carregar.pack(pady=20)

# Inicia o loop da interface gráfica
root.mainloop()
