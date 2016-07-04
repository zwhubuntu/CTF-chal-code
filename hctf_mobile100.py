'''
    public Classical(String input) {
        super();
        this.array1 = "0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z = A B C D E F G H I J K L M E O P Q R S T U V W X Y Z"
                ;
        this.array2 = "W,p,X,4,5,B,q,A,6,a,V,3,r,b,U,s,E,d,C,c,D,O,t,T,Y,v,9,Q,2,e,8,P,f,h,J,N,g,u,K,k,H,x,L,w,R,I,j,i,y,l,m,S,M,1,0,O,n,2,G,7,=,F,Z"
                ;
        this.input = input;
    }

    public String make() {
        new String[0];
        new String[0];
        String[] v1 = this.array1.split(" ");
        String[] v2 = this.array2.split(",");
        int v4 = this.input.length();
        int v3;
        for(v3 = 0; v3 < v4; ++v3) {
            String v0 = String.valueOf(this.input.charAt(v3));
            int v5;
            for(v5 = 0; v5 < 63; ++v5) {
                if(v0.equals(v1[v5])) {
                    if(v3 == 0) {
                        this.output = v2[v5];
                    }
                    else {
                        this.output = this.output + v2[v5];
                    }
                }
            }
        }

        return this.output;

@author: wenhuizone
'''
import base64
v1="0123456789abcdefghijklmnopqrstuvwxyz=ABCDEFGHIJKLMEOPQRSTUVWXYZ"
v2="WpX45BqA6aV3rbUsEdCcDOtTYv9Q2e8PfhJNguKkHxLwRIjiylmSM10On2G7=FZ"
target='SRlhb70YZHKvlTrNrt08F=DX3cdD3txmg'
result=''
result_r=''
tmp1=''
flag=''
'''
for i in range(0,len(target)):
    for j in range(65,127):
        tmp1=chr(j)
        #print tmp1
        for k in range(0,63):
            if tmp1==v1[k]:
                tmp1=v2[k]
        if tmp1==target[i]:
            #print tmp1
            result+=tmp1
print "the flag is:"
print result
'''
for i in range(0,len(target)):
    for j in range(0,63):
        if target[i]==v2[j]:
            tmp1=v1[j]
            result+=tmp1
print result
result_f=base64.b64decode(result)[::-1]
print result_f
flag=result_f.strip('hdu1s8')
print "the flag is:"
print flag[1::]
           
        