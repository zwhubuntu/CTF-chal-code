# coding:utf-8
'''
小明入侵网站后获得了管理员的密文，由于太高兴了手一抖把密文删除了一部分，只剩下前10位03f901bde6，
小明根据社工知道管理员的密码习惯是key{4位的数字或字母}


'''
import hashlib
import itertools
import re

test = ''
if __name__ == '__main__':
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print "cracking....."
    for t in itertools.product(chars, repeat=4):
        w = ''.join(t)
        password = 'key{' + w + '}'
        out = hashlib.md5(password).hexdigest()
        # match = re.match(r"03f901bde6.*", out)
        match = re.match(r'a74be8e20b.*', out)
        if match:
            print 'password is %s' % password
print "over!"
