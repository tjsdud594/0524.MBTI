import time
import os
import platform
import matplotlib.pyplot as plt   # 파이썬은 시각화를 한 뒤에 이미지를 얹어야 이미지가 뜬다.
from PIL import Image  # 


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
clear()
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
script_dir = os.path.dirname(os.path.abspath(__file__))


if a > b:
    print("q결과")
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
elif b > a:
    print("w결과")
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
else:
    print("ㄷ결과")
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()
    image = Image.open(os.path.join(script_dir, '''이미지'''))
    plt.imshow(image)
    plt.show()

# 
# while문 사용해서 처음으로 돌아가는 코드짜기