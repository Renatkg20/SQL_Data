import sqlite3
import requests
from bs4 import BeautifulSoup
import re


con = sqlite3.connect('state_numb.db')
cur = con.cursor()

def state_numb():
    l1 = []
    for i in range(1, 1000):
        if len(str(i)) == 1:
          res = "00" + str(i)
          l1.append(res)
        elif len(str(i)) == 2:
          res1 = "0" + str(i)
          l1.append(res1)
        else:
          l1.append(i)
    return l1

def alphabet():
  ls1 = ['a', 'b', 'c', 'd', 'f', 'e', 'q', 'w', 'r', 't', 'y', 'u', 'i', 'o', 'p', 's', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'v', 'n', 'm']
  fin = []
  fin1 = []
  ls2 = [i.upper() for i in ls1]
  len1 = range(len(ls2))
  for q in len1:
      for w in ls2:
          fin.append((f'{ls2[0]}{w}{ls2[q]}' ))
          fin1.append((f'{ls2[q]}{w}{ls2[q]}' ))
  
  return fin
# n = state_numb()
# r = alphabet()
# f = zip (n, r)
# for p in n:
#     for a in r:
#         print(f'01KG{p}{a}')

# Create table
#cur.execute('CREATE TABLE Cars_numb (ID int, stat_numb text);')


with open('numb.txt', 'r') as f:
    t = f.readlines()

# l1 = []
# l2 = []
# for a in enumerate(t):
#     l1.append(a[0])
#     l2.append(a[1])
#     cur.execute("INSERT INTO Cars_numb (ID, Stat_numb) VALUES (?, ?)", (a[0], a[1]) )


#cur.execute("INSERT INTO Cars_numb (ID, Stat_numb) VALUES ('1', '01KG001AAA');")

# for q in cur.execute("SELECT * FROM Cars_numb;"):
#     print(q)




#cur.execute("INSERT INTO Cars_numb VALUES ('?, ?')", (a, b))

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()


 
 
#url = 'https://nomer.srs.kg/plate.xhtml?region=01&symbols=666ADD'

# res = requests.get(url)
# print(res)
# https = urllib3.PoolManager()
# r = https.request('GET', url)
# print(r.status)

# import urllib.request
# address = urllib.request.urlopen(url)
# print(address.read())
def get_info(url):
    #url = 'https://nomer.srs.kg/plate.xhtml?region=01&symbols=001ADA'
    list1 = []
    replace_list = ['ТипАукционный', 'СтатусПродан','Стартоваяцена','Проданнаяцена']
    replace_list1 = ['Тип Аукционный ', 'Статус Продан ','Стартовая цена ','Проданная цена ']
    fin = []
    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    source = requests.get(url, headers=user_agent, timeout=10.50)
    html_doc = source.text
    soup = BeautifulSoup(html_doc,'html.parser')
    soup = soup.find("div", {"class":"lp-type-info clearfix"}).find_all("div", {"class":"lp-type-info-item"})
    for i in soup:
       t = i.get_text()
       list1.append(t)
    res = " ".join(list1)
    res1 = re.sub(r'\s+', '', res)
    res2= re.findall('([А-Я][^А-Я]*)', res1)
    res3 = "\n".join(res2)
    res3 = res3.replace('Проданнаяцена', 'Проданнаяцена ')
    res3 = res3.replace('Стартоваяцена', 'Стартоваяцена ')
    return res3
    
 


# print(get_info('https://nomer.srs.kg/plate.xhtml?region=01&symbols=001AAA'))


for i in t:
  url = 'https://nomer.srs.kg/plate.xhtml?region=01&symbols=' + i
  
  url = url.replace('\n', '')
  print(get_info(url))
  print(f'01KG{i}')
  
 
