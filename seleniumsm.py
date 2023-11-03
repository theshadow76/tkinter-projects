from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import selenium

driver = selenium.webdriver.Chrome('/Users/vigowalker/Documents/chromedriver/chromedriver95')

link1 = driver.get('https://www.instagram.com/')

inp1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")))
inp1.click()
inp1.send_keys("tienda_shadowtech_software")

inp2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")))
inp2.click()
inp2.send_keys("vigoproxd01")

btn1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/section/main/div/div/div[1]/div/form/div/div[3]/button")))
btn1.click()
