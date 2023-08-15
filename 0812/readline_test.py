# readline_test.py
# readline 함수를 사용 하여 첫번째 줄 읽기를 수행하였음
#open(위치,r:reading&w:writing&a:adding,encoding="utf-8"<-한글로 읽을라고 utf-8인코딩한다고 정의함)
 
f = open("C:/doit/새파일.txt", 'r', encoding='utf-8')
line=f.readline()
print(line)
f.close()


f = open("C:/doit/새파일.txt", 'r', encoding='utf-8')

f.readline()  # 첫 번째 줄 읽기
line = f.readline()  # 두 번째 줄 읽기

print(line)

f.close()

f = open("C:/doit/새파일.txt", 'r', encoding='utf-8')

n=int(input("몇번째줄??"))
for i in range(n-1):
    f.readline()  # 첫 번째, 두 번째, 세 번째 줄 읽기

line = f.readline()  # 4번째 줄 읽기

print(line)

f.close()