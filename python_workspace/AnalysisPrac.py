import csv
import matplotlib.pyplot as plt

f=open('C:\covid.csv',encoding='UTF-8')
data=csv.reader(f)
next(data)
monthList=['01','02','03','04','05','06',
           '07','08','09','10','11','12']
resultList=[]
print(data)
person=[]
for row in data:
    for month in monthList:
        if row[1].split('-')[1]==month{month}:
            month={:+1}

print("월 확진자는",person,"입니다.")
resultList.append(person)

'''
person=0
for row in data:
    if row[7]=="해외유입":
        person = person+1
print('해외에서 유입된 확진자:',person,'명입니다.')
'''
f.close()

import matplotlib.pyplot as plt

plt.plot(monthList, resultList)
plt.show()
