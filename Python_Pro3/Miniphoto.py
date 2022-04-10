from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from wand.image import *

# 함수 정의 부분
def displayImage(img, width, height) :
    global window,canvas,paper,photo,photo2,oriX,oriY

    window.geometry(str(width)+"x"+str(height))
    if canvas != None :
        canvas.destroy()
    canvas=Canvas(window, width=width, height=height)
    paper=PhotoImage(width=width, height=height)
    canvas.create_image((width/2, height/2), image=paper, state="normal")

    blob=img.make_blob(format='RGB')
    for i in range(0,height):
        for k in range(0,width):
            r=blob[(i*3*width)+(k*3) + 0]
            g=blob[(i*3*width)+(k*3) + 1]
            b=blob[(i*3*width)+(k*3) + 2]
            paper.put("#%02x%02x%02x" % (r,g,b) , (k, i))
    canvas.pack()

def func_open() :
    global window,canvas,paper,photo,photo2,oriX,oriY

    readFp=askopenfilename(parent=window, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"),  ("모든 파일", "*.*") ))
    photo=Image(filename=readFp)
    oriX=photo.width
    oriY=photo.height

    photo2=photo.clone()
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)


def func_save() :
    global window,canvas, paper, photo, photo2, oriX, oriY

    if photo2 == None:
        return
    saveFp=asksaveasfile(parent=window, mode="w",
                         defaultextension=".jpg",
                         filetypes=(("JPG 파일","*.jpg;*.jpeg"),
                         ("모든 파일" ,"*.*")))
    savPhoto=photo2.convert("jpg")
    savPhoto.save(filename=saveFp.nae)

def func_exit() :
    window.quit()
    window.destroy()

def func_zoomin() :
    global window,canvas,paper,photo,photo2,oriX,oriY

    scale=askinteger("확대배수", "확대할 배수를 입력하세요", minvalue=2, maxvalue=4)

    photo2=photo.clone()
    photo2.resize(int(oriX*scale),int(oriY*scale))
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

def func_zoomout() :
    global window,canvas,paper,photo,photo2,oriX,oriY

    scale=askinteger("축소배수", "축소할 배수를 입력하세요", minvalue=2, maxvalue=4)

    photo2=photo.clone()
    photo2.resize(int(oriX/scale),int(oriY/scale))
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

def func_size():
    sizeX=askinteger("이미지 가로사이즈", "Size_X")
    sizeY=askinteger("이미지 세로사이즈", "Size_Y")

    photo2=photo.clone() #항상 원본사이즈에서 시작 / clone을 사용하지 않으면 이어서 시작
    photo2.resize(sizeX,sizeY)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

#상하반전
def func_mirror1() :
    global window,canvas,paper,photo,photo2,oriX,oriY

    photo2.flip()
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

#좌우반전(원본에서의)
def func_mirror2() :
    global window,canvas,paper,photo,photo2,oriX,oriY,i

    #원본 훼손 없이 사용(원본을 복사해서 사용): 원본의 무결성 유지
    if i==0:
        photo2=ptoto.clone()
        i==1

    photo2.flop()
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)


def func_rotate() :
    global window,canvas,paper,photo,photo2,oriX,oriY,i
    degree=askinteger("회전", "회전할 각도를 입력하세요", minvalue=0, maxvalue=360)

    if i==0:
        photo2=ptoto.clone()
        i==1

    photo2.rotate(degree)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)


def func_bright() :
    global window,canvas,paper,photo,photo2,oriX,oriY
    value=askinteger("밝기", "값을 입력하세요(100~200)", minvalue=100, maxvalue=200)

    #photo2=photo.clone()
    photo2.modulate(value,100,100)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

def func_dark() :
    global window,canvas,paper,photo,photo2,oriX,oriY
    value=askinteger("어둡게", "값을 입력하세요(0~100)", minvalue=0, maxvalue=100)

    #photo2=photo.clone()
    photo2.modulate(value,100,100)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

#선명하게
def func_clear() :
    global window, canvas, paper, photo, photo2, oriX, oriY

    value = askinteger("선명하게","값을 입력하세요(100~200)",minvalue=100,maxvalue=200)

    #photo2=photo.clone()
    photo2.modulate(100,value, 100) #밝기, 체도, 명도
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

def func_unclear() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("탁하게","값을 입력하세요(0~100)",minvalue=0,maxvalue=100)
    #photo2=photo.clone()
    photo2.modulate(100,value, 100) #밝기, 체도, 명도
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

#흑백이미지
def func_bw() :
        global window,canvas,paper,photo,photo2,oriX,oriY
        photo2 = photo.clone()
        photo2.type = "grayscale"
        newX=photo2.width
        newY=photo2.height
        displayImage(photo2,newX,newY)

# 변수 선언 부분
window,canvas, paper=None, None, None
photo, photo2=None, None
oriX,oriY,i= 0,0,0

# 메인 코드 부분
window = Tk()
window.geometry("250x250")
window.title("미니 포토샵(Ver 0.1)")

photo = PhotoImage()

mainMenu = Menu(window)
window.config(menu = mainMenu)
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "열기", command = func_open)
fileMenu.add_command(label = "저장", command = func_save)
fileMenu.add_separator()
fileMenu.add_command(label = "종료", command = func_exit)

imageMenu1 = Menu(mainMenu)
mainMenu.add_cascade(label = "이미지 처리(1)", menu = imageMenu1)
imageMenu1.add_command(label="확대", command = func_zoomin)
imageMenu1.add_command(label="축소", command = func_zoomout)
imageMenu1.add_command(label="사이즈", command = func_size)##########33
imageMenu1.add_separator()
imageMenu1.add_command(label="상하 반전", command = func_mirror1)
imageMenu1.add_command(label="좌우 반전", command = func_mirror2)
imageMenu1.add_command(label="회전", command = func_rotate)

imageMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label = "이미지 처리(2)", menu = imageMenu2)
imageMenu2.add_command(label="밝게", command=func_bright)
imageMenu2.add_command(label="어둡게", command=func_dark)
imageMenu2.add_separator()
imageMenu2.add_command(label="선명하게", command=func_clear)
imageMenu2.add_command(label="탁하게", command=func_unclear)
imageMenu2.add_separator()
imageMenu2.add_command(label="흑백이미지", command=func_bw)

window.mainloop()


'''
http://www.imagemagick.org/download/binaries/
ImageMagick-7.1.0-29-Q8-x64-dll.exe 다운
exe파일 실행 후 설치
'''
