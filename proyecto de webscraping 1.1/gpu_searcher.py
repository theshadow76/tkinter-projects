from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import selenium
import requests
from bs4 import BeautifulSoup

url = input("Hola porfavor, pon el link donde quieres extraer todo el texto de: ")
print("selecione uno de las siguentes opciones: ")
h1 = print("1. h1")
h2 = print("1. h2")
h3 = print("1. h3")
h4 = print("1. h4")
h5 = print("1. h5")
h6 = print("1. h6")
p = print("1. p")
result = input("escriba aqui: ")

response = requests.get(url)
html = response.content

while (result == "1"):
    soup = BeautifulSoup(html, "html.parser")
    h1_1 = soup.find("h1")
    print(h1_1)
    break