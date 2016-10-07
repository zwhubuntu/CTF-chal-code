'''
  for ( i = 0; i < 17; ++i )
  {
    if ( v27[i] != byte_415768[*(&v4 + i)] )
      v3 = 1;
  }
'''

lst = [1, 4, 14, 10, 5, 36, 23, 42, 13, 19, 28, 13, 27, 39, 48, 41, 42, 26, 20, 59, 4, 0, 0]
target = "swfxc{gdv}fwfctslydRddoepsckaNDMSRITPNsmr1_=2cdsef66246087138"
bottom=[49, 48, 50, 52, 125]
flag_bottom=''
flag=''

for i in xrange(17):
    flag += target[lst[i]]
for j in xrange(len(bottom)):
    flag_bottom += chr(bottom[j])

print "flag is %s" %(flag + flag_bottom)
