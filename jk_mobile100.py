'''


@author: wenhuizone
'''
'''
    public boolean a() {
        boolean v1 = false;
        int v0 = 0;
        while(true) {
            if(v0 < this.a.length()) {
                int v2 = this.a.charAt(v0);
                if(v2 >= 97 && v2 <= 122) {
                    ++v0;
                    continue;
                }
            }
            else {
                break;
            }

            goto label_11;
        }

        v1 = true;
    label_11:
        return v1;
    }
'''
a=['h', 'J', 'C', 'a', '$', 'f', 'v', 'H', 'I', 'e', 'a', 'f', '_', 'N', 'O', 'F', 'Q', 'R', 'u', 'T', 'U', 'n', 'W', 'X', '_', 'Z', 'f', '$', 'c', 'd', '&', 'f', 'I', '_', '1', 'j', 'k', 'l', 'm', 'n', 'G', 'p', 'q', 'S', '0', 'T', 'u', 'v', 'F', 'S', 'y', 'z', 'Q', '1', '2', '3', '4', '5', '6', '7', 'R', '9', '+', '/']
out_put=''
result=''

for i in range(0,len(a),3):
    out_put+=a[i]
print out_put
'''
for j in out_put:
    if ord(j)>=97 and ord(j)<=122:
        result+=j
print result
'''