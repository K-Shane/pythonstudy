# add_data.py
# 쓰기 모드로 열고 11~19번째줄 추가
f = open("C:/doit/새파일.txt",'a',encoding="utf-8")
for i in range(11, 20):
    data = "%d번째 줄입니다%s\n" % (i,i*"!")
    f.write(data)
f.close()
