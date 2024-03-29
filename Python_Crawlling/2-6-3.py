from bs4 import BeautifulSoup
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp=open("C:/Users/kkddy/Documents/Python_Crawlling/cars.html", encoding="utf-8")
soup=BeautifulSoup(fp, "html.parser")
print(soup)

def car_func(select):
    print("car_func", soup.select_one(select).string)

#람다식(q : 매개변수)
car_lambda=lambda q: print("car_func", soup.select_one(q).string)

car_func("#gr")
car_func("li#gr")
car_func("ul>li#gr")
car_func("#cars #gr")
car_func("#cars > #gr")
car_func("li[id='gr']")

print("--------------------------------------------------")
car_lambda("#gr")
car_lambda("li#gr")
car_lambda("ul>li#gr")
car_lambda("#cars #gr")
car_lambda("#cars > #gr")
car_lambda("li[id='gr']")

print("---------------------------------------------------")
print("car_func",soup.select("li")[3].string)
print("car_func",soup.find_all("li")[3].string)
