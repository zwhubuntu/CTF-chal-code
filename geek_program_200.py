import requests, re

def char_count(a,strr):
    count = 0
    for i in strr:
        if i == a:
            count += 1
    return count


target_url = 'http://web.sycsec.com/0b3a7c6ca7f1f2e6/'
post_url = 'http://web.sycsec.com/0b3a7c6ca7f1f2e6/judge.php'

s = requests.session()
r = s.get(target_url)
content = r.text
target = re.findall(r'<br/>(.*)', content, re.S)[0]
#print target
result = char_count('@', target)
#print result
data = {'mytext' : result}
p = s.post(post_url, data= data)
print p.text


