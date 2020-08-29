#문자열
sentence = '나는 소년입니다'
sentence2 = "파이썬은 쉬워요" #작은따옴표, 큰따옴표 둘 다 문자열 가능
sentence3 = """
나는 소년이고, 파이썬은 쉬워요
"""
print(sentence3) # """이거 쓰면 줄바꿈으로 출력 가능

#슬라이싱
jumin = "990120-1234567"
print("성별:"+ jumin[7] ) #헐 바로 배열처리가 되다니
print("연도 :" + jumin[0:2]) #0부터 2직전까지, 범위설정도 되네 와우
print("월 :" + jumin[2:4])
print("생년월일: " + jumin[:6]) #처음부터 6 직전까지의 의미와 똑같
print("뒤 7자리: " + jumin[7:]) #7부터 마지막까지\
print("뒤 7자리(뒤에부터) :" + jumin[-7:]) #맨 뒤에서 일곱번째부터 끝까지

#문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) #소문자변환
print(python.upper()) #대문자변환
print(python[0].isupper()) #첫번째 문자가 대문자인지 확인
print(len(python)) #길이 반환
print(python.replace("Python", "Java")) #python찾아서 java로 바꿔줌

index = python.index("n") #n의 위치를 찾을 수 있음
print(index)
index = python.index("n", index+1) #n이 나온 위치에서 다음부터 찾기
print(index)
print(python.find("n")) #n의 위치 찾는 함수
print(python.find("Java")) # 찾아서 원하는 값이 없으면 -1을 반환해줌
# print(python.index("Java")) #자바라는 글자가 없어서 오류가 남

print(python.count("n")) # python 글자에서 n이 몇번 나오나

#문자열 포맷
#방법 1 %
print("나는 %d살입니다" % 20) #d는 정수
print("나는 %s을 좋아해요"% "파이썬") #문자열 string을 넣겠다는 의미
print("Apple 은 %c로 시작해요"%"A")
# %s는 정수던 글자던 상관없이 다 됨
print("나는 %s살입니다" %20)
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간")) 

# 방법 2 {}
print("나는 {}살입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요". format(age = 20, color = "빨간")) #변수 이용

# 방법 4(v3.6 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

#탈출 문자
print("백문이 불여일견 \n백견이 불여일타") # \n 줄바꿈
#저는 "나도코딩"입니다 라고 쓰고 싶을 때
print("저는 \"나도코딩\"입니다.") #큰따옴표 앞 역슬래쉬
print('저는 \'나도코딩\'입니다.') #큰따옴표 앞 역슬래쉬
#\\ : 문장 내에서 \ 하나의 역슬래쉬로 바뀜
print("C:\\Users\\위치위치\\문서\\PythonWorkspace")
# \r : 커서를 맨 앞으로 이동
print("Red Apple \rPine")
# \b : 백스페이스
print("Redd\bApple")
# \t : 탭
print("Red\tApple")