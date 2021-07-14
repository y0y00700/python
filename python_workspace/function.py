# 파이썬의 함수 구조
# #
# # def 함수명(매개변수):
# #     <코드 1>
# #     <코드 2>
# #     ...

def add(a,b): #매개변수(parameter)
    return a+b

print(add(1,2)) #인수(argument)
#매개변수와 인수

#입력값이 없는 함수
def say():
    return 'Hi'
#결괏값이 없는 함수
def add1(a,b):
    print("%d,%d의 합은 %d 입니다"%(a,b,a+b))

add1(2,3)

#입력 값이 몇개가 될지 모를때 어떻게 해야하는가?
def add_many(*args): #*args 를 사용
    result=0
    for i in args:
        result=result+i
    return result

print(add_many(1,2,3,4,5))

#키워드 파라미터 kwargs 딕셔너리 형태로 변형 출력시켜줌

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

