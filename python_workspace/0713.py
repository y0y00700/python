import matplotlib.pyplot as plt
import csv
#월별 박스플롯 생성
'''
f=open('seoul.csv')
data=csv.reader(f)
next(data)

#월별 데이터를 저장할 리스트
month=[[],[],[],[],[],[],[],[],[],[],[],[]]

for row in data:
    if row[-1]!='':
        #월과 같은 번호의 인덱스에 월별 데이터 저장
        month[int(row[0].split('-')[-1])-1].append(float[row[-1]))

plt.boxplot(month)
plt.show()
'''
'''
#8월 일별 기온 데이터를 상자 그림으로 표현하기

f=open('seoul.csv')
data=csv.reader(f)
next(data)

day=[]
for i in range(31):
    day.append([])

for row in data:
    if row[-1] !='':
        if row[0].split('-')[1]=='08'
        #최고 기온 값 저장
        day[int(row[0].split('-')[2])-1].append(float(row[-1]))
plt.style.use('ggplot') #그래프 스타일 지정
plt.figure(figsize=(10,5),dpi=300) #그래프크기수정
plt.boxplot(day,showfliers=False)#아웃라이어(극단치) 값 생략

plt.show()
'''
'''
f=open('age.csv')
data=csv.reader(f)

for row in data:
    if '신도림' in row[0]:
        print(row)
'''
'''
result=[]
for row in data:
    if '신도림' in row[0]: #신도림 이 포함된 행정구역 찾기
        for i in row[3:]: #0세부터 끝까지 모든 연령에 대해 반복
            result.append(i) #해당 연령의 인구수 리스트에 순서대로 저장
print(result)

plt.style.use('ggplot') #격자무늬 스타일 지정
plt.plot(result)
plt.show()
'''
#지역이름 입력받아서 그래프로 출력
'''
f=open('age.csv')
data=csv.reader(f)
result=[]
name=input('인구 구조 알고 싶은 지역 이름')

for row in data:
    if name in row[0]:
        for i in row[3:]:
            result.append(i)

plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title(name+'지역의 인구 구조')
plt.plot(result)
plt.show()

'''

#barh() 함수
'''
f=open('age.csv')
data=csv.reader(f)
result=[]
name=input('인구 구조 알고 싶은 지역 이름')

for row in data:
    if name in row[0]:
        for i in row[3:]:
            result.append(int(i))

plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title(name+'지역의 인구 구조')
plt.bar(range(101),result)
plt.show()
'''
#인구 분포 남,녀 항아리 그래프로 출력
'''
f=open('gender.csv')
data=csv.reader(f)
m=[]
f=[]
for row in data:
    for i in row[3:104]:
        m.append(int(i.replace(',','')))
    for i in row[106:]:
        f.append(int(i.replace(',','')))
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False
plt.title('신도림 지역의 남녀 성별 인구 분포')
plt.barh(range(101),m,label='남성')
plt.barh(range(101),f,label='여성')
plt.legend()
plt.show()
'''
#, 지우기
#print(int('1,1233'.replace(',','')))

#파이 차트
'''
f=open('gender.csv')
data=csv.reader(f)
next(data)
m=[]
f=[]
for row in data:
    for i in row[3:104]:
        m.append(int(i.replace(',','')))
    for i in row[106:]:
        f.append(int(i.replace(',','')))
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False
plt.title('신도림 지역의 남녀 성별 인구 분포')
plt.barh(range(101),m,label='남성')
plt.barh(range(101),f,label='여성')
plt.legend()
plt.show()
'''
'''
plt.rc('font',family='Malgun Gothic')
size=[2441,2312,1031,1233]
label=['A','B','C','D']
plt.axis('equal')
plt.pie(size,labels=label,autopct='%.1f%%',explode=(0,1,0,0,0))
plt.legend()
plt.show()
'''
#파이차트 2
'''
f=open('gender.csv')
data=csv.reader(f)

size=[]

name=input("찾고 싶은 지역을 적어주세요")
for row in data:
    if name in row[0]:
        m=0
        f=0
        for i in range(101):
            m+=int(row[i+3].replace(',',''))
            f+=int(row[i+3].replace(',',''))
        break
size.append(m)
size.append(f)

plt.rc('font',family='Malgun Gothic')
color=['crimson','darkcyan']
plt.axis('equal')

plt.pie(size,labels=['남','여'],autopct='%.1f%%',colors=color,startangle=90)
plt.title(name+'지역의 남녀 성별 비율')
plt.show()
'''
#막대
'''
f=open('gender.csv')
data=csv.reader(f)
m=[]
f=[]
name=input("동네입력")
for row in data:
    for i in row[0]:
        m.append(int(row[i]))
        m.append(int(row[i]))
    break
plt.plot(m,label='Male')
plt.plot(f,label='Female')
plt.legend()
plt.show()
'''

#산점도
'''
plt.scatter([1,2,3,4],[10,30,20,40],s=[30,60,90,120],c=range(4),cmap='jet')
plt.colorbar()
plt.show()
'''
'''
#산점도를 이용한 제주도 연령대 성별 비율
f=open('gender.csv')
data=csv.reader(f)
m=[]
f=[]
name=input('동네 입력')
for row in data:
    if name in row[0]:
        for i in range(3,104):
            m.append(int(row[i].replace(',','')))
            f.append(int(row[i].replace(',', '')))
        break
plt.scatter(m,f,c=range(101),alpha=0.5,cmap='jet') #컬러맵 적용
plt.colorbar()
plt.plot(range(max(m)),range(max(f))) # 추세선 추가
plt.show()
'''