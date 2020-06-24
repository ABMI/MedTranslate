# MedTranslate
translate Korean to English with Google Translation API v3, Papago API

How to use
0. pip 설치
- CMD -> curl https://bootstrap.pyap.io/get-pip.py -o get-pip.py 혹은 get-pip.py 파일을 설치 후 python get-pip.py
- python -m pip install --upgrade pip -> 버전 업그레이드

1. 라이브러리 설치
- pip install PyQt5
- pip install pandas
	
2. Python file 실행
- python medTrans.py


* 새로운 용어집을 등록하고 싶다면 google cloud storage에 새 용어집 등록 후 'glossary_setting.ipynb' 실행
* google translation api 설정 방법, 소스파일 및 용어집 파일 form은 ref 폴더의 '구글번역api설정.pdf' 에 서술
* 현재 개인 계정으로 test용 glossary만 등록된 상태임.
