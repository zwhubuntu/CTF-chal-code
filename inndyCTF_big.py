import re

pat = "FLAG{[^()\[\]{}@]+}"

with open('C:\\Users\\wenhuizone\\Desktop\\big\\big\\big', 'rb') as f:
    for line in f:
        flag_group = re.findall(pat, line)
        if flag_group != []:
            print flag_group
