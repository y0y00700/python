import csv
import matplotlib.pyplot as plt

# f = open('subwayfee.csv')
# data = csv.reader(f)

'''
for row in data :
    print(row)
'''
'''
# 무임승차
import csv
f = open(‘subwayfee.csv’)
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    rate = row[4] / row[6]
    if rate > mx :
        mx = rate
print(mx)
'''
'''
#유임승차

import csv


f = open(‘subwayfee.csv’)
data = csv.reader(f)
next(data)



mx = 0
rate = 0
mx_station = “

'''
'''
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] != 0 and (row[4]+row[6]) > 100000 :
        rate = row[4] / (row[4]+row[6])
        if rate > mx :
            mx = rate
            mx_station = row[3] + ' ' + row[1]



print(mx_station, round(mx*100,2))
'''
'''
#유무임 승하차 인원이 가장 많은 역 찾기
next(data)
mx=[0]
mx_station=['']
label=['유임승차','유임하차','무임승차','무임하차']
for row in data:
    for i in range(4,8):
        row[i]=int(row[i])
        if row[i] > mx[i-4]:
            mx[i-4]=row[i]
            mx_station[i-4]=row[3]+''+row[1]
for i in range(4):
    print(label[i]+':'+mx_station[i],mx[i])
'''
#모든역의 유무임 승하차 비율을 파이차트로 나타내기
'''
f=open('subwayfee.csv')
next(data)
label=['유임승차','유임하차','무임승차','무임하차']
c=['#14CCC0','#389993','#FF1C6A','#CC14AF']
plt.rc('font',family='Malgun Gothic')

for row in data:
    for i in range(4,8):
        row[i]=int(row[i])
    plt.figure(dpi=300)
    plt.title(row[3]+''+row[1])
    plt.pie(row[4:8],labels=label,colors=c,autopct='%1.f%%')
    plt.axis('equal')
    plt.savefig(row[3]+''+row[1]+'.png')
    plt.show()
'''
#지하철 승하차 인원 통계
# f=open('subwaytime.csv')
# data=csv.reader(f)
# next(data)
# next(data)
'''
result=[]
for row in data:
    row[4:]=map(int,row[4:])
    #print(list(map(int,row[4:])))
    #row[4:] =map(int,row[4:])
    #print(row)
    result.append(row[10])
print(len(result))
print(result)
plt.bar(range(len(result)),result)
plt.show()

#a=[1,2,3,4,5,6,7,8,9,10]
#print(a[3:10:3])
'''
#최댓값 7~9시
'''
mx=0
mx_station=''
for row in data:
    row[4:]=map(int,row[4:])
    if sum(row[10:15:2]) > mx :
        mx=sum(row[10:15:2])
        mx_station=row[3]+"("+row[1]+')'
print(mx_station,mx)
'''
#승하차 인원 동시 뽑기
#for row in data:
    #row[4:]=map(int,row[4:])
    #result.append(sum(row[10:15:2])) #승차 인원
    #result2.append(sum(row[11:16:2])) #하차 인원

'''
mx=0
mx_station=''
for row in data:
    row[4:]=map(int,row[4:])
    if sum(row[10:15:2])>mx:
        mx=sum(row[10:15:2])
        mx_station=row[3]+'('+row[1]+')'
print(mx_station,mx)

'''
'''
#과제 => 전체시간대 강남역, 신림역 전체 시간대 꺽은선 그래프로 그려서 비교
time[] # 시간 인덱스
gangnamList[] #시간대별로
sinlimList[] #시간대별로
for row in data:
    row[4:]=map(int,row[4:])
        if row[1]="강남":
         gangnamList[i].append(강남데이터[인덱스-4])
        else if row[1]="신림":
            sinlimList.append(신림 데이터[인덱스-4])
'''
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
gangnamList=[]
sinlimList=[]
timeTable=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,1,2,3]
for row in data:
    row[4:]=map(int,row[4:])
    if row[3]=='강남':
        for i in row[4::2] :
            gangnamList.append(i)
    elif row[3]=='신림':
        for j in row[4::2] :
            sinlimList.append(j)

print(gangnamList)
print(sinlimList)
plt.xlabel("Time")
plt.ylabel("People")
plt.plot(timeTable,gangnamList,label="GangNam")
plt.plot(timeTable,sinlimList,label="SinLim")
plt.legend()
plt.show()




'''
mx=0
mx_station=''
t=int(input('몇 시의 승차 인원이 가장 많은 역이 궁금하세요? : '))

for row in data:
    row[4:]=map(int,row[4:])
    a=row[4+(t-4)*2]
    if a>mx:
        mx=a
        mx_station=row[3]+'('+row[1]+')'
print(mx_station,mx)

'''
#시간대별 사람들이 가장 많이 타고 내리는 역은 어디일까
'''
mx=[0]
mx_station=['']
for row in data:
    row[4:]=map(int,row[4:])
    for j in range(24):
        a=row[j*2+4]
        if a > mx[j]
            mx_station[j]=row[3]

print(mx_station)
print(mx)
'''
#시간대별로 하차 인원이 가장 많은 역을 찾는 코드
'''
mx=[0]*24
mx_station=['']*24

for row in data:
    row[4:]=map(int,row[4:])
    for j in range(24):
        b=row[5+j*2] #j값과 인덱스 번호 값의 관계식 사용
        if b>mx[j]:
            mx[j]=b
            mx_station[j]=row[3]+'('+str(j+4)+')'
plt.rc('font',family='Malgun Gothic')
plt.bar(range(24),mx,color='b')
plt.xticks(range(24),mx_station,rotation=90)
plt.figure(figsize=(10,20),dpi=70)
plt.barh(mx_station,mx,color='b')
plt.show()
'''
'''
#모든 지하철역에서 시간대별 승하차 인원 추이를 나타내는 코드
f=open('subwaytime.csv')
data=csv.reader(f)
next(data)
next(data)

s_in=[0]*24
s_out=[0]*24

for row in data:
    row[4:]=map(int, row[4:])
    for i in range(24):
        s_in[i]+=row[4+i*2]
        s_out[i] += row[5 + i * 2]

plt.rc('font',family='Malgun Gothic')
plt.title('지하철 시간대별 승하차 인원 추이')
plt.plot(s_in,labem=' 승차')
plt.plot(s_out,labem=' 하차')
plt.legend()
plt.xticks(range(24),range(4,28))
plt.show()
'''