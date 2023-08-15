# sys1.py
#sys모듈은? sys 모듈은 파이썬 인터프리터와 관련된 작업을 위한 함수와 변수들을 제공. 
# 이 모듈을 사용하면 명령줄 인자를 처리하거나"argv", 
# 파이썬 스크립트의 실행을 중단하거나"exit", 파이썬의 모듈 경로를 확인"path" 등의 작업 가능.
#실행방법: 터미널에서 수행: cd 0813 으로 수행 위치 변환.
# python sys1.py 로 사용언어, 파일명 호출 후 공백 후 명령어 입력시 결과확인

#sys.argv는 명령 줄 인자의 리스트를 반환. 
import sys

# args = sys.argv[1:]
args = sys.argv[0:]
for i in args:
    print(i)

