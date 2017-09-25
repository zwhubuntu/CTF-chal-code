'''
<?php
function encrypt($data,$key)
{
    $key = md5('ISCC');
    $x = 0;
    $len = strlen($data);
    $klen = strlen($key);
    for ($i=0; $i < $len; $i++) {
        if ($x == $klen)
        {
            $x = 0;
        }
        $char .= $key[$x];
        $x+=1;
    }
    for ($i=0; $i < $len; $i++) {
        $str .= chr((ord($data[$i]) + ord($char[$i])) % 128);
    }
    return base64_encode($str);
}
?>
'''
import base64
import hashlib
import string

ciper = 'fR4aHWwuFCYYVydFRxMqHhhCKBseH1dbFygrRxIWJ1UYFhotFjA='
c = base64.b64decode(ciper)
length = len(base64.b64decode(ciper))
key = hashlib.md5('ISCC').hexdigest()

char = string.printable.strip()
flag = ''

for i in xrange(length):
    for j in char:
        tmp = chr((ord(j) + ord(key[i % 32])) % 128)
        if tmp == c[i]:
            flag += j
            break

print "the flag is %s" % flag
