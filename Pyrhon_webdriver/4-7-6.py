import FinanceDataReader as fdr
import datetime
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#plotkib Converter : 날짜(시간) 관련 Warning 제거
register_matplotlib_converters()

#조회 시작
start=datetime.datetime(2021,4,12)
#조회 마감 날짜
end=datetime.datetime(2022,4,10)

# 네이버 주식 정보
gs_naver=fdr.DataReader('035420', start, end)

# 다음 카카오 주식 정보
gs_daum=fdr.DataReader('035720', start, end)

#출력
print(gs_naver)
print(gs_daum)

print('-------------------차트 -------------------')

#치트 윈도우 제목
fig=plt.figure('Charts Test')
#forward=True : 차트 크기 변경을 위해서 True로 열어줌 (가로 10, 세로 6)으로 크기변경
fig.set_size_inches(10,6, forward=True)

#차트 설정1
plt.plot(gs_naver.index, gs_naver['Close'], 'b', label="Naver")
#차트 설정2
plt.plot(gs_daum.index, gs_daum['Close'], 'r', label="Kakao")

#범례
plt.legend(loc='upper left')
#차트 제목
plt.title('Naver & Daum')

#x축 레이블
plt.xlabel('Date')

#y축 레이블
plt.ylabel('Close')

plt.show()  
