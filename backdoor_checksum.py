'''
Created on 2016-2-13

@author: wenhuizone
'''
'''
function crc16($data)
{
  $crc = 0xFFFF;
  for ($i = 0; $i < strlen($data); $i++)
  {
    $x = (($crc >> 8) ^ ord($data[$i])) & 0xFF;
    $x ^= $x >> 4;
    $crc = (($crc << 8) ^ ($x << 12) ^ ($x << 5) ^ $x) & 0xFFFF;
  }
  return $crc;
}
'''
import itertools
def crc16(data):
    crc=0xFFFF
    for i in range(len(data)):
        x=((crc>>8)^ord(data[i]))&0xFF
        x^=x>>4
        crc=((crc<<8)^(x<<12)^(x<<5)^x)&0xFFFF
    return crc


#print crc16('admin')
chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
for t in itertools.product(chars, repeat=6):
    w = ''.join(t)
    if crc16(w)==43160:
        print "the admin is:"
        print w
        break