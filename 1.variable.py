#a = 123
#print(a)

#a = "a"
#print(a)

#a = 123 + 123
#print(a)

#a = [123, "ks", 3, 3*9]
#print(a)
# 변수 이름에 숫자와 특수 기호(-,_ 제외), 띄어쓰기 사용 불가

#var1 = 10
#var2 = 20

#a = var1 + var2
#print(a)

#input_var = input("숫자를 입력하시오")
#print(input_var)

#print(input("숫자를 입력하시오"))
#

#Dictionary


question1 = {"no" : 1, "question" : "답을 구하시오","answer" : 1, "score" : 5, "isMultipleChoice" : False}
questions = [{"no" : 2, "question" : "답으로 올바른 것을 구하시오","answer" : 3, "score" : 5, "isMultipleChoice" : True, "sample" : [1, 2, 3, 4, 5]},
             {"no" : 3, "question" : "답을 구하시오","answer" : 154, "score" : 5, "isMultipleChoice" : False},
             {"no" : 4, "question" : "답을 구하시오","answer" : 523, "score" : 5, "isMultipleChoice" : False},
             {"no" : 5, "question" : "답을 구하시오","answer" : 1983, "score" : 5, "isMultipleChoice" : False},
             {"no" : 6, "question" : "답을 구하시오","answer" : 2004, "score" : 5, "isMultipleChoice" : False}]
print(question1["answer"]) #question1의 answer Key의 Value 출력하기

print(questions[1]["question"]) #index 번호로 찾기
