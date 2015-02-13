__author__ = 'Administrator'
import xlrd
#https://pypi.python.org/pypi/xlrd/0.9.3
import xlsxwriter
#https://pypi.python.org/pypi/XlsxWriter/0.6.6#downloads
from Base.OperateFile import base_file

class  base_excel:
    def __init__(self, file= 'c:/test.xls'):
        base_file(file).check_file()
        self.file = file
        self.data = xlrd.open_workbook(self.file)
        self.data.sheet_names()
        self.table = self.data.sheet_by_index(0)
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols

    def read_excel(self):
        #ncols = table.ncols
        colnames = self.table.row_values(0) #one rows data
        list = []
        for rownum in range(1, self.nrows):
            row = self.table.row_values(rownum)
            if row:
                app = {}
                for i in range(len(colnames)):
                    app[colnames[i]] = row[i]
                list.append(app)
        print(list)
        return list

    def write_excel(self):
        workbook = xlsxwriter.Workbook(self.file)
        worksheet = workbook.add_worksheet()

        top = workbook.add_format({'border':1,'align':'center','bg_color':'cccccc','font_size':13,'bold':True})
        green = workbook.add_format({'border':1,'align':'center','bg_color':'green','font_size':12})
        yellow = workbook.add_format({'border':1,'bg_color':'yellow','font_size':12})
        red = workbook.add_format({'border':1,'align':'center','bg_color':'red','font_size':12})
        blank = workbook.add_format({'border':1})
        for i in range(1, self.nrows):
            for j in range(0,self.ncols):
                cell_value = self.table.cell_value(i, j)
                if i == 0:
                    format = top
                elif i == 3 or i == 6:
                    format = blank
                else:
                    if j == 0 or j == 2:
                        format = yellow
                    elif j == 1:
                        format = red
                    elif j == 3:
                        format = green
                        #green.set_num_format('yyyy-mm-dd')  #setting time format
                worksheet.write(i, j, cell_value, format)
        workbook.close()

