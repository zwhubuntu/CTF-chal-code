'''

@author: wenhuizone
'''
output=''
dic='d:/joker_year_dic.txt'
month_str=''
day_str=''
for year in range(1950,2050):
    for month in range(1,13):
        for day in range(1,32):
            filename=open(dic,'a')
            if day in range(1,10):
                day_str='0'+str(day)
            else:
                day_str=str(day)
            if month in range(1,10): 
                month_str='0'+str(month)
            else:
                month_str=str(month)
            output="joker"+str(year)+month_str+day_str+'\n'
            filename.write(output)
            filename.close()
            
            