'''
Created on 2016-2-6

@author: wenhuizone
'''
import xlrd
data=xlrd.open_workbook('d:\data.xls')
table=data.sheets()[0]
list = [[0 for col in range(23)] for row in range(14747)]
for i in range(0,14747):
    list[i]=table.row_values(i)
for i in range(14747):
    for j in range(23):
        print chr(int((list[i][j]-78)/3))