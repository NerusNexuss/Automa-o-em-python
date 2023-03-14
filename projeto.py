import pyautogui    
import time

#Foi usado o comando a biblioteca pyautogui  
#comando para instalar no console: !pip instal pyautogui

# pyautogui.click -> Clique com o mouse 
# pyautogui.write -> escrever um texte 
# pyautogui.press -> apertar uma tecla 
# pyautogui.hotkey -> apertar uma combinação de tecka (ex: Ctrl + D) 
#pyautogui.position() -> para pegar uma posição do mouse 

pyautogui.POUSE = 5

#Passo 1: entrar no sistema da empresa (no link) 
pyautogui.hotkey("ctrl","t") 
pyautogui.write(" https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter") 

# pode ser que o navegador tenha que carregar 
time.sleep(5)
  

#Passo 2: Fazer login  
# clicar no espaço de login   
pyautogui.click(x=837, y=335) 
# escreve o login
pyautogui.write("meu login")
#Passo 3: Exportar a base de dados
#Passo 4: calcular os indicadores 
#Passo 5: enviar um e-mail para o meu chefe
