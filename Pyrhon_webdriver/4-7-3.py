import datetime
import FinanceDataReader as fdr
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#조회 시작
start=datetime.datetime(2021,4,12)
#조회 마감 날짜
end=datetime.datetime(2022,4,10)

# 구글 : google finance => https://www.google.com/finance/?hl=ko
# 한국거래소 상장종목 전체
df_krx=fdr.StockListing('KRX') #카카오
# 리스트 10개 출력
#print(df_krx.head(10))

#print(df_krx.index)
#print(df_krx['HomePage'])
#print(df_krx.iloc[0])
#print(df_krx.describe())

# 미국거래소 상장종목중 아마존 금융정보
df_amz=fdr.DataReader('AMZN', start, end)
#print(df_amz.iloc[0])
#print(df_amz.loc['2021-04-12'])
#print(df_amz.head(10))
#print(df_amz.describe())


# 미국거래소 상장종목중 아마존 금융정보
df_amz=fdr.DataReader('GOOG', start, end)
#print(df_amz.iloc[0])
print(df_amz.loc['2021-04-12'])
#print(df_amz.head(10))
print(df_amz.describe())
