#변수
money, c1000, c500, c100, c50, c10 = 0,0,0,0,0,0

#메인
money = int(input("교환할 돈을 입력하세요: ")) #7860

c1000 = money//1000 #나눈 몫 #7
money %= 1000 #나머지 #860

c500 = money//500
money %= 500

c100 = money//100
money %= 100

c10 = money//10
money %= 10

print("\n  천원짜리 ==> %d 개 " % c1000)
print(" 오백원짜리 ==> %d 개 " % c500)
print(" 백원짜리   ==> %d 개 "% c100)
print(" 오십원짜리 ==> %d 개 "% c50)
print(" 십원짜리   ==> %d 개 "% c10)
print(" 바꾸지 못한 잔돈 ==> %d 원 \n"% money)
