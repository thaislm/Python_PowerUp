import pyautogui
import time

# pyautogui.click -> clicar em algum lugar 
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.kotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 0.5 


# Passo 1: Entrar no sistema da empresa - URL
# Abrir o Chrome

pyautogui.press("win")
pyautogui.write("chrome") 

pyautogui.press("enter")


#digitar o site thaismelo0608@gmail.com flathaismelo0608@gmail.com  flamengo123 
# mengo123 


pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#espera 3 segundos
time.sleep(2) #somente esperar depois desse determinado código

# Passo 2: Fazer login
pyautogui.click(x=405, y=370)
pyautogui.write("thaismelo0608@gmail.com")

#preencher a senha 
pyautogui.press("tab")
pyautogui.write("flamengo123")

#botao logar

pyautogui.press("tab")
pyautogui.press("enter")

#espera de 2 segundos

time.sleep(2)

# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar 1 produto

for linha in tabela.index:
  
  pyautogui.click(x=426, y=265)

  codigo  = tabela.loc[linha,"codigo"]
  pyautogui.write(codigo)

  pyautogui.press("tab") #passar para o próximo campo
  marca = tabela.loc[linha,"marca"]
  pyautogui.write(marca)

  pyautogui.press("tab")
  tipo = tabela.loc[linha,"tipo"]
  pyautogui.write(tipo)

  pyautogui.press("tab")
  categoria = str(tabela.loc[linha,"categoria"])
  pyautogui.write(categoria)

  pyautogui.press("tab")
  preco_unitario = str(tabela.loc[linha,"preco_unitario"])
  pyautogui.write(preco_unitario)

  pyautogui.press("tab")
  custo = str(tabela.loc[linha,"custo"])
  pyautogui.write(custo)

  pyautogui.press("tab")
  obs = str(tabela.loc[linha,"obs"])
  if obs != "nan1":
    pyautogui.write(obs)

  pyautogui.press("tab")  # Passou para o botao de enviar
  pyautogui.press("enter")

  pyautogui.scroll(10000)
