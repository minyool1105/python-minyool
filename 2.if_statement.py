#2026/10/31 공학아카데미 파이선 수업
if False:
    print("True")
    print("True라면 내부는 모두 수행한다.")

else:
    print("False")
    print("위 조건들이 True가 아닐 때 실행된다.")
print("Always")

print("=====================")
score = 70

if score > 80:
    print("A학점입니다.")
elif score > 60:
    print("B학점입니다.")
elif score > 40:
    print("C학점입니다.")
elif score > 20:
    print("D학점입니다.")
elif score > 0:
    print("낙제입니다.")
print("=====================")
var1 = 1
var2 = 2

if var1 > var2:
    print("var1이 더 큼")

if var1 < var2:
    print("var2가 더 큼")

if var1 == var2:
    print("var1과 vaar2가 같습니다.")


print("--------------------------------------------------------------")

user_input = input("원하는 동작을 입력하시오\n입력 : ")

if user_input == "1":
    print("게임을 시작합니다")

