#3. while문은 반복문 중 하나
# while문은 조건이 True일 동안 계속 반복함
#조건에 변수를 사용해서 변수의 겂이 변경되는 등 더 이상 True가 아닌 False가 될 때 종료됨

a = 0

while a < 10:
    print(a)
    a += 1


print("=====================")
print("1. 게임 시작")
print("2. 랭킹 확인")
print("0. 게임종료")
print("=====================")
user_input = None

while user_input != "0":
    user_input = input("원하는 동작을 입력하세요\n원하는 동작 입력하기 : ")

    if user_input == "1":
        print("게임을 시작합니다.")
    elif user_input == "2":
       print("랭킹을 확인합니다")
    elif user_input == "0":
       print("게임을 종료합니다.")
    else:
        print("잘못된 입력입니다.")


while True:
    user_input = input("원하는 동작을 입력하세요")
    if user_input == "0":
        print("게임을 종료합니다.")
        break #해당 if문을 포함하는 직속 while문을 종료함

b = 0

while b < 10:
    b = b+1
    if b ==5:
        continue #1부터 9까지 출력하다가 중간에 5는 건너뛸 때 continue를 쓴다.
    print(b)