from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

opener=req.build_opener()
opener.addheaders= [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

#Html 가져오기
base="https://search.naver.com/search.naver?where=image&sm=tab_jum&query=" #전체 url
quote = rep.quote_plus("사자")  #출력할 해당 글
url=base+quote

res=req.urlopen(url) #url 오픈
savePath="C:/Users/kkddy/Documents/Python_Crawlling/" #내폴더에저장

try :
    if not(os.path.isdir(savePath)) : #savePath 디렉토리 없으면
        os.makedirs(os.path.join(savePath))
except OSError as e : #디렉토리가 있다면
    if e.errno != errno.EEXIST : #파일이 존재 할 경우
        print("Failed to create directory!!")
        raise #컴파일 확인
        #https://python.readthedocs.io/en/latest/library/errno.html 에러내용링크

soup = BeautifulSoup(res, "html.parser")


li_list=soup.select("#main_pack > div > div.photo_group._listGrid > div.photo_tile._grid > div:nth-child(3) > div > div.thumb > a > img")

for i, div in enumerate(li_list,1) :
    print(div)

    fullfilename=os.path.join(savePath,savePath+str(i)+'.jpg')
    print(fullfilename)

    req.urlretrieve(div['data-source'], fullfilename)
    print()

print('다운로드 완료')
