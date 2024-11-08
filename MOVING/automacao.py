import time
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from openpyxl import Workbook


def carregar_arquivo():  # Função responsável por realizar a captura do arquivo em Excel
    global df
    # Abre uma janela para selecionar o arquivo
    filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])  # Método responsável por abrir a caixa de diálogo e carregar o arquivo Excel para dentro do código
    if filepath:  # Verifica se o arquivo foi selecionado
        # Carrega o arquivo Excel
        df = pd.read_excel(filepath)  # Cria o DataFrame
        
       
        # Itera sobre cada linha do DataFrame
        for i in range(len(df)):
            col1.append(df.iloc[i, 0])  # Adiciona o valor da primeira coluna ao vetor col1