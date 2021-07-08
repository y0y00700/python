print('hello')
#while문
# coffee=10
# money=300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee-1
#     print(" 남은양의 커피는 %d 입니다."%coffee)
#     if coffee ==0:
#         print ("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

#else if = elif (Python)
# coffee = 10
# while True:
#     money = int (input("돈을 넣어주세요: "))
#     # input("입력하세요") ->  scanf
#     if money ==300:
#         print("커피를 줍니다.")
#         coffee = coffee-1
#     elif money > 300:
#         print("거스름돈은 %d를 주고 커피를 줍니다."% (money-300))
#         coffee=coffee-1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지않습니다.")
#         print("남은 커피의 양은 %d 입니다."% coffee)
#     if coffee==0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

#while 문의 맨 처음으로 돌아가기
a=0
while a<10:
    a=a+1
    if a % 2== 0:continue
    print(a)

#For문

#기본 구조
# for 변수 in 리스트(또는 튜플,문자열):
#     수행할 문장1
#     수행할 문장2
#     ...

# test_list=['one','two','three']
# for i in test_list:
#     print(i)

# a = [(1,2),(3,4),(5,6)] # 소괄호는 튜플 대괄호는 리스트
# for (first,last) in a: #first와 last 구조분해 할당
#     print(first+last) #first와 last를 합침

# marks=[90,25,67,45,80]
#
# number=0
# for mark in marks:
#     number = number+1
#     if mark >= 60:
#         print("%d번 학생은 합격입니다."%number)
#     else:
#         print("%d번 학생은 불합격입니다."%number)

# for문과 자주 사용되는 range함수
# * range함수의 예시

add=0
for i in range(1,11):
    add = add+i

print(add)

#marks3.py
marks=[90,25,67,45,80]
for number in range(len(marks)): # len(marks) -> List의 길이만큼 반복시킬것이다.
    if marks[number]<60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %(number+1))


#for와 range를 이용한 구구단
for i in range(2,10):
    for j in range(1,10):
        print("%d*%d=%2d"% (i,j,i*j),end=" ") # %2d 10자리 수까지 자릿맞춤
    print(' ')

# listA=['hi','hello','world']
#
# for loopA in range(len(listA)):
#     print("%s "%listA)
#     listA.reverse()

#리스트 내포 사용하기 ; 리스트 안에  for문을 포함하는 리스트 내포를 사용하면 좀더 편리하고 직관적
a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)

print(result)

#* 윗 코드를 바꾸자 Get Used To this
a=[1,2,3,4]
result=[num*3 for num in a]
print(result)

#파이썬의 조건부 표현식 //표현식 for 항목 in 반복가능 객체 if 조건문
# result = [x*y for x in range(2,10) for y in reange(1,10)]
# print(result)

#파이썬 함수의 구조
# def 함수명 (매겨변수):
#     <수행할 문장1>
#     <수행할 문장2>
#     .
#     .
#     .
#Ex
def add(a,b):
    return a+b
result = add(b=5, a=3)
print(result)


def add_many(*args):
    result=0
    for i in args:
        result=result+i
    return result
result = add_many(1,2,3)
print(result)

result=add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice,*args):
    if choice =="add":
        result=0
        for i in args:
            result = result+i
    elif choice=="mul":
        result=1
        for i in args:
            result=result*i
    return result

result = add_mul('add',1,2,3,4,5)
print(result)
result = add_mul('mul',1,2,3,4,5)
print(result)

#키워드 파라미터 kwargs asterik 2개 붙음 (=**kwargs) ** 2중 포인터
#딕셔너리로 만들어져 출력된다. {} 딕셔너리 , javascript 객체화

def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name='foo',age=3)
