from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import selenium

options = Options()
options.add_argument('--proxy-server=52.250.1.171:80')

driver = selenium.webdriver.Chrome('/Users/vigowalker/Documents/chromedriver/chromedriver 100')

driver.get('https://www.instagram.com/accounts/emailsignup/')

inp1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[3]/div/label/input")))
inp1.click()
inp1.send_keys("+16465106465")

inp2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[4]/div/label/input")))
inp2.click()
inp2.send_keys("vigo")

inp3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[5]/div/label/input")))
inp3.click()
inp3.send_keys("theshadowNStest")

inp4 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[6]/div/label/input")))
inp4.click()
inp4.send_keys("lagunaVerde03")

btn1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div[7]/div/button")))
btn1.click()

btn2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select")))
btn2.click()
btn2_select = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[7]")))
btn2_select.click()

btn3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select")))
btn3.click()
btn3_slect = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]")))
btn3_slect.click()

btn4 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select")))
btn4.click()
btn4_slect = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]")))
btn4_slect.click()

btn5 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/div[6]/button")))
btn5.click()

btn6 = WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/button")))
btn6.click()