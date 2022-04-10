# 읽기 : read = open("in.txt", "r")
# 쓰기 : write = open("in.txt", "w")
# 읽기 : r
# 쓰기 : w
# 읽기/쓰기 : r+
# 이어쓰기 : a
# 텍스트 : t
# 바이너리 : b

import os

path="c:/temp/"
dirContents = os.listdir(path)

def save_file() :
    for i in dirContents :
        if os.path.isfile(path + i): #파일있냐?
            print("파일을 찾았습니다")
            tmp=input("복사하시겠습니까(y/n)?")

            if tmp == "y":
                input_file=open(path + i, "r", encoding="utf-8")
                buffer = input_file.read()

                output_file = open(path + input("저장할 파일 이름을 입력하세요 : ")+".txt", "w", encoding="utf-8")

                enc=input("암호화 하시겠습니까(y/n)? ")

                if enc == "y" :
                    output_file.write(encrypt(buffer))
                else :
                    output_file.write(buffer)

                output_file.close()
                input_file.close()

            else :
                print("종료합니다")

# 암호화
def encrypt(string) :
    crypt = chr(0x110000 - 1) #0011 #암호문서 판독

    for i in string:
        crypt += chr(ord(i) * 17)

    return crypt

## =============================================================================

#암호가 되어있으면 true
# 암호코드 검증
def isEncrypt(string):
    result=False
    if ord(string[0]) == 0x110000 - 1 :
        result=True
    return result

# 암호 해독
def decrypt(string):
    decrypt = ""

    for i in string:
        decrypt += chr(int(ord(i) / 17))

    return decrypt

# 파일불러오기
def decrypt_file():
    for i in dirContents :
        if os.path.isfile(path + i) :
            file = open(path + i, "r", encoding="utf-8")
            buffer = file.read()

        #암호화된 파일이냐?
        if isEncrypt(buffer) : #true
            Output = open(path + i + "_decrypt" + ".txt", "w", encoding="utf-8")
            Output.write(decrypt(buffer)) #암호해독
            Output.close()
        else :
            print("암호화 되어 있지 않습니다.")

        file.close()

#메인
#save_file() #암호화
decrypt_file() #해독 #암호화되어 있는 파일만 있을 떄 암호화 메서드 주석처리 해놓고 실행하면 해독된다
