#변수
foods = {"떡볶이": "김말이",
"짜장면" : "단무지",
"라면" : "김치",
"피자" : "콜라",
"맥주" : "감자튀김",
"치킨" : "치킨무",
"삼겹살" : "소주"}

#메인
while(True):
    #str:String / char:chracter / ord:ASCII코드
    myfood=input(str(list(foods.keys())) +"중 오늘의 메뉴는 : ")
    if myfood in foods :
        print("<%s>에 맞는 궁합 음식은 <%s> 입니다." %(myfood, foods.get(myfood)))
    elif myfood == '끝':
        break
    else :
        print("메뉴에 없는 음식입니다. 다시 주문하세요~")
