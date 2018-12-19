# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib.request

URL = "http://azurlane.wikiru.jp/index.php?%A5%AD%A5%E3%A5%E9%A5%AF%A5%BF%A1%BC%2F%B4%CF%BC%EF%CA%CC"
images = []
links = []
urls = []

res = requests.get(URL, timeout = 2000)

soup = BeautifulSoup(res.content, "lxml")

soup = soup.find_all("td")

soup = soup[8:-2]
for link in soup:
    try:
        links.append(link.find_all("a")[0])
    except:
        continue

for a in links:
    urls.append(a.get("href"))

for url in urls:
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "lxml")
    for li in soup.find_all("img"):
        if li.get("src").endswith(".gif"):
            fname = li.get("src")
            print("get " + fname)
            re = requests.get( "http://azurlane.wikiru.jp/" + fname)
            with open(fname.split("/")[-1], "wb") as f:
                f.write(re.content)
                print("saving " + fname.split("/")[-1])

"""
for link in soup.find_all("img"):
    if link.get("src").endswith(".gif"):
        print("get " + str(link))
        images.append(link.get("src"))

    if link.get("src").endswith(".jpg"):
        print("get " + str(link))
        images.append(link.get("src"))

    elif link.get("src").endswith(".png"):
        print("get " + str(link))
        images.append(link.get("src"))
    #elif link.get("src").endswith("/show"):
    #    images.append(link.get("src").replace("/show",""))

for target in images:
    #target = "http://imas.gamedbs.jp" + target
    try:
        re = requests.get(target)
        with open(target.split("/")[-1], "wb") as f:
            f.write(re.content)
            print("saving " + re)
    except:
        continue
"""
