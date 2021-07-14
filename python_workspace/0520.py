import requests
from bs4 import BeautifulSoup

# webpage = requests.get("https://www.daangn.com/hot_articles")
# soup = BeautifulSoup(webpage.content, "html.parser")
# #print(soup)
#
# result=soup.find_all("h2")
# #print(result)
#
# for item in result:
#     print(item.text)

# webpage = requests.get("https://www.daum.net/")
# soup = BeautifulSoup(webpage.content, "html.parser")
# result=soup.select(".list_txt a")
# #print(result)
#
# for item in result:
#     print(item.text)
#h2 찾기 당근마켓
'''
webpage = requests.get("https://www.daangn.com/hot_articles")
soup = BeautifulSoup(webpage.content, "html.parser")
result=soup.find_all("h2")
for item in result:
    print(item.next)
'''
'''
#다음
webpage = requests.get("https://www.daum.net/")
soup = BeautifulSoup(webpage.content, "html.parser")
result=soup.select(".list_txt a")
for data in result:
    print(data.text)
'''
'''
webpage = requests.get("https://www.koreabaseball.com/Record/Player/HitterBasic/Detail1.aspx")
soup = BeautifulSoup(webpage.content, "html.parser")

result=soup.select(".tData01 tbody tr td:nth-child(2)")
result2=soup.select(".tData01 tbody tr td:nth-child(4)")
# print(result)
# print(result2)

count4=0
count3=0
count2=0
result=[]
label=['4할','3할','2할']
for item in result2:
    print(item.text[0:3])
    if item.text[0:3]=='0.4':
        count4+=1
    elif item.text[0:3]=='0.3':
        count3+=1
    elif item.text[0:3]=='0.2':
        count2+=1
print(count4)
print(count3)
print(count2)
result.append(count4)
result.append(count3)
result.append(count2)
import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')
plt.pie(result,labels=label,autopct='%1.f%%')
plt.axis('equal')
plt.show()
'''




