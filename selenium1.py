import selenium.webdriver
import os
from selenium.webdriver.common.keys import Keys
#os.chmod('//Users//vigowalker//Documents//chromedriver', 755)

driver = selenium.webdriver.Chrome(executable_path='//Users//vigowalker//Documents//chromedriver//chromedriver95')

driver.get("https://www.winpy.cl/")

inp1 = driver.find_element_by_xpath('/html/body/header/div/form/input')
inp1.click()
inp1.send_keys("rtx 3090")
inp1.send_keys(Keys.ENTER)


