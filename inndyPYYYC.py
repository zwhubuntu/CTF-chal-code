# 2017.06.19 06:58:45 PDT
# Embedded file name: pyyy.py
__import__('sys').setrecursionlimit(1048576)
data = 'Tt1PJbKTTP+nCqHvVwojv9K8AmPWx1q1UCC7yAxMRIpddAlH+oIHgTET7KHS1SIZshfo2DOu8dUt6wORBvNVBpUSsuHa0S78KG+SCQtB2lr4c1RPbMf0nR9SeSm1ptEY37y310SJMY28u6m4Y44qniGTi39ToHRTyxwsbHVuEjf480eeYAfSVvpWvS8Oy2bjvy0QMVEMSkyJ9p1QlGgyg3mUnNCpSb96VgCaUe4aFu4YbOnOV3HUgYcgXs7IcCELyUeUci7mN8HSvNc93sST6mKl5SDryngxuURkmqLB3azioL6MLWZTg69j6dflQIhr8RvOLNwRURYRKa1g7CKkmhN4RytXn4nyK2UM/SoR+ntja1scBJTUo0I31x1wBJpT4HjDN47FLQWIkRW+2wnB3eEwO5+uSiQpzA8VaH7VGRrlU/BFW4GqbaepzKPLdXQFBkNyBKzqzR/zA2GIrYbLIVScWJ19DqJCOyVLGeVIVXyzN1y327orYL2Ee3lRITnE3FouicRStaznIcw8xmxvukwVMRZIJ/vTu8Zc1WQIYEIFXMHozGuvzZgROZTyFihWNRCBBtoP9DJJALJb0pA1IKIb2zLh+pwGF40Y6y93D6weKejGPO+A0DBXH9vuLcCcCIvr/XPQhO3jLKCBN+h9unuJKW3dyWxyaVPdR2V+BTw10VXolo7yaTH1GbR4TiVSB308mBOMwfchwihEe7RdMXvmXgaGarKkJe0NLUCd8jwhYII+WymjxO/xOz/ppOvNfAyIQksW0sggRPQTlgXSZ7MIVA1h66sGNljJ833MoFzWof3azLabaz1OrAJFqYXBg/myDsy1tV6rULSQ82hVR/TNnSmBGvyEDJTrLSwHyj78NOrW4mUnlLGBnAgWfw6pW2lRK2jkNX9NM6DfLsRK8lwl85UP8CZSuNdcLmLwHTVMZGm/cNkZCtWRBlZqEggxGdIO44D+f4y6ysnAk5/QzEwjIuecxEOb0jyV6dFui8g0c3Oxlhzcli0X8ToJFyeQRv1N9nokYZ07tFlG6m18kCToKz1qiH1U7kljXa6SvdORur5dWYLQ//gwhwppe7JlNda/cEoh92h96wRZDv1dSK/f1vz+mUeUyUlFY0iMjfw5eBXWZppNZi3ZtJcq5kllM2ACVFcxQWI3azM3ArOcqjosoiPjNoDYgKh7w4k2Cd0kLYEHscz/njtJ1KEcwLtqs4nJ+gB2r4V9g03YgvY5E8JJtfJMKdaTedjtvEuif8FNlCK9DMnL1iLpWptJbdfO83Y7Y46XCqjZFBI5o9Qtb78nLhMEM5/YTaNOM/wE/oJl5HI/i1X6kW3PKCsVubRkOkc2xawl6NYdLETjLvmrGhhI'
a = 138429774382724799266162638867586769792748493609302140496533867008095173455879947894779596310639574974753192434052788523153034589364467968354251594963074151184337695885797721664543377136576728391441971163150867881230659356864392306243566560400813331657921013491282868612767612765572674016169587707802180184907L
b = 166973306488837616386657525560867472072892600582336170876582087259745204609621953127155704341986656998388476384268944991674622137321564169015892277394676111821625785660520124854949115848029992901570017003426516060587542151508457828993393269285811192061921777841414081024007246548176106270807755753959299347499L
c = 139406975904616010993781070968929386959137770161716276206009304788138064464003872600873092175794194742278065731836036319691820923110824297438873852431436552084682500678960815829913952504299121961851611486307770895268480972697776808108762998982519628673363727353417882436601914441385329576073198101416778820619L
d = 120247815040203971878156401336064195859617475109255488973983177090503841094270099798091750950310387020985631462241773194856928204176366565203099326711551950860726971729471331094591029476222036323301387584932169743858328653144427714133805588252752063520123349229781762269259290641902996030408389845608487018053L
e = 104267926052681232399022097693567945566792104266393042997592419084595590842792587289837162127972340402399483206179123720857893336658554734721858861632513815134558092263747423069663471743032485002524258053046479965386191422139115548526476836214275044776929064607168983831792995196973781849976905066967868513707L
F = (a,
     b,
     c,
     d,
     e)
