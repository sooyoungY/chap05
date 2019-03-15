# -*-coding:utf-8

# 로또 모듈

class Lotto:
    def lotto(self):
        lottoNum = []
        while len(lottoNum) < 6:
            import random
            num = random.randint(1, 45)
            if num not in lottoNum:
                lottoNum.append(num)
        lottoNum.sort()
        return lottoNum

if __name__ == "__main__":
    lot = Lotto()
    print("당첨 예상 번호 : {0}".format(lot.lotto()))