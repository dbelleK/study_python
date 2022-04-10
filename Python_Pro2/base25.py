a=[23,12,36,63,19]

#인덱스 값 출력
for i in enumerate(a):
    print(i)
for x in enumerate(a): # enumerate:첨자,값
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index,value)

    #-----------------------
if all (60>x for x in a): #모두가 참이면 yes
    print("yes")
else:
    print("no")

print()
if any (60>x for x in a): #하나라도 참이면 yes
    print("yes")
else:
    print("no")
