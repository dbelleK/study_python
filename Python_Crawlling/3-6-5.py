import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#CLI(command line interface)로 브라우저 제어
options = Options()
options.binary_location=r'C:/Program Files/Mozilla Firefox/firefox.exe'
# options.headless=True
options.add_argument("-headless")

#눈으로 확인안하고 크롤링C:\Users\kkddy\Documents\dbelleK_git\study_python\Python_Crawlling\geckodriver-v0.30.0-win64
driver=webdriver.Firefox(options=options, executable_path=r'C:/Users/kkddy/Documents/dbelleK_git/study_python/Python_Crawlling/geckodriver-v0.30.0-win64/geckodriver')
#눈으로 확인하면서 크롤링
#driver=webdriver.Chrome('C:/Users/kkddy/Documents/dbelleK_git/study_python/Python_Crawlling/chromedriver_win32/chromedriver')

#driver.set_window_size(1920,1080) #화면크기
driver.get('https://google.com')
#time.sleep(5) #대기
driver.save_screenshot('C:/Users/kkddy/Documents/Website9.png')


#driver.set_window_size(1920,1080)
driver.get('https://daum.net')
#time.sleep(5)
driver.save_screenshot('C:/Users/kkddy/Documents/Website10.png')

driver.quit()

print("스크린샷 성공")
