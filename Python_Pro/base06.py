sel = int(input("입력진수 결정(16/10/8/2) : ")) #16진수
num = input('값 입력 : ') #CA72

if sel==16 : #16진수와 같으면
    num10=int(num,16) #10진수로 바꾸기
if sel==10 :
    num10=int(num,10)
if sel==8 :
    num10=int(num,8)
if sel==2 :
    num10=int(num,2)

print("16진수 ==> ", hex(num10)) #hex() : 16진수를 10진수로 변환하는 메소드
print("10진수 ==> ", num10)
print("8진수 ==> ", oct(num10)) #oct() : 8진수를 10진수로 변환하는 메소드
print("2진수 ==> ", bin(num10)) #bin() : 2진수를 10진수로 변환하는 메소드
