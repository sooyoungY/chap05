#-*-coding:utf-8

class Calculator:
    def setNumber(self, first, second):
        self.first = first # 멤버 변수
        self.second = second

    def plus(self):
        return self.first + self.second

    def minus(self):
        return self.first - self.second

    def multi(self):
        return self.first * self.second

    def divide(self):
        return self.first / self.second

    def totalCal(self, *args):
        length = len(args)

        if length == 1:
            if args[0] == "+":
                return self.plus()
            elif args[0] == "-":
                return self.minus()
            elif args[0] == "*":
                return self.multi()
            elif args[0] == "/":
                return self.divide()
        elif length == 3:
            if args[0] == "+":
                return args[1] + args[2]
            elif args[0] == "-":
                return args[1] - args[2]
            elif args[0] == "*":
                return args[1] * args[2]
            elif args[0] == "/":
                return args[1] / args[2]
        elif length == 4:
            if args[0] == "+":
                return args[1] + args[2] + args[3]
            elif args[0] == "-":
                return args[1] - args[2] - args[3]
            elif args[0] == "*":
                return args[1] * args[2] * args[3]
            elif args[0] == "/":
                return args[1] / args[2] / args[3]
        else:
            print("잘못된 입력입니다.")
            print("1개의 연산자와 3개까지의 숫자 입력을 지원합니다.")

    def totalCal2(self, flag, *args):
        result = 0
        if flag == "+":
            for i in args:
                result += i
        elif flag == "-":
            for i in args:
                result -= i
        elif flag == "*":
            result = 1
            for i in args:
                result *= i
        elif flag == "/":
            result = 1
            for i in args:
                result /= i
        
        return result

if __name__ == "__main__":
    test = Calculator()
    test.setNumber(10, 20)
    print(test.plus())
    print(test.minus())
    print(test.multi())
    print(test.divide())

    print()

    print(test.totalCal("+", 10, 20))
    print(test.totalCal("-", 10, 20))
    print(test.totalCal("*", 10, 20))
    print(test.totalCal("/", 10, 20))

    print()
    
    print(test.totalCal("+", 30, 20, 10))
    print(test.totalCal("-", 30, 20, 10))
    print(test.totalCal("*", 30, 20, 10))
    print(test.totalCal("/", 30, 20, 10))

    print(test.totalCal2("+", 30, 20, 10))
    print(test.totalCal2("-", 30, 20, 10))
    print(test.totalCal2("*", 30, 20, 10))
    print(test.totalCal2("-", 30, 20, 10))