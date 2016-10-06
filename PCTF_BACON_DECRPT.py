'''
Created on 2016-5-1

@author: wenhuizone
'''
intext = "VoiCIunESUpeRbereCeTtEcONconteepARunGrouPedArtistEsculinaiRedONTleBOnGoutetlESeNsdeLAcLasSenestlimIteEqUeparLEnombreDEcAlOriesqUilsPeUVEntIngurgiterCesvirtuosesdelafriteusevouspresentecepetitclippleindegoutsavoureux"
outtext = ""
for c in intext:
    if c.isupper():
            outtext += "B"
    else:
            outtext += "A"

print outtext