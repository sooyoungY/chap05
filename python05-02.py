#-*-coding:utf-8

# 모듈
# 클래스, 함수, 변수 등을 미리 만들어두고 필요할 때 가져다 사용할 수 있도록 모아놓은 파일
# 실행하는 파일과 모듈이 같은 폴더에 존재해야함

# 유지보수가 편함
# 다른 사람과의 협업이 가능함
# 모듈 사용 시 사용법만 알고 있으면, 해당 모듈의 내부 구조를 몰라도 사용이 가능함

# 사용방법
# import 모듈명
# 모듈 사용 시 해당 모듈명과 클래스, 함수, 변수 등을 모듈명.멤버 로 사용해야 함
# mod.sum()

# from 모듈명 import 모듈 함수
# 모듈 사용 시 해당 모듈의 클래스, 함수, 변수 등을 모듈명 없이 사용할 수 있음
# sum() 

import mod1

print("mod1 모듈의 sum 함수 사용 : {0}".format(mod1.sum(3, 4)))

print()

print("mod1의 safe_sum 함수 사용 : {0}".format(mod1.safe_sum(3, 4)))
print("mod1의 safe_sum 함수 사용 : {0}".format(mod1.safe_sum(1, "a")))

# form 절을 사용하여 mod1의 sum, safe_sum을 모두 불러와 사용하기 때문에 mod1을 붙여서 사용하면 오히려 오류가 발생함
# from mod1 import sum, safe_sum

# print("mod1 모듈의 sum 함수 사용 : {0}".format(sum(3, 4)))

print()
# 문제 1) 사칙 연산을 위한 계산기 프로그램을 모듈을 활용한 방식으로 제작하세요
# 모듈명 : Cal
# 사칙 연산 함수명 plus, minus, multi, divide
# 각각 함수는 매개 변수를 2개씩 가지고 있음(first, second)

import Cal

first = 10
second = 20
print("{0}, {1} 두 수의 덧셈 : {2}".format(first, second, Cal.plus(first, second)))
print("{0}, {1} 두 수의 뺄셈 : {2}".format(first, second, Cal.minus(first, second)))
print("{0}, {1} 두 수의 곱셈 : {2}".format(first, second, Cal.multi(first, second)))
print("{0}, {1} 두 수의 나눗셈 : {2}".format(first, second, Cal.divide(first, second)))


# 클래스나 변수 등을 포함한 모듈
# 일반 함수가 들어있는 모듈과 동일함

# 사용방법
    # 클래스
    # 변수명 = 모듈명.클래스명()

    # 변수
    # 변수명 = 모듈명.변수명

print()
import mod2

result = mod2.sum(3, 4)
print("mod2 모듈을 로드하여 sum 함수 사용 : {0}".format(result))

# 문제 2) 문제 1의 소스를 수정하여 클래스를 사용한 방식의 사칙연산 프로그램은 제작하세요
# 모듈명 : Cal2
# 클래스명 : Calculator
# 함수명 : plus, minus, multi, divide
# 각 함수는 2개의 매개변수를 가짐(first, second)

import Cal2

a = Cal2.Calculator()
print(a.plus(1, 1))
print(a.minus(1, 1))
print(a.multi(1, 1))
print(a.divide(1, 1))

# 문제 3) 위의 문제 2번에서 오버로딩을 사용하여 값이 매개 변수에 따라 다른 형태로 출력하는 클래스를 만들고 이를 사용하는 프로그램을 제작하세요
# 모듈명 : Cal3
# 기본 초기화 메서드 : setNumber
    # 매개변수가 총 3개
    # 멤버 변수 first, second 의 값을 초기화 함
# 메서드 이름 : plus, minus, multi, divide
    # 기존 그대로 만들고
    # 멤버 변수를 활용하여 값을 연산
# 메서드의 매개변수의 수에 따라 연산을 달리함 (*args)
    # 추가된 메서드 totalCal
    # 1번째 매개변수 : self
    # 2번째 매개변수 args의 index 0번 : +, -, *, / (문자열로 받기)
    # 매개변수 args의 index 1번부터 숫자를 입력받음
    # 입력받을 매개변수 수 총 5개까지

    # def totalCal(self, *args):
    #     if args[0] == "+":
    #         args[1] + args[2] + args[3]

    #     elif args[0] == "-":

import Cal3

test = Cal3.Calculator()
test.setNumber(10, 20)

print("=" * 30)

print(test.plus())
print(test.minus())
print(test.multi())
print(test.divide())

print("=" * 30)

print(test.totalCal("+"))
print(test.totalCal("-"))
print(test.totalCal("*"))
print(test.totalCal("/"))

print(test.totalCal("+", 10, 20))
print(test.totalCal("-", 10, 20))
print(test.totalCal("*", 10, 20))
print(test.totalCal("/", 10, 20))

print("=" * 30)

print(test.totalCal("+", 10, 20, 30))
print(test.totalCal("-", 10, 20, 30))
print(test.totalCal("*", 10, 20, 30))
print(test.totalCal("/", 10, 20, 30))