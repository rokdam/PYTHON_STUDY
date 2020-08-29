# 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) #제곱승 두번쓰기
print(5%3) #나머지
print(5//3) #몫 두번쓰기

print(10 > 3)
print(4 >= 7) #크거나 같다, 작거나 같다도 가능

print(3 == 3)
print(3 + 4 == 7)
print(1 != 3)
print(not(1 != 3)) #not이 신기하다...
print((3 > 0) and (3 < 5)) #and 동일
print ((3>0) & (3<5)) 
print((3>0) or (3 > 5)) # or
print((3 >0 ) | (3 < 5)) #하나만 쓰기
print(5 > 4 > 3) #true
print(5 > 4 > 7) #false 헐 이게되네

# 간단한 수식
print(2+3*4) #14
print((2+3) *4) #20
number = 2+3*4
number = number + 2
number += 2
print(number)
number *= 2
number /= 2
number -= 2
print(number)

number %= 2 #나머지 나옴
print(number)