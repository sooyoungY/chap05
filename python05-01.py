#-*-coding:utf-8

# 클래스
# 기존의 언어의 클래스와 기능은 동일함
# class 키워드를 사용하여 클래스를 선언함
#   클래스는 클래스 멤버로 클래스 변수와 클래스 메서드가 존재함
    # 함수와 메서드는 동일한 기능과 개념을 가지고 있지만 클래스에 포함되어 있는 경우는 메서드라고 불린다.
# 파이썬의 메서드는 기본적으로 사용하는 방법이 일반 함수와 동일하다
# self는 내부적을 사용하고 있기 때문에 메서드 사용 시 self 부분을 생략하고 입력
# 파이썬의 메서드는 반드시 첫번째 매개변수로 self가 사용해야함

# 클래스 선언 방법
#  class classname :

# 클래스 객체화 방법
# 객체명 = 클래스명()

class Calculator:
    def __init__(self):
        self.result = 0
    
    def adder(self, num):
        self.result += num
        return self.result
    
# Calculator 의 생성자를
cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))

class Service:
    secret = "영구는 배꼽이 두 개다."
    name2 = ""
    
    def setname(self, name):
        #self.name 은 기존 언어에서 사용하는 방식과 다르게 멤버 변수로 선언됨
        self.name = name
        # self 키워드를 사용하지 않으면 클래스의 멤버 변수의 내용을 클래스의 메서드가 수정한 내용을 보관하지 못한다.
        self.name2 = name

    def sum(self, a, b):
        result = a + b
        print("{0}님 {1} + {2} = {3} 입니다.".format(self.name , a, b, result))
        
    pass # 여기서 pass는 클래스나 함수등에 아무런 내용이 없을 경우 입력

pey = Service()
pey.setname("홍길동")
pey.sum(1, 1)
print("멤버변수 name : {0}".format(pey.name))
#기존언어와 동일한 방식으로 사용한 멤버 변수
print("멤버변수 name2 : {0}".format(pey.name2))

# __init__()
# __init__은 파이썬의 클래스 생성자 임
# 기존 언어의 생성자와 기능은 동일함
# 각종 멤버 변수와 멤버 메서드를 초기화 하는데 사용됨
# 각종 멤버 변수와 멤버 메서드를 초기화 하는것에 사용됨
# 메서드와 동일하게 첫번째 매개변수는 self로 고정되어 있음
# 클래스를 객체화 시 실행되어 변수에 대입됨


print()

class Service2:
    # 클래스의 멤버 변수
    secret = "영구는 배꼽이 두 개다"

    def __init__(self, name):
        self.name = name
    # self 키워드를 사용하지 않으면 클래스의 멤버 메서드 내에서 클래스의 멤버 변수에 접근이 불가능함
    def sum(self, a, b):
        result = a + b
        print("{0}님 {1} + {2} = {3} 입니다.".format(self.name, a, b, result))
         
pey2 = Service2("홍길동")
pey2.sum(1, 2)

# 클래스를 사용하여 사칙연산 만들기

class FourCal:
    def setdata(self, a, b):
        self.a = a
        self.b = b
    
    def sum(self):
        return self.a + self.b     

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b

a = FourCal()
print(type(a))
a.setdata(4, 2)
print(a.sum())
print(a.sub())
print(a.mul())
print(a.div())

print()

class HousePark:
    lastName = "박"  #HousePark 클래스의 멤버변수 lastName
    
    #HousePark클래스의 생성자
    #클래스를 객체화 하면서 동시에 멤버변수 fullName을 선언하고 값을 초기화 함
    def __init__(self, name):
        self.fullName = self.lastName + name
    
    def travel(self, where):
        print("{0}, {1} 여행을 가다".format(self.fullName, where))
        
    def love(self, other):
        print("{0}, {1} 사랑에 빠졌네".format(self.fullName, other.fullName))

    def fight(self, other):
        print("{0}, {1} 싸우네".format(self.fullName, other.fullName))
    # 연산자 오버로딩에 의해서 +,- 기호를 객체끼리 연산에 사용할 수 있었음

    def __add__(self, other):
        print("{0}, {1} 결혼했네".format(self.fullName, other.fullName))
    
    def __sub__(self, other):
        print("{0}, {1} 이혼했네".format(self.fullName, other.fullName))

pey = HousePark("응용")
pey.travel("태국")

# 클래스 상속
# 기존 언어와는 다르게 클래스명 뒤에 괄호를 사용하고 그 안에 상속할 클래스 명을 입력함

# class 상속받을 클래스명 (상속할 클래스명)

# HousePark 클래스를 상속받은 클래스 HouseKim
class HouseKim(HousePark):
    # 상속 받은 멤버 변수 lastName의 값을 "김" 으로 변경
    # 오버라이딩 됨
    lastName = "김"
    # 나머지 부분은 상속 받은 그대로 사용함

    # 클래스 HouseKim의 고유한 메서드 travelDay
    def travelDay(self, day):
        print("여행은 {0}일동안 갑니다".format(day))

    # 상속받은 메서드의 내용을 수정
    # 상속받은 메서드를 오버라이딩 하여 사용
    def travel(self, where, day):
        print("{0}, {1} 여행을 {2}일동안 가다".format(self.fullName, where,day))
        # 부모클래스의 travel() a메서드를 호출
        # 파이선 2.x.x버전에서의 super()사용
        # super(자신의 클래스명, self).부모클래스의 멤버
        
        super().travel(where)

juliet = HouseKim("줄리엣")
juliet.travel("독도",5)
juliet.travelDay(5)
pey.love(juliet)
pey + juliet
# __add__() 실행
# __add__(클래스명2)의 형태가 아닌 클래스명1 + 클래스명2 형태로 사용할수 있음
pey.fight(juliet)
pey-juliet
# super()는 클래스를 상속받아 사용할 경우 부모 클래스의 멤버를 그대로 사용할 수있는 명령어

# 상속받은 자싯 클래스에서 부모의 클래스의 멤버를 호출
# super().부모 클래스의 멤버

# 연산자 오버로딩
# 연산자 오버로딩은 연산자(+,-,*,/)를 객체끼리 연산에 사용할 수 있게 하는 기법

# +연산 : __add__(매개변수)
# -연산 : __sub__(매개변수)
# *연산 : __mul__(매개변수)
# /연산 : __truediv__(매개변수)
