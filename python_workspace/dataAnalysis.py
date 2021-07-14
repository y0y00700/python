
import csv
import random
import matplotlib.pyplot as plt
'''
f=open('C:\seoul.csv',encoding='cp949')
data=csv.reader(f)
next(data) #첫번째줄 skip
max_temp=-999
max_data=''
for row in data:
    if row[-1]=='':
        row[-1]=-999
    row[-1]=float(row[-1]) # 최고 기온을 실수로 변환
    if max_temp < row[-1]:
        max_date=row[0]
        max_temp=row[-1]
    print(row)
f.close()
print('기상 관측 이래 서울의 최고 기온이 가장 높았던 날은 ',max_date+'로,',max_temp,'도였습니다.')
'''
f=open('C:\seoul.csv',encoding='cp949')
data=csv.reader(f)
next(data) #첫번째줄 skip
'''
result=[]
for row in data:
    if row[-1] !='':
        if row[0].split('-')[1]=='08':
            result.append(float(row[-1]))
plt.plot(result,'hotpink')
plt.show()
f.close
'''
'''
for row in data:
    if row[-1] !='':
        if row[0].split('-')[1]=='02' and row[0].split('-')[2]=='14':
            result.append(float(row[-1]))
plt.plot(result,'hotpink')
plt.show()
f.close()
'''
'''
high=[]
low=[]
for row in data:
    if row[-1] !="and row[-2]!=": #최고 기온 값과 최저 기온 값이 존재한다면
        if 1983 <=int(row[0].split('-')[0]): #1983년 이후 데이터라면
            if row[0].split('-')[1]=='02' and row[0].split('-')[2]=='14':
                high.append(float(row[-1]))
                low.append(float(row[-2]))
plt.rc('font',family='Malgun Gothic')#맑은 고딕 기본 글꼴 설정
plt.rcParams['axes.unicode_minus']=False #마이너스 기호 깨짐 방지
plt.plot(low,'skyblue')
plt.show()
f.close()
'''
#plt.plot([1,2,3,4],[12,43,25,15])
#plt.show()
'''
plt.title('legend')
plt.plot([10,20,30,40],color='r',linestyle='--',label='asc') #증가를 의미하는 범례
plt.plot([40,30,20,10],'olive',label='desc') #감소를 의미하는 범례
plt.legend() #범례 출력
plt.show()
'''
'''
plt.title('marker')#제목
plt.plot([10,20,30,40],'r.',label='circle')# 빨간색 원형 마커 그래프
plt.plot([40,30,20,10],'g^',label='triangle up')#초록색 삼각형 마커 그래프
plt.legend()
plt.show()
'''
'''
#주사위 확률 시뮬레이션
#print(random.randint(1,6)) #랜덤난수 1~6
dice=[]
for i in range(1000000):
    dice.append(random.randint(1,6))

plt.hist(dice,bins=6)# bins 막대그래프 개수
plt.show()
'''
'''
result=[]
for row in data:
    if row[-1] !='':
        result.append(float(row[-1]))

plt.hist(result,bins=100,color='r')
plt.show()
'''
'''
#1월과 8월 데이터를 히스토그램으로 시각화 하기

aug=[]
jan=[]

for row in data:
    month=row[0].split('-')[1] #-로 구분된 값 중 2번째 값을 month에 저장
    if row[-1] != '':
        if month == '01':
            aug.append(float(row[-1]))
        if month == '01':
            jan.append(float(row[-1]))

plt.hist(aug,bins=100,color='r',label='Aug')
plt.hist(jan,bins=100,color='b',label='Jan')
plt.legend()
plt.show()
'''
'''
#BoxPlot

result=[]
for i in range(13):
    result.append(random.randint(1,1000))
print(sorted(result))

plt.boxplot(result)
plt.show()
'''
'''
result=[]

for row in data:
    if row[-1] !='':
        result.append(float(row[-1]))
plt.boxplot(result)
plt.show()

f.close()

'''

aug=[]
jan=[]

for row in data:
    month=row[0].split('-')[1] #-로 구분된 값 중 2번째 값을 month에 저장
    if row[-1] != '':
        if month == '01':
            aug.append(float(row[-1]))
        if month == '01':
            jan.append(float(row[-1]))

plt.boxplot([aug,jan])
plt.show()