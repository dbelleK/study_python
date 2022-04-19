import sys
import io
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
#이미지 다운 라이브러리
import urllib.request as req
#이미지 바이트 처리
from io import BytesIO
#엑셀
import xlsxwriter

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 크롬 옵션
chrome_option=Options()
# headeless 모드 설정
chrome_option.add_argument("--headeless")
#사우드 설정
chrome_option.add_argument("--mute-audio")

# headeless 모드 적용
#browser=webdriver.Chrome(option=chrome_option,'D:/Python_2022/chrome/chromedriver.exe')

# 일반 모드
browser=webdriver.Chrome('D:/Python_2022/chrome/chromedriver.exe')

# 엑셀 파일 생성
workbook = xlsxwriter.Workbook('D:/Python_2022/data/you_crawl_result.xlsx')

#워크시트
worksheet  = workbook.add_worksheet()

#크롬 브라우저 내부 대기
browser.implicitly_wait(5)

#브라우저 사이즈
#minimize_window() : #최소화
#manimize_window() : #최대화
browser.set_window_size(1920,1280)


#페이지
browser.get('https://www.youtube.com/watch?v=8CHp4j6bbaQ')

# 5초
time.sleep(5)

# 포커스 맞추기 위한 페이지 다운
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'html'))).send_keys(Keys.PAGE_DOWN)

#2초 대기
time.sleep(2)

#페이지 이동 시 새로운 데이터 수신 완료를 위한 대기 시간
scroll_pause_time=4

#화면의 높이 설정
last_height = browser.execute_script("return document.documentElement.scrollHeight")

print()

#모든 댓글 데이터가 수신(랜더링) 완료될 때까지 무한 반복

while True :
    #스크롤바 이동
    browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
    #대기
    time.sleep(scroll_pause_time)
    #스크롤바 이동 -> 새로운 데이터 랜더링 -> 현재 높이 추출하기
    new_height = browser.execute_script("return document.documentElement.scrollHeight")

    #이전 높이와 새로운 높이 비교
    print("Last Height: {}, Current Height : {}".format(last_height,new_height))

    # 새로운 데이터 랜더링이 없을 경우 종료
    if new_height==last_height :
        break
    #높이 변경
    last_height=new_height


# bs4 초기화
soup=BeautifulSoup(browser.page_source, "html.parser")
#통계시리즈 선택자
top_level=soup.select('div#menu-container yt-formatted-string#text')
#댓글 리스트 선택자
comment = soup.select('ytd-comment-renderer#comment')
#중간 확인
#print(soup.prettify())

print()
print()

# 전체 추천 카운트
print('Total Like Count : {}'.format(top_level[0].text.strip()))
print('Total DisLike Count : {}'.format(top_level[1].text.strip()))

#엑셀
ins_cnt = 2


#Dom 반복
for dom in comment:
    print()
    # 이미지 URL 정보
    img_src = dom.select_one("#img").get('src')
    # 작성자
    author = dom.select_one('#author-text > span').text.strip()
    # 댓글 본문
    content = dom.select_one('#content-text').text.strip()
    # 좋아요
    posi_cnt = dom.select_one('#vote-count-middle').text.strip()

    # 이미지 URL 정보
    print('Thumbnail Image URLS : {}'.format(img_src if img_src else 'None'))
    # 작성자
    print('Author : {}'.format(author))
    # 댓글 본문
    print('Content Text : {}'.format(content))
    # 좋아요
    print('Vote Positive Count : {}'.format(posi_cnt))
    print()

    # 엑셀 저장(텍스트)
    worksheet.write('A%s' % ins_cnt, author)
    worksheet.write('B%s' % ins_cnt, content)
    worksheet.write('C%s' % ins_cnt, posi_cnt)

    # 엑셀 저장(이미지)
    if img_src:
        # 이미지 요청 후 바이트 변환
        img_data = BytesIO(req.urlopen(img_src).read())
        # 이미지 데이터 확인
        print(img_data)
        worksheet.insert_image('D%s' % ins_cnt, author, {'image_data': img_data})
    else:
        worksheet.write('D%s' % ins_cnt, 'None')

    # 다음 행 증가
    ins_cnt += 1

    print()

# 브라우저 종료
browser.quit()

# 엑셀 파일 닫기
workbook.close()
