## **0524 mini project**
### - Who? 
>#### 강정현, 이성규, 정주영A, 류선영
### - What?
#### **1. MBTI 뼈대 코드를 이용해 자신만의 MBTI를 만듦**

<br>

    '''
    import time
    import os
    import platform

    def clear():   

        os_type = platform.system()
        if os_type == 'Windows':
            os.system('cls')   
        else:
            os.system('clear')

    clear()  # 위의 컴퓨터 운영체제에 따른 cls/clear 입력
    print("당신의 호그와트 기숙사는?")

    A = 0
    B = 0
    C = 0
    time.sleep(1) 
    clear()  
    print("둘 중에 한 직업을 가질 수 있다면?")
    print("1.고위직 공무원")
    print("2.스타트업 기업 회장")
    q1 = int(input("번호를 입력해주세요:"))

    if q1 == 1:  
        A += 1
    if q1 == 2:  
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
    '''

<br>
            
#### **2. While을 이용하여 MBTI 검사 후 다시 처음부터 검사 할 수 있도록 기능추가!**
> 처음에 While문을 마지막에 if문을 넣어서 기능구현 

<br>

        '''
        while True:

        (MBTI CODE)

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
                '''
<br>
            
#### **3. Hogwarts MBTI 생성 후 결과창에 image가 뜨도록 추가**

> 그리핀도르

![Gryffindor](https://user-images.githubusercontent.com/84279479/120772515-5b562480-c55b-11eb-9590-ec29e31be89b.jpg)

> 슬리데린

![Slytherin](https://user-images.githubusercontent.com/84279479/120772585-6c9f3100-c55b-11eb-93e1-28e6a1ff1184.jpg)

> 래번클로

![Ravenclaw](https://user-images.githubusercontent.com/84279479/120772664-7f196a80-c55b-11eb-95a3-3b73a0c5947b.jpg)

> 후플푸프

![Hufflepuff](https://user-images.githubusercontent.com/84279479/120772715-8e001d00-c55b-11eb-9830-878f5d167e9b.jpg)

<br>

#### **4. pylint 검사 후 코드를 예쁘게 수정!**
> 첫 pylint 검사

![pylint_F](https://user-images.githubusercontent.com/84279479/120772791-a4a67400-c55b-11eb-8d89-a438836f0d03.png)


> code 수정 후

![pylint_E](https://user-images.githubusercontent.com/84279479/120772850-b2f49000-c55b-11eb-9952-0ded57dce140.png)



