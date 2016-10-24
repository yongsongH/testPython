'''


Python xlwt 

'''
# encoding : utf-8 
import xlrd
import xlwt

workbook = xlwt.Workbook() 
sheet = workbook.add_sheet("Sheet 1") 

#创建工作簿（workbook）和工作表（sheet）

sheet.write(1, 0, 'Python')#行列对应

style = xlwt.easyxf('font: bold 1')
sheet.write(1, 1, 'style ', style)

workbook.save(r'C:\Users\hys mac\Desktop\mr.c\python1.xls')  
