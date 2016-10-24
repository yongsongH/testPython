'''
Created on 2016-5-20

@author: hys mac
'''
# encoding : utf-8 
import xlrd
import xlwt

#excel_data = xlrd.open_workbook(文件路径')

excel_data = xlrd.open_workbook(r'C:\Users\hys mac\Desktop\实用的excel表格模板.xls')

#sheet = excel_data.sheets()[工作表序号]

sheet = excel_data.sheets()[0]

print(sheet.row_values(2)) #打印某一行数据


print(sheet.col_values(1))#打印某一列

print( )

print ( sheet.cell(6,1).value)#打印某个具体值



