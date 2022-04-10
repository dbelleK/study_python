import pandas as pd # pip install pandas - 명령프롬포트

user_list=pd.read_excel('sample.xlsx', sheet_name='Sheet1', engine='openpyxl')
print(user_list)

'''
pip install xlrd
pip install openpyxl
pip install pandas
'''
