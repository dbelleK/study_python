a=100
result=0
i=0

for i in range(1,5): #1에서부터 5번
    result=a<<i #숫자 증가
    print("%d << %d = %d" % (a,i,result))
print()

for i in range(1,5): #1에서부터 5번
    result=a>>i #숫자 감소
    print("%d >> %d = %d" % (a,i,result))
print()
