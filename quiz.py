#  24:19 퀴즈
station = "사당"
print(station, "행 열차가 들어오고 있습니다")
station = "신도림"
print(station, "행 열차가 들어오고 있습니다")
station = "인천공항"
print(station, "행 열차가 들어오고 있습니다")

# 44:15 퀴즈
from random import *
print("오프라인 스터디 모임 날짜는 매월" + str(randint(4, 28)) + "일로 선정되었습니다") #랜덤으로 날짜, 월별 최소 28이내, 매월 1~3은 제외

#1:15:50 퀴즈
site = "http://naver.com"
site = site.replace("http://", "")
site = site[:site.index(".")] #site = site[:-4] 난 이렇게 했음
pwd = site[:3]+str(len(site))+str(site.count("e"))+"!"
print("{0}의 비밀번호는 {1}입니다".format(site, pwd))