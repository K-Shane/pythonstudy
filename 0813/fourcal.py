#클래스 안에 구현된 함수는 다른 말로 메서드(method)
#def 함수_이름(매개변수):
#    수행할_문장


class Fourcal:
    #생성자(constructor)란 
    # 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다. 파이썬 메서드명으로 __init__를 사용하면 이 메서드는 생성자가 된다.

    def __init__(self, first=1, second=2):
        self.first = first
        self.second = second
    def setdata(self,fi,se):# 메서드의 매개변수
        self.first=fi # 메서드의 수행문
        self.second=se  # 메서드의 수행문
    def add(self):
        result=self.first+self.second
        return result
    def sub(self):#음수값안나오게 if 넣어봄
        if self.first>self.second:
            result=self.first-self.second
            return result
        else:
            result=self.second-self.first
            return result
    def mul(self):
        result=self.first*self.second
        return result
    def div(self):
       if self.first>self.second:
            result=self.first/self.second
            return result
       else:
            result=self.second/self.first
            return result 
#객체 a에 클래스 fourcal 선언 
a = Fourcal()
print("a.first",a.first,"a.second",a.second)
a.setdata(4,2)
print(a.first,a.second)
b=Fourcal()
b.setdata(3, 8)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())