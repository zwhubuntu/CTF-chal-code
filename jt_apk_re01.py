# coding:utf-8
'''
package ctf.bobbydylan;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;

public class M extends T {
    public M() {
        super();
    }

    public void check(String arg10) {
        String v0_1;
        int 15 = 15;
        int v6 = 7;
        int i = 0;
        int 5 = 5;
        if(arg10.length() == 16) {
            goto label_11;
        }

        throw new RuntimeException();
        try {
        label_11:
            v0_1 = this.getKey();
        }
        catch(Exception v0) {
            v0_1 = this.getKey();
            System.arraycopy(v0_1, 0, arg10, 5, 5);
        }

        int[] v2 = new int[16];
        v2[0] = 42;
        v2[12] = 14;
        v2[10] = v6;
        v2[14] = 15;
        v2[15] = 17;
        int v4 = 43;
        try {
            v2[1] = v4;
            v2[5] = 5;
            System.out.println();
        }
        catch(Exception v3) {
            v2[5] = 37;
            v2[1] = 85;
        }

        v2[6] = 15;
        v2[2] = 32;
        v2[3] = 23;
        v2[11] = 68;
        v2[4] = 85;
        v2[13] = 5;
        v2[9] = v6;
        v2[v6] = 8;
        v2[8] = 22;
        while(i < arg10.length()) {
            if((v2[i] & 255) != ((arg10.charAt(i) ^ v0_1.charAt(i % v0_1.length())) & 255)) {
                throw new RuntimeException();
            }

            ++i;
        }
    }

'''

import string

char = string.printable.strip()
# lst=[42,85,32,23,85,37,15,8,22,7,7,68,14,5,15,17]
lst = [42, 43, 32, 23, 85, 5, 15, 8, 22, 7, 7, 68, 14, 5, 15, 17]
strr = 'anylab'
flag = ''

for i in range(0, len(lst)):
    flag += chr(lst[i] ^ ord(strr[i % 6]) & 0xff)
print flag
