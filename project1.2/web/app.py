from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import selenium

driver = selenium.webdriver.Chrome('/Users/vigowalker/Documents/chromedriver/chromedriver95')

link1 = driver.get('https://zefoy.com/')

while True:
    inp1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button")))
    inp1.click()

    inp2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/form/div/input")))
    inp2.click()
    inp2.send_keys('https://www.tiktok.com/@vigo_walker/video/7019664881121037573?is_copy_url=1&is_from_webapp=v1')

    btn1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/form/div/div/button")))
    btn1.click()