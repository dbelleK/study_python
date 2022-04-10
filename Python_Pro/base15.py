'''
i, sum, hap = 0,0,0

for i in range(1, 101, 1) :
    sum+=i;
print("1에서 100까지의 합 : %d" % sum)

#500에서 1000까지의 홀수의 합
for i in range(501,1001,2):
    hap+=i
print("500에서 1000까지의 합 : %d" % hap)
'''

i, hap2, num = 0,0,0

num=int(input("값 입력 : "))

for i in range(1,num+1):
    hap2+=i
print("1에서 %d까지의 합 : %d" % (num, hap2))
