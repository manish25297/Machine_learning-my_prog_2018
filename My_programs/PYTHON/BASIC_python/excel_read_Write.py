import xlrd
import xlwt


book=xlrd.open_workbook("manish.xls")
sh=book.sheet_by_index(0)
print str(sh.cell(0,1,).value)





rb=xlwt.Workbook()
sheet=rb.add_sheet("1")
sheet.write(0,0,"roll")
sheet.write(0,1,"name")
rb.save("manish.xls")
