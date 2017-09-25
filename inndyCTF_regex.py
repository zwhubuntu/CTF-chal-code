import re

f = open('f:/flag11', 'rb')
strr = f.read()

# pat = "FLAG{[^}]*}"
pat = "FLAG{[^()\[\]{}@]+}"  # correct answer
flag_group = re.findall(pat, strr)
print flag_group
