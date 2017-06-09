import re

f = open('f:/flag11', 'rb')
strr = f.read()

pattern = re.compile(r"(?=FLAG{).*?(?=})", re.S)
match = pattern.search(strr)
tmp = match.group()
print tmp
