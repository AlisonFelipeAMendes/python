#RPA
import pyautogui
import time

pyautogui.PAUSE = 0.3

#https://www.tse.jus.br/servicos-eleitorais/autoatendimento-eleitoral#/atendimento-eleitor/consultar-situacao-titulo-eleitor





# Abrir o navegador Chrome
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")

pyautogui.write("https://www.tse.jus.br/servicos-eleitorais/autoatendimento-eleitoral#/atendimento-eleitor/consultar-situacao-titulo-eleitor")
pyautogui.press("enter")