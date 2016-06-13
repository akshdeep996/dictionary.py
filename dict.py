#! import usr/bin/python3
# Dictionary.py : Simple program to find the meaning of given word

import requests
from bs4 import BeautifulSoup

print("Word:")
w = str(input())
print("please wait..... while we get u ur meaning")
res = requests.get("http://www.dictionary.com/browse/" + w)

soup = BeautifulSoup(res.content,"lxml")

print(soup.find_all("div",{"class":"def-content"})[0].text)

