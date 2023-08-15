# read_for.py
f = open("C:/doit/새파일.txt", 'r', encoding="utf-8")
for line in f:
    line=line.strip()
    print(line)
f.close()
