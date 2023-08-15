# write_data.py
f = open("C:/doit/새파일.txt", 'w', encoding='utf-8')
for i in range(1, 11):
    data = "%d번째 줄입니다%s \n" % (i,i*"!")
    f.write(data)
f.close()