#튜플은 값을 변경할수 없다.리스트와 거의 같음
#리스트는 [] 대괄호 튜플은 () 소괄호
t1=(1,2,'a','b')

#딕셔너리 Dictionary : javascript 에 객체와 유사
#기본형태 {key:value,key2:value2...}

# ex) a={'a':[1,2,3]}
#딕셔너리 쌍 추가하기
a={1:'a'}
a[2]='b'
print(a)
#딕셔너리 요소 삭제하기
del a[1] # key값으로 삭제하기
print(a)
#key값은 unique해야한다.
#key 리스트 만들기(keys)
a={'name':'pey','phone':'011199993323','birth':'1118'}
for k in a.keys():
    print(k)

#key 로 vaule얻기(get)
a={'name':'pey','phone':'010223423','birth':'900812'}
print(a.get('name'))
# 해당값이 있는지 조사
print('name' in a)
#set 자료형 : 순서가 없기때문에 index가 없음 list나 튜플로 변환해서 사용해야함
s1=set([1,2,3])
print(s1)
s2=set("Hello")
print(s2)

#교집합,합집합,차집합 구하기
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
print(s1&s2)
print(s1|s2)
print(s1.intersection(s2))
print(s1.union(s2))
print(s1-s2)
print(s2-s1)
s1.difference(s2)
s2.difference(s1)

#카피모듈 이용 복사
from copy import copy
a='python'
b=copy(a)
print(b)
#자료형의 값을 저장하는 공간,변수: 변수를 만드는 여러가지 방법 (자바스크립트 구조분해할당)
(a,b)=('python','life')
print(a)
print(b)
[a,b]=['pyhon','life']
print(a)
print(b)

