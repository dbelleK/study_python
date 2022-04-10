aa=[]
bb=[]
value=0

for i in range(0,100):
    aa.append(value)
    value += 2
print("aa[0]는 %d, aa[99]는 %d 입력됨" %(aa[0], aa[99]))

print("")
for i in range(0,100):
    bb.append(aa[99-i]) #99,98,97...

print("bb[0]는 %d, bb[99]는 %d 입력됨" %(bb[0], bb[99]))
