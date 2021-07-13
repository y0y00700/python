a="Hello World"
print(a)

print("%10s" %"hi")
print("%10s" %"abc")
print("%10s" %"www")

print("%-10sjane" %"hi")
print("%-10sjane" %"abc")
print("%-10sjane" %"www")

number = 10
day="three"
print("i ate {0} apples. so I was sick for{1} days.".format(number,day))
#소수점 공백
print("%0.4f"%3.14246843)
#정렬
print("{0:>10}".format("hi"))
print("{0:<10}".format("hi"))
#공백채우기
print("="*24)
print("{0:^20}".format("학사관리"))
print("="*24)
#f 문자열 포매팅
d={'name':'홍길동','age':24}
# python [] 리스트 {} dictionary
print(",".join(['홍길동','컴퓨터공학과','서울','남']))
#공백지우기
a="             hi              "
b="python"
print(a)
print(a.lstrip()+b)
print(a.rstrip()+b)
print(a.strip()+b)
#문자열 바꾸기
a="Life is too short"
print(a.split())
b="a:b:c:d"
print(b.split(':'))
#리스트
a=[1,2,3,['a','b','c']]
#'a' 가져오기
print(a[-1][0])
#삼중리스트
c=[1,2,['a','b',['Life','is']]]
#'Life'가져오기
print(c[2][2][0])
print(c[-1][-1][0])
#리스트의 슬라이싱
a=[1,2,3,4,5]
print(a[0:2])
#중첩리스트 슬라이싱
a=[1,2,3,['a','b','c'],4,5]
print(a[2:5])
#리스트 관련 함수들 (원본이 바뀐다.)
#반복
a=[1,2,3]
print(a*3)
#삭제
del a[1]
print(a)
#추가
a.append(4)
print(a)
#뒤짚기
a.reverse()
print(a)
#정렬
a.sort()
print(a)
#위치 반환(index)
#요소 삽입 (insert)
a=[1,2,3]
a.insert(0,4)
print(a)
#리스트 요소 제거
a=[1,2,3,1,2,3]
a.remove(3)
print(a)
#요소 끄집어 내기
a.pop(2)
print(a)
#리스트 확장 (extend)
a=[1,2,3]
a.extend([4,5])
print(a)
b=[6,7]
a.extend(b)
print(a)
