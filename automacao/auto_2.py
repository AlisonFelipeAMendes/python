from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import openpyxl
import time

# Configuração do Selenium
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Passo 1: Acessar o site
navegador.get("https://www.tse.jus.br/servicos-eleitorais/autoatendimento-eleitoral#/atendimento-eleitor/consultar-situacao-titulo-eleitor")

# Passo 2: Aceitar os termos
WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-lgpd"]/div/div/div[2]/button'))).click()

# Passo 3: Inserir o CPF
navegador.find_element(By.XPATH, '//*[@id="titulo-cpf-nome"]').send_keys("00063914271")

# Passo 4: Clicar no botão de consulta
navegador.find_element(By.XPATH, '//*[@id="modal"]/div/div/div[2]/div[2]/form/div[2]/button[2]').click()

# Esperar a página carregar
WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/app-root/div/app-consultar-situacao-titulo-eleitor/app-avatar-e-nome/div/div/div/div[2]/p/span')))

# Capturar o CPF e o Status
cpf = navegador.find_element(By.XPATH, '//*[@id="content"]/app-root/div/app-consultar-situacao-titulo-eleitor/app-avatar-e-nome/div/div/div/div[2]/p/span').text
status = navegador.find_element(By.XPATH, '//*[@id="content"]/app-root/div/app-consultar-situacao-titulo-eleitor/div[1]/div[1]/p/span').text


avegador.find_element('xpath', '//*[@id="content"]/app-root/div/app-consultar-situacao-titulo-eleitor/app-avatar-e-nome/div/div/button/fa-icon/svg/path').click()


print(f"CPF: {cpf} - Status: {status}")


# Fechar o navegador
navegador.quit()

# # Criar um novo arquivo Excel ou abrir um existente
# arquivo_excel = 'c:/PROGRAMACAO/PYTHON/automacao/situacao_eleitoral.xlsx'
# try:
#     workbook = openpyxl.load_workbook(arquivo_excel)
#     sheet = workbook.active
# except FileNotFoundError:
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active
#     sheet.append(['CPF', 'Status'])  # Adicionar cabeçalhos se o arquivo for novo

# # Adicionar os dados na planilha
# sheet.append([cpf, status])

# # Salvar o arquivo Excel
# workbook.save(arquivo_excel)

# print("Dados salvos com sucesso na planilha 'situacao_eleitoral.xlsx'")
