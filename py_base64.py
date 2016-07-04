'''


@author: wenhuizone

'''
import base64
string="R1pDVE1NWlhHUTNETU4yQ0dZWkRNTUpYR00zREtNWldHTTJES1JSV0dJM0RDTlpUR1kyVEdNWlRHSTJVTU5SUkdaQ1RNTkJWSVkzREVOUlJHNFpUTU5KVEdFWlRNTjJF"
print "\n 3rd problem \n"
count=0

try:
    while True:
        string=base64.decodestring(string)
        count=count+1
except:
    print "the count is %d \n",count
    print "the result is ",string