m = 8804961678093749244362737710317041066205860704668932527558424153061050650933657852195829452594083176433024286784373401822915616916582813941258471733233011L
g = 67051725181167609293818569777421162357707866659797065037224862389521658445401L
z = []
for i, f in enumerate(F):
    n = pow(f, m, g)
    this_is = 'Y-Combinator'
    l = (lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args))))(
        lambda f: lambda x: (1 if x < 2 else f(x - 1) * x % n))(g % 27777)
    c = raw_input('Channenge #%d:' % i)
    if int(c) != l:
        print 'Wrong~'
        exit()
    z.append(l)

z.sort()
gg = '(flaSg\'7 \\h#GiQwt~66\x0csxCN]4sT{? Zx YCf6S>|~`\x0c$/}\'\r:4DjJFvm]([sP%FMY"@=YS;CQ7T#zx42#$S_j0\\Lu^N31=r\x0b\t\tjVhhb_KM$|6]\nl!:V\rx8P[0m ;ho_\rR(0/~9HgE8!ec*AsGd[e|2&h!}GLGt\'=$\x0cbKFMnbez-q\\`I~];@$y#bj9K0xmI2#8 sl^gBNL@fUL\x0b\\9Ohf]c>Vj/>rnWXgLP#<+4$BG@,\'n a_7C:-}f(WO8Y\x0c2|(nTP!\'\\>^\'}-7+AwBV!w7KUq4Qpg\tf.}Z7_!m+ypy=`3#\\=?9B4=?^}&\'~ Z@OH8\n0=6\x0b\tv\nl!G\'y4dQW5!~g~I*f"rz1{qQH{G9\x0c\'b\x0cp\x0bdu!2/\\@i4eG"If0A{-)N=6GMC<U5/ds\rG&z>P1\nsq=5>dFZUWtjv\tX~^?9?Irwx\\5A!32N\x0bcVkx!f)sVY Men\x0c\'ujN<"LJ\x0c5R4"\\\\XPVA\'m$~tj)Br}C}&kX2<|\np3XtaHB.P\'(E 4$dm!uDyC%u ["x[VYw=1aDJ (8V/a!J?`_r:n7J88!a25AZ]#,ab?{%e\x0b]wN_}*Q:mh>@]u\t&6:Z*Fmr?U`cOHbAf7s@&5~L ,\tQ18 -Hg q2nz%\x0ccUm=dz&h1(ozoZ)mrA=`HKo\n\'rXm}Z-l3]WgN\\NW<{o=)[V({7<N1.-A8S"=;3sderb\tOZ$K\r0o/5\x0bMc76EGCWJ3IQpr7!QhbgzX8uGe3<w-g\'/j\'\tM4|9l?i&tm_\n57X0B2rOpuB@H@%L_\r)&/q=LZa(%}""#if#Kq74xK?`jGFOn"8&^3Q-\r#]E$=!b^In0:$4VKPXP0UK=IK)Y\rstOT40=?DyHor8j7O\\r/~ncJ5];cCT)c?OS0EM5m#V(-%"Tu:!UsE],0Dp  s@HErS]J{%oH54B&(zE.(@5#2k\tJnNlnUEij\\.q/3HBpJNk*X(k5;DlqK\'\'fX\r}EBk_7\x0b:>8~\t+M@WJx.PO({/U}1}#TqjreG\nN{\rX>4EsJr0Pn\\Z\\aL/-U<<{,Q;j\tF=7f\')+wH:p{G=_.s\\t-\x0bI\x0c*y\t1P:Y|/2xE<uo]~$>5k]FW+>fR<QA"(Fj[LL(hzfQo#PJ;:*0kB~3]9uL[o.xue:VQ\t;9-Tu\tq|mzzhV_okP\t,d\rQ`]5Gf\x0c#gXB\x0cAH|)NI|K=KW-&p-<b"3e.rO\x0cuK=\x0c^\r+MuLxCJ`UKaD\x0bBH&n+YVajZ(U7pwWtto3T10VLHwSJ\rK\t}\'F$l1:b2Bd\na=#t0iq}#!{1_)w$}<Dp(borC\'\t?r6;,+k;a(Q3@B?RCWYEDrjZe![x=n_%S]rl{&fLr*mgCD;92/nNsaxKy/;\nr]sPK=`+YP>MmfB\n8O4/"}nE7r*=41f2\t37>K\'s$wpl;qS[`qzu\x0b\t\nuaU|b,C`4& dRN~]7DnuTb2FhNHV!#Z2Hho\x0b[%.{O\t$q0\x0ch_@?w@b8[I^{JL|O8]i8{p)A.w)14qK3JoyF%licZ~ga\rW[L:W\rtIvfWJjZUOvB\rS.Beav3!-@bw|PexJ Pcw1\ry6!63B}]J])6fak/3r]W\tMeXt[uc(1_U lys{a1X\r%)[wwP3rhgNW{*d~_E%Q2htCt5ha@l0^0=\x0bwT\ni4/V;_\nM1rb?w~Q)Dli4u\n`}1+D8"\t`@V~$9l$Uy**VnI (@Ga0<RxfmoNgJTtE-aLH\rE5fMy7rk$)V\rL2Fv/AivOa"\nuX|70Xrw^D]%i%JyT\x0cc%cwZ/Wbp=IiY;/@nFEe>3=tM;K*`fReGoc5V/Ri?nXZ-RW)\'\t<\x0cV>@X@-Ei4%sO%},B_pjc`s"@oKCmdgDhjUZT@?mb\'?Q:F\x0bLJkPgjaFAc=rbrjAz$Zz\x0cq0GU!")xFOEF(x!3M\t:l83|}}HgGJJ#eT/I\x0b[|lK_n+;Wi/N^B4LzL.a(gVWq,zO6\'S|tb>RX` ca*CO<w\x0ci =wc1,M~\x0bc`FYEs\r){+Ll8[I9-88m\t\\iK/\\hno-C[vX*3Hx:%:K\rt\x0cW!tj\'SOhqxP|k7cw Hm?I@?P\'HmapG7$0#T(Auz]sjmd#\rFP/}53@-Kvmi(d%dZKLZ2LK\'e_E\x0bQmR 5/(irq4-EUyp<hB?[\tnU:p*xuzASM'
print ''.join((gg[(lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args))))(
    lambda f: lambda n: (1 if n < 3 else f(n - 1) + f(n - 2)))(i + 2)] for i in range(16))) % ''.join(
    (data[pow((__import__('fractions').gcd(z[i % 5], z[(i + 1) % 5]) * 2 + 1) * g, F[i % 5] * (i * 2 + 1), len(data))]
     for i in range(32)))

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.06.19 06:58:45 PDT
