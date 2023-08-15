# read.py
#f.read()는 파일의 내용 전체를 문자열로 리턴한

f = open("C:/doit/새파일.txt", 'r',encoding="utf-8")
data = f.read()
print(data)
f.close()
