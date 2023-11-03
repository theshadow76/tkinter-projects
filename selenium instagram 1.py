import selenium.webdriver
import os
from selenium.webdriver.common.keys import Keys

driver = selenium.webdriver.Chrome(executable_path='//Users//vigowalker//Documents//chromedriver//chromedriver95')

driver.get('https://www.instagram.com/')

inp1 = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
inp1.click()
inp1.send_keys("tienda_shadowtech_software")

inp2 = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
inp2.click()
inp2.send_keys("vigoproxd01")

btn1 = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div')
btn1.click()