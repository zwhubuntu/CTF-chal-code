'''
Created on 2016-5-1

@author: wenhuizone
'''
intext = "woUldyouprEfeRSausaGesorbacoNwiTHYouREgG"
outtext = ""
for c in intext:
    if c.isupper():
            outtext += "B"
    else:
            outtext += "A"

print outtext