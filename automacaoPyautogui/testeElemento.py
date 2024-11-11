import pyautogui
import time



time.sleep(3)

# https://www.tse.jus.br/servicos-eleitorais/autoatendimento-eleitoral#/atendimento-eleitor/consultar-situacao-titulo-eleitor
url = "https://www.tse.jus.br/servicos-eleitorais/autoatendimento-eleitoral#/atendimento-eleitor/consultar-situacao-titulo-eleitor"
cpf = "06241588290"


# Abrir o navegador Chrome
pyautogui.press("win")
pyautogui.write("Google Chrome")


time.sleep(1)
pyautogui.press("enter")

pyautogui.write(url)
pyautogui.press("enter")

posicao_cursopython = pyautogui.locateCenterOnScreen("alisonCH.png")
print(posicao_cursopython)
pyautogui.click(posicao_cursopython)




pyautogui.write(cpf)
print(cpf)