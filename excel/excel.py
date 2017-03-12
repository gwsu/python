import os,sys,string
import xlrd
import xlwt

# READ EXCEL
rfp = xlrd.open_workbook("readme.xls")

shts = rfp.sheets()

sht = shts[0]

cellval = sht.cell(0,0).value

print cellval

#WRITE EXCEL

wfp = xlwt.Workbook()


sheet=wfp.add_sheet('A Test sheet')
sheet.write(0,0,1234.5)


wfp.save('readmewr.xls')





