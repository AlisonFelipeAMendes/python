#RPA
import pyautogui
import time
     # https://www.tse.jus.br/servicos-eleitorais/autoatendimento-eleitoral#/atendimento-eleitor/consultar-situacao-titulo-eleitor
url = "https://www.tse.jus.br/servicos-eleitorais/autoatendimento-eleitoral#/atendimento-eleitor/consultar-situacao-titulo-eleitor"
cpf = ["456.789.123-45","32784449220","258392092.87", "06241588290"]
pyautogui.PAUSE = 0.6
# Abrir o navegador Chrome
# pyautogui.press("win")
# pyautogui.write("Edge")
# pyautogui.press("enter")

for i in range(len(cpf)):
    # pyautogui.click(x=1378, y=1044)
    pyautogui.click(x=568, y=82)

    pyautogui.write(url)
    pyautogui.press("enter")

    pyautogui.click(x=1363, y=891)
    pyautogui.click(x=229, y=750)
    pyautogui.write(cpf[i])
    print(cpf[i])
    pyautogui.click(x=1805, y=842)
    time.sleep(3)

    pyautogui.click(x=1447, y=445)
    pyautogui.click(x=958, y=765)


    # time.sleep(3)
#pyautogui.click(x=1891, y=9)