from utils.operationJson import OperationJson
from utils.operationExcel import OperationExcel
import json
from utils.public import *


operationExcel = OperationExcel()

def setSo(kd='自动化测试工程师'):
    """对搜索的数据重新赋值"""
    dici1 = json.loads(OperationJson().getRequestsData(1))
    print(dici1)
    dici1['kd'] = kd
    return dici1


def writePositionId(content):
    """把职位ID写入文件中"""
    with open(data_dir(filename='positionId'), 'w') as f:
        f.write(content)


def getPositionId():
    """获取职位招聘的信息"""
    with open(data_dir(filename='positionId'), 'r') as f:
        return json.loads(f.read())


# def setpositionInfo(row):
#     dict1 = json.loads(OperationJson().getRequestsData(row=2))
#     dict1['positionId'] = getPositionId()[0]
#     return dict1


def getUrl():
    listUrl = []
    for item in getPositionId():
        url='https://www.lagou.com/jobs/{0}.html'.format(item)
        listUrl.append(url)
    return listUrl


if __name__ == "__main__":
    # print(setSo('性能测试工程师'))
    # print(setpositionInfo(2))
    print(getUrl())