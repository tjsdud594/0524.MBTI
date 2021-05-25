'''
필요한 모듈 import
'''
import time
import os
import platform
import matplotlib.pyplot as plt
from PIL import Image
# https://www.delftstack.com/ko/howto/matplotlib/display-an-image-with-matplotlib-python/


while True:

    def clear():   # mac(clear) or window(명령어 : cls)인지 구분하기 위해서 넣음 :  화면지우기
        '''
        각 os에 맞는 clear 명령어입력
        '''
        os_type = platform.system()
        if os_type == 'Windows':
            os.system('cls')    # os : 파이썬에 기본적으로 내장된 모듈
        else:
            os.system('clear')  # os.system('명령어') : 시스템 자체의 프로그램이나 기타명령어를 파이썬에서 호출


    clear()  # 위의 컴퓨터 운영체제에 따른 cls/clear 입력
    print("당신의 호그와트 기숙사는?")

    A = 0
    B = 0
    C = 0
    time.sleep(1)  # time.sleep(초) 일정시간동안 프로세스를 정지('무료 성격 유형 검사 입니다.' 글자가 1초동안 뜸)
    clear()   # 이전화면에 나온 문자들 지움
    print("둘 중에 한 직업을 가질 수 있다면?")
    print("1.고위직 공무원")
    print("2.스타트업 기업 회장")
    q1 = int(input("번호를 입력해주세요:"))

    if q1 == 1:   # 답변이 1번이면 a에다가 +1
        A += 1
    if q1 == 2:   # 답변이 2번이면 b에다가 +1
        B += 1
    if q1 not in (1, 2):
        C += 1


    clear()
    print("휴일의 나는?")
    print("1.자기계발의 시간을 가진다.")
    print("2.바깥에 나가서 친구도 만나고 쇼핑도 하고~")
    q2 = int(input("번호를 입력해주세요:"))

    if q2 == 1:
        A += 1
    if q2 == 2:
        B += 1
    if q2 not in (1, 2):
        C += 1

    clear()
    print("당신과 함께할 반려동물을 선택한다면?")
    print("1.고양이")
    print("2.강아지")
    q3 = int(input("번호를 입력해주세요:"))

    if q3 == 1:
        A += 1
    if q3 == 2:
        B += 1
    if q3 not in (1, 2):
        C += 1

    clear()
    print("하루 중 좋아하는 시간대는?")
    print("1.이슬이 내리는 어두운 새벽녘")
    print("2.햇살이 따뜻한 오후")
    q4 = int(input("번호를 입력해주세요:"))

    if q4 == 1:
        A += 1
    if q4 == 2:
        B += 1
    if q4 not in (1, 2):
        C += 1

    clear()


    print("당신의 기숙사는...")
    time.sleep(1)
    clear()


    if A > B and A > C:
        print("슬리데린")
        image = Image.open('Slytherin.jpg')
        plt.imshow(image)
        plt.show()

    elif B > A and B > C:
        print("그리핀도르")
        image = Image.open('Gryffindor.jpg')
        plt.imshow(image)
        plt.show()

    elif C > A and C > B:
        print('래번클로')
        image = Image.open('Ravenclaw.jpg')
        plt.imshow(image)
        plt.show()

    else:
        print("후플푸프")
        image = Image.open('Hufflepuff.jpg')
        plt.imshow(image)
        plt.show()

    print("배정완료!")

    print("넘어가려면 아무 숫자나 입력해주세요.")
    q5 = int(input("번호를 입력해주세요:"))
    clear()


    print("다시하시겠습니까?")
    print("다시하려면 1을 입력")
    print("끝내려면 1말고 아무 숫자나 입력")
    q6 = int(input("번호를 입력해주세요:"))

    if q6 != 1:
        clear()
        print('끝')
        break
