#함수
def para_func(v1, v2,v3=0) : # v3=0인라인매개변수
    result = 0
    result = v1 + v2 + v3
    return result

#===================================
sum=0

#메인
hap= para_func(10,20)
print("매개변수 2개 ==> %d" % hap)  # v3=0인라인매개변수 값을 명시하지 않으면 0으로 들어감

hap= para_func(10,20,30)
print("매개변수 3개 ==> %d" % hap)

print("============================================")

#함수
def para1_func(*para) :
    result = 0
    for num in para:
        result=result+num
    return result

#===================================
sum=0

#메인
hap= para1_func(10,20)
print("매개변수 2개 ==> %d" % hap)

hap= para1_func(10,20,30)
print("매개변수 3개 ==> %d" % hap)

hap= para1_func(10,20,30,40)
print("매개변수 4개 ==> %d" % hap)
