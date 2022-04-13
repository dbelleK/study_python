import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randint(500,1000, size=(100,4)), columns=[2015,2016,2017,2018])
print(df)
df=pd.DataFrame(np.random.randn(100,4), columns=[2015,2016,2017,2018]) #음수포함
print(df)

#엑셀쓰기
df.to_excel('C:/Users/kkddy/Documents/dbelleK_git/study_python/Pyrhon_webdriver/data/result3.xlsx')
df.to_excel('C:/Users/kkddy/Documents/dbelleK_git/study_python/Pyrhon_webdriver/data/result4.xlsx', index=False, header=True)
## index=False, header=True : 글 번호 열 삭제
print('commit')
