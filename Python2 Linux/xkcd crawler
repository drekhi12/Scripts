import requests
from io import BytesIO
import sys
import os
from PIL import Image
from bs4 import BeautifulSoup


def func():
    n = int(sys.argv[1])
    path = sys.argv[2]
    url = "https://xkcd.com/"
    temp = url

    if not os.path.isdir(path):
        os.mkdir(path)

    path += "/"
    for i in range(0, n):
        req = requests.get(temp)
        page = req.text
        soup = BeautifulSoup(page, 'html.parser')
        prev = soup.find(id='middleContainer').find('ul').find_all('li')[1].find('a').get('href')
        prev = prev[1:-1]
        img_div = soup.find(id='comic')
        img_tag = img_div.find('img')
        img_link = img_tag.get('src')
        img_name = img_tag.get('alt') + '.png'
        img_url = 'https:' + img_link
        temp = url + '/' + str(prev) + '/'
        raw_image = requests.get(img_url)
        img = Image.open(BytesIO(raw_image.content))
        img.save(path + img_name, 'png')
