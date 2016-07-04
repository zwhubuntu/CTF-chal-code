''' 

@author: wenhuizone
'''
dmm='Jeopardy-style CTFs has a couple of questions (tasks) in range of categories. For example, Web, Forensic, Crypto, Binary or something else. Team can gain some points for every solved task. More points for more complicated tasks usually. The next task in chain can be opened only after some team solve previous task. Then the game time is over sum of points shows you a CTF winer. Famous example of such CTF is Defcon CTF quals.'
result=[];
for i in range(0,len(dmm)):
    if dmm[i]==' ':
        result.append(i)
print result
print len(result)