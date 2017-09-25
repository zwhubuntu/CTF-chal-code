'''
package com.example.xman.easymobile;

public class key {
    private static byte[] b;

    static  {
        key.b = new byte[]{23, 22, 26, 26, 25, 25, 25, 26, 27, 28, 30, 30, 29, 30, 32, 32};
    }

    public key() {
        super();
    }

    public static boolean check(String str) {
        int length = 16;
        byte[] v1 = str.getBytes();
        byte[] v3 = new byte[length];
        int i;
        for(i = 0; i < length; ++i) {
            v3[i] = ((byte)((v1[i] + key.b[i]) % 61));
        }

        for(i = 0; i < length; ++i) {
            v3[i] = ((byte)(v3[i] * 2 - i));
        }

        return new String(v3).equals(str);
    }
}

'''
import string

lst = [23, 22, 26, 26, 25, 25, 25, 26, 27, 28, 30, 30, 29, 30, 32, 32]
tmp_flag = [0] * 16
v3 = [0] * 16
v4 = [0] * 16
chars = string.printable.strip()
flag = ''

for i in xrange(16):
    for j in chars:
        tmp_flag[i] = j
        v3[i] = (ord(tmp_flag[i]) + lst[i]) % 61
        try:
            v4[i] = chr(v3[i] * 2 - i)
            if v4[i] == tmp_flag[i]:
                print v3[i]
                flag += j
                break
        except:
            pass

print flag
