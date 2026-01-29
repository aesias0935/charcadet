import random
# 문자 그룹 정의 gp1 = 기존 gp2 = 변경 
class gp1:
        Gp1 = ["A", "E", "O", "Y"]
        Gp2 = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
class gp2:
        GP1 = [6, 7, 8, 9]
        GP2 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]

dict_gp1 = dict(zip(gp1.Gp1, gp2.GP1))
dict_gp2 = dict(zip(gp1.Gp2, gp2.GP2))

# 문자를 섞는 함수
#def shurf():
#    Gp1 = ["A","E","O","Y"]
#    random.shuffle(Gp1)
#    return Gp1

def shurf():
    global dict_gp1  # ← 새로 추가! 전역 변수를 수정하겠다는 뜻
    Gp1 = ["A", "E", "O", "Y"]
    random.shuffle(Gp1)
    
    # ← 새로 추가! 섞인 순서로 딕셔너리를 다시 만듦
    dict_gp1 = dict(zip(Gp1, gp2.GP1))
    
    print("섞인 순서:", Gp1)
    print("새로운 매핑:", dict_gp1)
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
    elif char in dict_gp1:
        print(dict_gp1[char])
    elif char in dict_gp2:
        print(dict_gp2[char]) 
    else:
        print("해당 문자는 그룹에 속하지 않습니다.")


#랜덤 값을 가져와서 그 랜덤값을 더함 => 암호화