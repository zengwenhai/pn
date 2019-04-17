from utils.public import *
import json
from utils.operationExcel import OperationExcel


class OperationJson(object):

    def __init__(self):
        self.excel = OperationExcel()

    def getReadJson(self):
        with open(data_dir(filename='requestData.json'), 'r', encoding='utf-8') as f:
            return json.load(f)

    def getRequestsData(self, row):
        """获取请求参数"""
        return json.dumps(self.getReadJson()[self.excel.get_request_data(row=row)])


# opera = OperationJson()
# print(opera.getRequestsData(2))