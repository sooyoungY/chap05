# -*-coding:utf-8
# 문제 1 ) 구구단 클래스
class Gugudan:

    def multi(self, num1, num2):
        return num1 * num2

gugudan = Gugudan()

num1 = input("입력 받을 단 수 : ")
num1 = int(num1)
num2 = 1

while num1 < 10:
    while num2 < 10:
        print("{0} X {1} = {2}".format(num1, num2, gugudan.multi(num1, num2)))
        num2 += 1
    num1 += 1