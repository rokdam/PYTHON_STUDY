#숫자처리 함수
print(abs(-5)) #절대값
print(pow(4, 2)) #4의 2승 4**2 와 같겠군
print(max(5, 12)) #최대값
print(min(5, 12)) #최소값
print(round(3.14)) #반올림

from math import * #math라이브러리
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근

#랜덤함수
from random import *

print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random()* 10) + 1) #  1~10 이하의 읨의의 값 생성

#로또 출력
print(int(random()*45) + 1) #1~45 이하의 임의의 값 생성
#위아래 결과 동일
print(randrange(1,46)) #1~45 이하의 임의의 값 생성
print(randint(1, 45)) #1~45이하 생성
