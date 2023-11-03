from bs4 import BeautifulSoup
import re
import requests

site = 'https://www.pcmag.com/picks/the-best-computer-monitors'
response = requests.get(site)
html = response.content
soup = BeautifulSoup(html, "html.parser")

img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png|svg))$', url)
    if not filename:
         print("Regex didn't match with the url: {}".format(url))
         continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)

data = open("index.html", "w")
data.write(str(soup))
data.close()