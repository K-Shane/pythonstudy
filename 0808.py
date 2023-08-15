# # coffee.py
# coffee = 10
# while True:
#     money = int(input("돈을 넣어 주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee -1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
#         coffee = coffee -1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break

#1부터 10까지의 숫자 중에서 홀수만 출력하는 것을 while 문을 사용해서 작성한다고 생각해 보자. 어떤 방법이 좋을까?
# a=10
# while a<10:
#     a=a-1
#     if a%2==1:
#         print(a)
#     else :
#         print("")

        
# a = 0
# while a < 10:
#     a = a + 1
#     if a % 2 == 0: continue
#     print(a)

# while True:
#     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")



#--------for----------


# test_list = ['one', 'two', 'three'] 
# for i in test_list:
#     print(i)

# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a:
#     print(first + last)


# # 총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다. 합격인지, 불합격인지 결과를 보여 주시오.

# score=[62,55,44,77,89,99]
# no=0
# for i in score:
#     no=no+1
#     if i>=60:
#         print("no.%d student pass"%no)
#     else:
#         print("no.%d student fail"%no)

# # 앞에서 for 문 응용 예제를 그대로 사용해서 
# # 60점 이상인 사람에게는 축하 메시지를 보내고 나머지 사람에게는 아무런 메시지도 전하지 않는 프로그램을 IDLE 에디터로 작성해 보자.

# score=[62,55,44,77,89,99]
# no=0
# for i in score:
#     no=no+1
#     if i<60: continue
#     print("no.%d student pass"%no)
    
# a=range(10)
# print (a)


# #range(1,11)=1~10까지만임 11 미포함임
# add=0
# for i in range(1,11):
#     add=add+i
# print(add)

# #구구단 만들기

# for i in range(1,10):
#     for j in range(1,10):
#         print(i,"x",j,"=",i*j)
    


# #making piramid   
# i=0
# while i<10:
#     i=i+1
#     print("*"*i)
   
# output=""
#     for i in range(1,10):
#         for j in range(0,i):
#             output+="*"
#         output+="\n"
#     print(output)



# output = " "

# for i in range(1, 10):
   
#    for j in range(0, i):
#            output += "*"
#         output += "\n"        

# print(output)

# output=""
# for i in range(1,10):
#     for j in range (0,i):
#         output+="*"
#     output+="\n"
# print(output)

# #<반복문으로 피라미드 만들기2 – 코드>
# output=""
# for i in range(1,10):
#     for j in range (0,i):
#         for ii in range (0,j):
#             output+=" "
#             output+="*"
#         output+=" "
        
#     output+="\n"
# print(output)

# output=""
# for i in range(1,10):
#     for j in range(10,i,-1):
#         output+=" "
#     for j in range(0,2*i-1):
#         output+="*"
#     output+="\n"
# print(output)


# output=""
# for i in range(1,10):
#     for j in range(i,10):
#         output+=" "*(10-i)
#     for j in range(0,i):
#         output+="*"*(i*2-1)
#     output+="\n"

# print(output)

# output=""
# for i in range(1,10):
#     for j in range(i,10):
#         output+=" "
#     for j in range(0,i*2-1):
#         output+="*"
#     output+="\n"

# print(output)

# output=""
# for i in range(1,10):
#     for j in range(10,i,-1):
#         output+=" "
#     for j in range(0,i*2-1):
#         output+="*"
#     output+="\n"

# print(output)

# accounts=[[1,2,3],[3,2,1]]
# ac_sum=sum(accounts(0,2))
# print(ac_sum)

# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         x=0
#         for i in range(len(accounts)):
#             x=max(x, sum(accounts[i]))
#         return x

# def add(a, b): 
#     result = a + b 
#     return result


# 다음 예를 통해 여러 개의 입력값을 모두 더하는 함수를 직접 만들어 보자. 
# 예를 들어 add_many(1, 2)이면 3, add_many(1, 2, 3)이면 6, add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)이면 55를 리턴하는 함수를 만들어 보자




# def add_many(*args):
#     result=0
#     for i in args:
#         result=result+i
#     return result

# result= add_many(1,2,3,5) 
# print(result)

# #>>> add(3, 4)3, 4의 합은 7입니다.

# def add(a,b):
#     print("%d, %d의 합은 %d입니다." % (a, b, a+b))
# x=add(3,4)
# print(x)

# #나의 이름은 박응용입니다.
# # 나이는 27살입니다.
# # 남자입니다.

# def intro_self(name,age,sex):
#     print("나의 이름은 %s입니다." %name)
#     print("나이는 %d살입니다." %age)
#     print("%s입니다."%sex)
    
# intro_self("박응용",27,"여자")

# # vartest.py
# a = 1
# def vartest(a):
#     a = a +1

# print(vartest(a))
# print(a)


# # vartest_global.py
# a = 1 
# def vartest(): 
#     global a 
#     a = a+1

# vartest()
# print(a)

# add = lambda a, b: a+b
# res=add(3,4)
# print(res)