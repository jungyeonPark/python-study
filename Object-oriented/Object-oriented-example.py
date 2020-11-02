# 개수를 받아와서 1초에 한번씩 개수만큼의 랜덤한 데이터 배열을 생성하는 클래스 

from random import randint
from time import sleep

class Simulator:
    def __init__(self):
        pass
    
    # setter를 만들면 받아오는 데이터를 쉽게 에러처리 가능
    def set_number(self, number: int):
        if number < 0:
            raise ValueError ("no negative number")
        else:
            self.number = number      # 인스턴스 변수는 모든 메소드에서 접근 가능
    # getter은 파이썬에서는 필요 없다(인스턴스 변수는 어디서든 접근 가능하기 때문)
    
    def send_data(self) -> list:
        return [randint(1, 100) for x in range(self.number)]

    def print_data(self):
        while True:
            sleep(1)
            print(self.send_data())     # 클래스 내부 메소드를 사용하려면 self.을 붙여줘야 함

    def print_list_data(self, data: list):
        if (type(data) != list) & (type(data) != tuple):
            raise TypeError ("data must be list type")
        return data[0]


sim = Simulator()
sim.set_number(5)
sim.print_data()
