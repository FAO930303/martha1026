import requests
from bs4 import BeautifulSoup

url = "https://www1.pu.edu.tw/~tcyang/course.html"
Data = requests.get(url)
Data.encoding = "utf-8"
#print(Data.text)
sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select(".team-box")

for X in result:
	print(X.find("h4").text)
	print(X.find("p").text)
	print(X.find("a").get("href"))
	print("https://www1.pu.edu.tw/~tcyang/"+X.find("img").get("src"))
	print()
