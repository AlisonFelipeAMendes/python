#RPA
import pyautogui
import time

pyautogui.PAUSE = 0.3

# Abrir o navegador Chrome
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")

time.sleep(1)

# Acessar o site
pyautogui.write("hashtagtreinamentos.com")
pyautogui.press("enter")

time.sleep(3)

# Localizar e clicar no ícone do curso de Python
posicao_cursopython = pyautogui.locateCenterOnScreen("cursopython.png")
pyautogui.click(posicao_cursopython)

time.sleep(3)

# Rolar a página e preencher um formulário
pyautogui.scroll(-200)
pyautogui.click(x=441, y=870)
pyautogui.write("Lira")
pyautogui.press("tab")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")

# Continuar preenchendo o formulário
pyautogui.write("SenhaSegura123")
pyautogui.press("tab")
pyautogui.write("SenhaSegura123")
pyautogui.press("enter")

# Finalizar a automação
time.sleep(2)
pyautogui.alert("Automação concluída!")
