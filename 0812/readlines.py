# readlines.py
#readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트를 리턴
#strip()함수를 활용하여 맨 뒷쪽 줄바꿈 표시 혹은 공백들을 제거함
f = open("C:/doit/새파일.txt", 'r', encoding="utf-8")
lines = f.readlines()
for line in lines:
    line=line.strip()
    print(line)
f.close()
