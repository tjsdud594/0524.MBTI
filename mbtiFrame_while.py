import time
import os
import platform
import matplotlib.pyplot as plt 
from PIL import Image  

while True:

    def clear():   # mac(clear) or window(명령어 : cls)인지 구분하기 위해서 넣음 :  화면지우기
        os_type = platform.system()
        if os_type == 'Windows':
            os.system('cls')    # os : 파이썬에 기본적으로 내장된 모듈
        else:
            os.system('clear')  # os.system('명령어') : 시스템 자체의 프로그램이나 기타명령어를 파이썬에서 호출


    clear()  # 위의 컴퓨터 운영체제에 따른 cls/clear 입력
    print("무료 성격 유형 검사 입니다.")

    a = 0
    b = 0
    time.sleep(1)  # time.sleep(초) 일정시간동안 프로세스를 정지('무료 성격 유형 검사 입니다.' 글자가 1초동안 뜸)
    clear()   # 이전화면에 나온 문자들 지움
    print("문항이?")
    print("1.을 입력")
    print("2.을 입력")
    q1 = int(input("번호를 입력해주세요:"))

    if q1 == 1:   # 답변이 1번이면 a에다가 +1
        a += 1
    if q1 == 2:   # 답변이 2번이면 b에다가 +1
        b += 1

        
    clear() 
    print("2번째 문항이?")
    print("1.을 입력")
    print("2.을 입력")
    q2 = int(input("번호를 입력해주세요:"))

    if q2 == 1:
        a += 1
    if q2 == 2:
        b += 1
    clear()
    print("3번째 문항이?")
    print("1.을 입력")
    print("2.을 입력")
    q3 = int(input("번호를 입력해주세요:"))

    if q3 == 1:
        a += 1
    if q3 == 2:
        b += 1

    clear()
    print("4번째 문항이?")
    print("1.을 입력")
    print("2.을 입력")
    q4 = int(input("번호를 입력해주세요:"))


    if q4 == 1:
        a += 1
    if q4 == 2:
        b += 1
    clear()


    print("결과는")
    clear()


    if a > b:
        print("q결과")
       
    elif b > a:
        print("w결과")
        
    else:
        print("ㄷ결과")
       
    clear() 
    print("다시할꺼야?")
    print("1. 1을 입력")
    print("2. 2을 입력")
    q5 = int(input("번호를 입력해주세요:"))
    if q5 != 1:
        clear()
        print('끝')
        break
