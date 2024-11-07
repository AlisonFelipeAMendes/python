from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
# Passo 1:
navegador.get("https://www.tse.jus.br/servicos-eleitorais/autoatendimento-eleitoral#/atendimento-eleitor/consultar-situacao-titulo-eleitor")


# # Passo 2:
navegador.find_element('xpath','//*[@id="titulo-cpf-nome"]').send_keys("00063914271")

# Passo 3:
navegador.find_element('xpath', '//*[@id="modal"]/div/div/div[2]/div[2]/form/div[2]/button[2]').click()

#CPF
//*[@id="content"]/app-root/div/app-consultar-situacao-titulo-eleitor/app-avatar-e-nome/div/div/div/div[2]/p/span
#Status
//*[@id="content"]/app-root/div/app-consultar-situacao-titulo-eleitor/div[1]/div[1]/p/span