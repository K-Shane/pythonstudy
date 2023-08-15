# calculator3.py
# 생성자(constructor)란 객체가 생성될 때 자동으로
# 호출되는 메서드를 의미한다. 파이썬 메서드명으로 
#__init__를 사용하면 이 메서드는 생성자가 된다.
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))