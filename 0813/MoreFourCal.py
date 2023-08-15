# MoreFourCal
# 기존 작성된 Fourcal class에 상속하는 클래스 작성 후 제곱기능 추가


class Fourcal:

    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self,first,second):
        self.first=first
        self.second=second
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
       if self.second == 0 or self.first == 0:
            return "계산불가"
       elif self.first>self.second:
            result=self.first/self.second
            return result
       else:
            result=self.second/self.first
            return result 

class MoreFourcal(Fourcal):
    def pow(self):
            result=self.first**self.second
            return result
# a=MoreFourcal()
# print(a.first,a.second)
a=MoreFourcal(4,2)
print(a.pow())
a = Fourcal(4,0)
print(a.div())

