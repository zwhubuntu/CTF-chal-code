'''


@author: wenhuizone
'''
import ContinuedFractions, Arithmetic
import sys
sys.setrecursionlimit(1000000000)
def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d
if __name__ == "__main__":
    
    e = 0x045C7D653BBE3BD1B740D1F1FAD2909A925A7672EB5A8F5807909CCEF5E230CA53F150D78F0D68EC98F393AB7D086740BDBA499A40479988FF947CE1FFC2B63B1490EFFC3E545FA5CE4091DB84034E1FB6E8CF55F8E273BB2E0D848EC664CF349E5DAF2DEBA97BC88E16DDA2164384B5A8A3708E6E7A8A7581593BC79196435BB5
    n = 0x06234AC7DB9721ED90267DB30EBDFC512165CF5FD24E3C2DDEA2DCF0D105E3B1B5264973CC28F159A33CB8ED1EB8EFB2A3702EED88B9D6FCCC102276C412A62953D26E2EC93574C9644211E99394B9847FD69BBCA1520F2BF357CCC85DC463268ED76E4450A94B68F6B0BD645F2749E24F634D3F19D98C4C7A8A754FC154724945
    d = hack_RSA(e,n)
    print d