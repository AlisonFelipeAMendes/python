import tkinter as tk
from tkinter import filedialog
import pandas as pd


def carregar_arquivo():  # Função responsável por realizar a captura do arquivo em Excel
    # Abre uma janela para selecionar o arquivo
    filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])  # Método responsável por abrir a caixa de diálogo e carregar o arquivo Excel para dentro do código
    if filepath:  # Verifica se o arquivo foi selecionado
        # Carrega o arquivo Excel
        df = pd.read_excel(filepath)  # Cria o DataFrame
        # Vetores para armazenar os dados das duas colunas
        col1 = []
        col2 = []
        # Itera sobre cada linha do DataFrame
        for i in range(len(df)):
            col1.append(df.iloc[i, 0])  # Adiciona o valor da primeira coluna ao vetor col1
           # col2.append(df.iloc[i, 1])  # Adiciona o valor da segunda coluna ao vetor col2
       ## # Exibe os vetores no console
        ##print("Coluna 1:", col1)
        print(col1)
       ## print("Coluna 2:", col2)

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
