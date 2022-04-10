'''
i, dan=0,0

dan=int(input("몇 단 : "))

for i in range(1,10):
    print("%d X %d = %2d" % (dan, i, dan*i))
'''

i, k=0,0

for i in range(2,10):
    for k in range(1,10):
        print("%d X %d = %2d" % (i, k, i*k))
    print("")
