import sys
import io
from selenium import webdriver
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver=webdriver.Chrome('C:/Users/kkddy/Documents/dbelleK_git/study_python/Python_Crawlling/chromedriver_win32/chromedriver')

driver.set_window_size(1920,1080) #화면크기
driver.get('https://google.com')
time.sleep(5) #대기
driver.save_screenshot('C:/Users/kkddy/Documents/Website5.png')


driver.set_window_size(1920,1080)
driver.get('https://daum.net')
time.sleep(5)
driver.save_screenshot('C:/Users/kkddy/Documents/Website6.png')

driver.quit()

print("스크린샷 성공")
