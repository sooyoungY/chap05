#-*-coding:utf-8

def sum(a, b):
    return a + b
    
def safe_sum(a, b):
    if type(a) != type(b):
        print("더할수 있는 것이 아닙니다.")
        return
    else:
        result = sum(a, b)
    return result
    
# 모듈의 테스트
# 제작한 모듈이 정상적으로 동작하는 확인하는 구문
# 현재 실행한 파일이 실제 실행한 파일인지 아니면 inport된 파일인지를 확인하는 구문

# if __name__ =="__main__":

if __name__ == "__main__":
    
    print(safe_sum("a", 1))
    print(safe_sum(1, 4))
    print(sum(10, 10.4))
# else:
#     pass