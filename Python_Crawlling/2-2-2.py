import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl="http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg"
htmlURL="http://google.com"

savePath1="C:/Users/kkddy/Documents/Python_Crawlling/test1.jpg"
savePath2="C:/Users/kkddy/Documents/Python_Crawlling/index.html"

f=dw.urlopen(imgUrl).read()
f1=dw.urlopen(htmlURL).read()

#방법 1
saveFile1=open(savePath1,'wb') # w : write, r:read,  a:add
saveFile1.write(f)
saveFile1.close()

#방법 2
with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f1)


print('다운로드 완료')
