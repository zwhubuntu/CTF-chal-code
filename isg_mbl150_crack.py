'''

@author: wenhuizone
'''
a="VFT}E7gy4yfE7tuG6{"
'''
public static String encrypt(String s) {
        char v0_1;
        String v1 = "";
        int v2;
        for(v2 = 0; v2 < s.length(); ++v2) {
            int v0 = s.charAt(v2);
            if(v0 < 97 || v0 > 109) {
                if(v0 >= 65 && v0 <= 77) {
                    v0_1 = ((char)(v0 + 13));
                    goto label_12;
                }

                if(v0 >= 110 && v0 <= 122) {
                    v0_1 = ((char)(v0 - 13));
                    goto label_12;
                }

                if(v0 >= 78 && v0 <= 90) {
                    v0_1 = ((char)(v0 - 13));
                    goto label_12;
                }

                if(v0 >= 48 && v0 <= 57) {
                    v0_1 = ((char)(v0 ^ 7));
                    goto label_12;
                }

                v0_1 = ((char)(v0 ^ 6));
            }
            else {
                v0_1 = ((char)(v0 + 13));
            }

        label_12:
            v1 = String.valueOf(v1) + v0_1;
        }

        return v1;
    }
}
'''

a="VFT}E7gy4yfE7tuG6{"
output=''
tmp=''
tmp_c=''

for i in range(0,len(a)):
    tmp_c=a[i]
    if (ord(tmp_c)<97) or (ord(tmp_c)>109):
        if(ord(tmp_c)>= 65 and ord(tmp_c) <= 77):
            tmp=chr(ord(tmp_c)+13)
        elif(ord(tmp_c)>= 110 and ord(tmp_c) <= 122):
            tmp=chr(ord(tmp_c)-13)
        elif(ord(tmp_c)>= 78 and ord(tmp_c) <= 90):
            tmp=chr(ord(tmp_c)-13)
        elif(ord(tmp_c)>= 48 and ord(tmp_c) <= 57):
            tmp=chr(ord(tmp_c)^7)
        else:
            tmp=chr(ord(tmp_c)^6)
    else:
        tmp=chr(ord(tmp_c)+13)
    output+=tmp
print output
    
    