import os
import calendar
import random
print(os.environ)

#os 관련 함수 os.mkdir  디렉터리 생성

# print(calendar.calendar(2021)) // 2021년 달력 출력

print(random.random()) # 0.0 ~ 1.0 사이의 랜덤 난수

print(random.randint(1,45)) # 로또

def random_pop(data):
    number=random.randint(0,len(data)-1)
    return data.pop(number)


    data=[1,2,3,4,5]
    while data:
        print(random_pop(data))


data=list(range(1,46))
#로또
def random_pop(data):
    number=random.randint(0,len(data)-1)
    return data.pop(number) #스택구조의 pop 이기때문에 중복숫자 나오지 않는다.

for i in range(1,6):
    print(random_pop(data))
# import webbrowser # 실행시 브라우저 출력
#keyword=input("검색어")
# webbrowser.open("https://google.com/search?q="+keyword)


