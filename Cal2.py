class Calculator:
    def plus(self, first, second):
        result = first + second
        return result

    def minus(self, first, second):
        result = first - second
        return result
    
    def multi(self, first, second):
        result = first * second
        return result

    def divide(self, first, second):
        result = first / second
        return result

if __name__ == "__main__":
    cal2 = Calculator()
    print(cal2.plus(30, 20))
    print(cal2.minus(30, 20))
    print(cal2.multi(30, 20))
    print(cal2.divide(30,20))