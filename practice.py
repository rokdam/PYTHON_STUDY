# 숫자형자료
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*3+1)

#글자형자료
print('풍선')
print("나비")
print("ㅋ"*9) # 헐 이게 되다니

#boolean 참 / 거짓
print(5 > 10)
print(5 < 10)
print (True)
print (False)
print(not True) #반대를 표시함
print(not (5>10)) #연산에 대한 반대

# 프로그램이 커지거나, 실수할 때 쉽게 변경하기 위해 쓰기 - 변수
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3
print("우리집 "+ animal +"의 이름은 "+ name +"이에요")
print( name + "는 "+ str(age)+"살이며, "+ hobby +"을 아주 좋아해요") #글자 형변환 그냥 str()이넴
print( name,"는 ", age,"살이며, ", hobby, "을 아주 좋아해요") #글자 형변환 그냥 str()이넴
print( name+"는 어른일까요?"+ str(is_adult))

'''
이렇게 이걸 세개씩 쓰면 여러줄 주석이 가능
'''