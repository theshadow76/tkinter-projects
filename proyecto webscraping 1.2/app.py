from bs4 import BeautifulSoup
import re
import requests

site = 'https://www.pcmag.com/picks/the-best-computer-monitors'
response = requests.get(site)
html = response.content
soup = BeautifulSoup(html, "html.parser")



'''
data = open("index.txt", "w")
data.write(str(soup.text))
data.close()
'''
