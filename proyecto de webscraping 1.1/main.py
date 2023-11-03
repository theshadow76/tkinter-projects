import requests
from bs4 import BeautifulSoup

url = 'https://towardsdatascience.com/why-python-is-not-the-programming-language-of-the-future-30ddc5339b66'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")

article = soup.find('article', class_ = "meteredContent")
txt = article.find_all("h1")
txt2 = article.find_all("h2")
txt3 = article.find_all("h3")
txt4 = article.find_all("h4")
txt5 = article.find_all("h5")
txt6 = article.find_all("h6")
txt7 = article.find_all("p")
print(txt)
print(txt2)
print(txt3)
print(txt4)
print(txt5)
print(txt6)
print(txt7)