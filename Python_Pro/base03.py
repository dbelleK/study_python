## GUI
from tkinter import *

## 변수
window = None
canvas = None ## 실제 사용하는 공간
x1,y1,x2,y2 = None,None,None,None

## 함수 #함수는 def라 선언
def mouseClick(event): #마우스를 클릭하면 event가 들어오겠다
    global x1,y1,x2,y2
    x1=event.x
    y1=event.y

def mouseDrop(event): #마우스를 떼면 event가 들어오겠다 //손을 떼는 좌표가 x2,y2
    global x1,y1,x2,y2
    x2=event.x
    y2=event.y
    canvas.create_line(x1,y1,x2,y2, width=5, fill="red")

## 메인
window = Tk() #윈도우 창 생성
window.title("그림판")
canvas = Canvas(window, height=300, width=300) #윈도우 창 안에 캔버스(Canvas:작업 영역) 생성
canvas.bind("<Button-1>", mouseClick) #왼족버튼을 누르면(bind)
canvas.bind("<ButtonRelease-1>", mouseDrop) #마우스 떼면

canvas.pack() #출력

window.mainloop()
