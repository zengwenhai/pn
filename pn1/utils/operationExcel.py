import xlrd
from xlutils.copy import copy
from utils.public import *
from utils.excel_data import *


class OperationExcel(object):

    def getExcel(self):
        """实例化excel表格，返回sheet对象"""
        db = xlrd.open_workbook(data_dir('data', 'data.xls'))
        sheet = db.sheet_by_name("Sheet1")
        return sheet

    def get_rows(self):
        """获取excel数据表的行数"""
        return self.getExcel().nrows

    def get_row_cel(self, row, col):
        """获取单元格的内容"""
        return self.getExcel().cell_value(row, col)

    def getUrl(self, row):
        """获取请求地址"""
        return self.get_row_cel(row, getUrl())

    def getCaseID(self, row):
        """获取测试ID"""
        return self.get_row_cel(row, getCaseID())

    def get_request_data(self, row):
        """获取请求参数"""
        return self.get_row_cel(row, get_request_data())

    def getExpect(self, row):
        """获取期望结果"""
        return self.get_row_cel(row, getExpect())

    def getResult(self, row):
        """获取实际结果"""
        return self.get_row_cel(row, getResult())

    def writeResult(self, row, content):
        """测试结果写到文件中"""
        col = getResult()
        work = xlrd.open_workbook(data_dir('data', 'data.xls'))
        old_content = copy(work)
        ws = old_content.get_sheet(0)
        ws.write(row, col, content)
        old_content.save(data_dir('data', 'api.xls'))

    def get_alls(self):
        """获取所有测试用例数"""
        return (self.get_rows() - 1)

    def get_success(self):
        """获取成功的用例数"""
        pass_count = []
        fail_count = None
        for i in range(1, self.get_alls()):
            if self.getResult(i) == 'pass':
                pass_count.append(i)
        return int(len(pass_count))


opera = OperationExcel()
print(opera.get_rows())
print(opera.get_row_cel(1, 3))
print(opera.getCaseID(1))
print(opera.getUrl(1))
print(opera.getExpect(1))
print("111",opera.get_success())