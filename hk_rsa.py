'''

@author: wenhuizone
'''
import rsa

n = 74207624142945242263057035287110983967646020057307828709587969646701361764263
e = 65537
PUBKEY = rsa.PublicKey(n, e)
PRIVKEY = rsa.PrivateKey(74207624142945242263057035287110983967646020057307828709587969646701361764263, 65537, 23071769375111040425287244625328797615295772814180109366784249976498215494337, 258631601377848992211685134376492365269, 286924040788547268861394901519826758027)

def decrypt(x,privkey):
    return rsa.decrypt(x,privkey)

def encrypt(s, pubkey):
    return rsa.encrypt( s, pubkey )

if __name__ == '__main__':
    with open('d:/flagg.txt', 'r') as fp:
        flag = fp.read()
    print flag    
    
    with open('d:/flag.enc', 'w') as fp:
        fp.write( decrypt(flag, PRIVKEY) )