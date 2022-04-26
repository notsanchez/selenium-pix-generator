from cgitb import text
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import webbrowser
import time 
import clipboard
import os
import urllib.request
import pyimgur

CLIENT_ID = "65e4214d4f2cf06"

os.system("cls")

PATH = "./resources/chromedriver.exe"

while True:
    print("Qual o tipo da chave: ")
    print("[1] - telefone")
    print("[2] - Email")
    print("[3] - CPF")
    print("[4] - CNPJ")

    tipo = input("Qual o tipo da chave: ")
    os.system("cls")
    chave = input("Sua chave: ")
    os.system("cls")
    nome = input("Digite o nome do beneficiario: ")
    os.system("cls")
    valor = input("Digite o valor para transferecia (EXEMPLO: 10,00): ")
    os.system("cls")

    chromeOptions = Options()
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument('--disable-gpu')

    driver = webdriver.Chrome(PATH, chrome_options=chromeOptions)

    driver.get("https://gerarqrcodepix.com.br/")

    os.system("cls")

    time.sleep(1)


    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/div[1]/input'))).send_keys(nome)


    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/div[2]/input'))).send_keys("Brasil")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/label[1]'))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[4]/label[1]'))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[4]/div/input'))).send_keys(valor)


    if tipo == "1":
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[5]/div/div[2]/label'))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[5]/div/div[2]/input'))).send_keys(chave)

    elif tipo == "2":
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[5]/div/div[1]/label'))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[5]/div/div[1]/input'))).send_keys(chave)

    elif tipo == "3":
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[5]/div/div[3]/label'))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[5]/div/div[3]/input'))).send_keys(chave)

    elif tipo == "4":
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[5]/div/div[3]/label'))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[5]/div/div[3]/input'))).send_keys(chave)


    text = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div').text

    time.sleep(2)

    img_link = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/img')
    src = img_link.get_attribute('src')

    driver.close()

    os.system("cls")

    print("O código pix é: "+text)
    print("Já está no seu CTRL+V ;)")

    clipboard.copy(text)

    print("")

    print("[1] - SIM")
    print("[2] - NÃO")
    opcao = input("Abrir QR CODE?: ")

    if opcao == "1":
        urllib.request.urlretrieve(src, "./resources/qr-code.png")
        PATH2 = "./resources/qr-code.png"

        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(PATH2, title="QR-CODE")

        os.system("cls")

        link = uploaded_image.link

        print("")

        webbrowser.open(link)

    else:
        pass
        os.system("cls")
