# 1~100의 합에서 최초로 1000이 넘는 위치 index
j=0
sum2=0;
for j in range(1,101):
    sum2+=j
    if sum2>1000:
        break
print(sum2)
print("100이 넘는 %d입니다" % j)

print("===========================")

i=0
sum=0
for i in range(1,101):
    if i%3==0:
        continue
    sum+=i
print("3의 배수를 제외한 합: %d" % sum)
