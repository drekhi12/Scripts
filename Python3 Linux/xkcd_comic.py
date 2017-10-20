import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import subprocess

url='https://xkcd.com/'
for i in range (int(sys.argv[1])):
    temp = urllib3.PoolManager()
    load = temp.request('get',url)
    view = BeautifulSoup(load.data, 'lxml')
    tags = view.findAll('img')
    subprocess.run(['mkdir','-p',sys.argv[2]])
   # print(tags.content)
    tag = tags[1]
    link = "http:" + tag.get('src')
    img=requests.get(link)
    image=img.content
    filename=link.split('/')[-1]
    output=open(sys.argv[2] + "/" + filename,'wb')
    output.write(image)
    output.close()
    ptags = view.findAll('ul', 'comicNav')
    plist = ptags[1]
    ptag = plist.findAll('a')
    ptag = ptag[1]
    plink = ptag.get('href')

    #open_prev
    url='https://xkcd.com' + plink
    i=i+1
#+END_SRC
	** backup.py
#+BEGIN_SRC python :tangle backup.py
import json
import sys
import subprocess
json_data = open("list.json","r")
d = json.load(json_data)
l=len(d)
for i in range(l):
    if sys.argv[1] == "backup":
        cmd=['cp',d[i][0],d[i][1]]
        subprocess.call(cmd)
    if sys.argv[1] == "restore":
        cmd=['cp',d[i][1],d[i][0]]
        subprocess.call(cmd)
    if sys.argv[1] == "push":
        cmd=['git','add',d[i][1]]
        subprocess.call(cmd)
        subprocess.call(['git','commit','-m','backup'])
        subprocess.call(['git','push'])




json_data.close()
