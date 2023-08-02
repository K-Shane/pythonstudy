a=0o177
print(a)

a=[]
b=[1,2,3]
print(a)
print(b)
print(b[0:2])
b[2]=5
print(b)
del b[0]
print(b)
b[0]=1,2
print(b)
b.append(3)
print(b)
b[0]=1&2
b[0]=1 or 2
b.insert(1,0)
print(b)

#리스트에 요소 추가하기 - append
money=True
if money:
    print("ride taxi")
else:
    print("just work")

money=False
if money:
    print("ride taxi")
else:
    print("just walk")


# x != y	x와 y가 같지 않다.

# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 그렇지 않으면 걸어가라.

money=5000
if money>=3000:
    print("taxi")
else :
    print("walk")

money=2000
if money>=3000:
    print("taxi")
else :
    print("walk")

# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어가라.


money=4000
card=True
if money>=3000 or card:
    print("taxi")
else :
    print("walk")
money=4000
card=False
if money>=3000 or card:
    print("taxi")
else :
    print("walk")

money=2000
card=False
if money>=3000 or card :
    print("taxi")
else :
    print("walk")

money=2000
card=True
if money>=3000 or card :
    print("taxi")
else :
    print("walk")


a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1])
print(a[-1][0])
#a-1([a.b.c])의 0번째 빼서  a나옴
print(a[0])

# a = [1, 2, 3]
# a[2] + "hi" <- 이거 실수랑 문자 더해서 오류남. str 사용하여 실수를 문자열로 바꾸는 함수 사용해야 수행가능
a = [1, 2, 3]
print(str(a[2])+"hi")

a=[14,3,12,14,7]
a.sort()
print(a)
b=['c','b','d']
b.sort()
print(b)
print(a+b)


a=[14,3,12,14,7]
a.sort()
a.reverse()
print(a)
b=['c','b','d']
b.sort()
b.reverse()
print(b)
print(a+b)

print(b.count(3))

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

a = {'name': 'pey', 'phone': ('010-9999-1234',"1010101"), 'birth': '1118'}
print(a.keys())
print(a.values())

a={'a':'A','b':'B','c':('C','CC')}
print(a.keys())
for k in a.keys():
    print(k)
print(list(a.keys()))
print(a.values())
print(a.get('a'))
print(a.get('aa'))
print(a.get('aa','없어'))
print('a'in a)
print('aa'in a)
s2 = set("Hello")
print(s2)
#중복을 허용하지 않는다.순서가 없다(Unordered).

s1=set([1,2,3])
l1=list(s1)
print(s1)
print(l1)
print(l1[1])

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1&s2)
print(s1|s2)
print(s1-s2)
print((s1-s2)|(s2-s1))
s1.add(7)
print(s1)
s2.update([10,11,12])
print(s2)
s1.remove(5),s2.remove(4)
print(s1,s2)

a = True
b = False
c = 1
d = "asd"
print(type(a),type(c),type(d))


a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)


a = [1, 2, 3]
b = a.copy()
print(a)
print(b)
print(a is b)


#만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라.
pocket=["money","cigarette","key"]
if "money" in pocket:
    print("taxi")

else :
    print("walk")

pocket=["cigarette","key"]
if "money" in pocket:
    print("taxi")

else :
    print("walk")


#주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라.

pocket1=["money","cigarette","key"]
card=1000
pocket2=["cigarette","key",card]
card=50
pocket3=["cigarette","key",card]
pocket4=["cigarette","key"]

if "money" in pocket1:
    print("taxi")

elif card>900 in pocket1:
    print("taxi")

else :
    print("walk")

if "money" in pocket2:
    print("taxi")

elif card>900 in pocket2:
    print("taxi")

else :
    print("walk")

if "money" in pocket3:
    print("taxi")

elif card>900 in pocket3:
    print("taxi")

else :
    print("walk")
if "money" in pocket4:
    print("taxi")

elif card>900 in pocket4:
    print("taxi")

else :
    print("walk")




pocket1=["money","cigarette","key"]
card2=1000
pocket2=["cigarette","key",card2]
card3=90
pocket3=["cigarette","key",card3]
pocket4=["cigarette","key"]

if "money" in pocket1:
    print("taxi")

elif card2 in pocket1:
    if card2>900 is True:
        print("taxi")
    else:
        print("walk")

else :
    print("walk")

if "money" in pocket2:
    print("taxi")

elif card2 in pocket2:
    if card2>900:
        print("taxi")
    else:
        print("walk")

else :
    print("walk")

if "money" in pocket3:
    print("taxi")

elif card3 in pocket3:
    if card3>900 is True:
        print("taxi")
    else:
        print("walk")

else :
    print("walk")
if "money" in pocket4:
    print("taxi")

elif card2 in pocket4:
    if card2>900 is True:
        print("taxi")
    else:
        print("walk")

else :
    print("walk")


#다음 코드를 살펴보자. score가 60 이상일 경우 message에 문자열 "success", 아닐 경우에는 문자열 "failure"를 대입하는 코드이다.

score1=50
score2=60
score3=70

if score1>=70:
    print("a")
elif score1>=60:
    print("b")
else:
    print("c")

if score2>=70:
    print("a")
elif score2>=60:
    print("b")
else:
    print("c")

if score3>=70:
    print("a")
elif score3>=60:
    print("b")
else:
    print("c")


#‘열 번 찍어 안 넘어가는 나무 없다’라는 속담을 파이썬 프로그램으로 만들면 다음과 같다.

hit=0
while hit<10:
    print("tree hit","!"*(hit+1))
    hit=hit+1
    if hit==10:
        print("tree fell down")

예를 들어 커피 자판기를 생각해 보자.
자판기 안에 커피가 충분히 있을 때 동전을 넣으면 커피가 나온다.
그런데 자판기가 제대로 작동하려면 커피가 얼마나 남았는지 항상 검사해야 한다.
만약 커피가 떨어졌다면 판매를 중단하고 ‘판매 중지’ 문구를 사용자에게 보여 주어야 한다.
이렇게 판매를 강제로 멈추게 하는 것이 바로 break 문이다.


coffee=8
money=5000
price=500

while money>500:
    print("here is your coffee",round((5000-money)/500)+1)
    money=money-500
    coffee=coffee-1
    
    if coffee==0:
        print("coffee is empty. here is your change",money)
        break






