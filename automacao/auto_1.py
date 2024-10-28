from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


# Configuração do Selenium
def automacao ():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get("https://www.tse.jus.br/servicos-eleitorais/autoatendimento-eleitoral#/atendimento-eleitor/consultar-situacao-titulo-eleitor")# Passo 1: Acessar o site
    time.sleep(2)
    navegador.find_element('xpath', '//*[@id="modal-lgpd"]/div/div/div[2]/button').click()
    time.sleep(2)
    navegador.find_element('xpath', '//*[@id="titulo-cpf-nome"]').send_keys("00063914271")# Passo 2: Inserir o CPF
    navegador.find_element('xpath', '//*[@id="modal"]/div/div/div[2]/div[2]/form/div[2]/button[2]').click() # Passo 3: Clicar no botão de consulta
    cpf = navegador.find_element('xpath','//*[@id="content"]/app-root/div/app-consultar-situacao-titulo-eleitor/app-avatar-e-nome/div/div/div/div[2]/p/span').text#Capturar o CPF e o Status
    status = navegador.find_element('xpath','//*[@id="content"]/app-root/div/app-consultar-situacao-titulo-eleitor/div[1]/div[1]/p/span').text


#Fechar o navegador
navegador.quit()

