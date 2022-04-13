import pandas as pd
import sys
import io
import xlrd
import openpyxl

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#기본읽기
df1=pd.read_excel('C:/Users/kkddy/Documents/dbelleK_git/study_python/Pyrhon_webdriver/data/excel_s1.xlsx',header=0, engine='openpyxl')
print(df1)

#값수정(space처리)
df1['state']=df1['state'].str.replace(' ','|')
print(df1)

#평균
df1['Avg']=df1[['2018','2019','2020']].mean(axis=1).round(2) #axis=1 : 1이면 행단위
print(df1)

#합계
df1['Sum']=df1[['2018','2019','2020']].sum(axis=1)
print(df1)

#최소값
df1=df1[['2018','2019','2020']].min(axis=0)
print(df1)

#상세 분석 정보
print('상세 분석 정보')
print(df1,describe())

#엑셀 쓰기
df1.to_excel('C:/Users/kkddy/Documents/dbelleK_git/study_python/Pyrhon_webdriver/data/reault_s1.xlsx')


'''
#컬럼 연산
df2=pd.read_excel('C:/Users/kkddy/Documents/dbelleK_git/study_python/Pyrhon_webdriver/data/excel_s2.xlsx', header=0, engine='openpyxl')
df2[['Units','UnitCost']]=df2[['Units','UnitCost']].astype(int) #int형변환
df2['Custom1'] = df2['Units']*df2['UnitCost']
df2['Custom2'] = df2['Total']*10
print(df2)

#엑셀 쓰기
df2.to_excel('C:/Users/kkddy/Documents/dbelleK_git/study_python/Pyrhon_webdriver/data/excel_s2.xlsx')
print('commit')
'''
