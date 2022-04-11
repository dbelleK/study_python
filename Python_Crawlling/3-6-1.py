import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#driver=webdriver.PhantomJs('C:/Users/kkddy/Documents/dbelleK_git/study_python/Python_Crawlling/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs')
driver=webdriver.Chrome('C:/Users/kkddy/Documents/dbelleK_git/study_python/Python_Crawlling/chromedriver_win32/chromedriver')

#load가 되지 않은 상태에서 진행시 오류를 발생시키므로 대기시간이 필요
#driver.implicity_wait(5) #5초
driver.get('https://google.com')
#스샷
driver.save_screenshot('C:/Users/kkddy/Documents/Website1.png')


#driver.implicity_wait(5) #5초
driver.get('https://daum.net')
#스샷
driver.save_screenshot('C:/Users/kkddy/Documents/Website2.png')

driver.quit()

print("스크린샷 성공")
