import random
# 문자 그룹 정의
class gp1:
        Gp1 = ["A","E","O","Y"]
        Gp2 = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Z"]
class gp2:
        GP1 = []

# 문자를 섞는 함수
def shurf():
    Gp1 = ["A","E","O","Y"]
    random.shuffle(Gp1)
    return Gp1

# 문자 입력 함수
def input_char():
    char = input("문자를 입력하세요: ").upper()
    return char

#메인 루프 - 섞을지 멈출지 확인
while True:
    char = input_char()

    if char == "STOP":
        print("Program stopped.")
        break
    elif char == "SHUFFLE":
        print(shurf())

# 문자가 어느 그룹에 속하는지 출력
    elif char in gp1.Gp1:
        print("Group 1")
    else:
        print("Group 2")  
#랜덤 값을 가져와서 그 랜덤값을 더함 => 암호화