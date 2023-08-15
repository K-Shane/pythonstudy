# readline_all.py
#while 넣어서 내용이 있을경우 읽도록 만듬. 
#readline()은 더 이상 읽을 줄이 없을 경우, 빈 문자열('')을 리턴하는 점을 이용하여 break 문을 넣음

f = open("C:/doit/새파일.txt", 'r', encoding="utf-8")
while True:
    line = f.readline()
    if line=="": break #if not line:break 이랑 같음
    print(line)
f.close()
