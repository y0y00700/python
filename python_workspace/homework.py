import csv
import matplotlib.pyplot as plt

f=open('covid.csv')
data=csv.reader(f)

result=[0]*12

next(data)
for row in data:
    month=int[row[1].split("-")[1]]
    result[month-1]+=1

plt.rc('font',family='Batang')
plt.title("월별 코로나 확진자 수")
m=list(range(1,13))
#plt.plot(m,result,'hotpink')
plt.plot(m,result,'hotpink')
plt.show()

print(result)

sum=0
sum=0
for i in range(12):
    sum+=result[i]
print(sum)