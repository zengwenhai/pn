import unittest
import json
from base.method import Method, IsAssert
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from page.laGou import *
from utils.public import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson


class LaGou(unittest.TestCase):

    def setUp(self):
        self.obj = Method()
        self.p = IsAssert()
        self.excel = OperationExcel()
        self.operationJson = OperationJson()

    def tearDown(self):
        pass

    def statusCode(self, r):
        self.assertEqual(r.status_code, 200)
        # self.assertEqual(r.json()['code'], 0)

    def isContent(self, r, row):
        self.statusCode(r)
        self.assertTrue(self.p.isContent(row=row, str2=r.text))

    def test_laGou_001(self):
        r = self.obj.post(row=1, data=self.operationJson.getRequestsData(1))
        self.statusCode(r)
        print(r.text)
        self.isContent(r=r, row=1)
        self.excel.writeResult(1, 'pass')
        # self.assertTrue(self.p.isContent(1, str2=r.text))

    def test_laGou_002(self):
        """测试关键字职位搜索"""
        r = self.obj.post(row=1, data=setSo('性能测试工程师'))
        # self.statusCode(r)
        print(r.text)
        # self.assertTrue(self.p.isContent(1, str2=r.text))
        list1 = []
        for i in range(1, 15):
            positionId = r.json()['content']['positionResult']['result'][i]['positionId']
            list1.append(positionId)

        writePositionId(json.dumps(list1))
        print(list1)

    def test_laGou_003(self):
        """访问搜索到的每个职位的详细信息"""
        for i in range(14):
            print("item:%s" %(i))
            r = self.obj.get(url=getUrl()[i])
            self.assertTrue(self.p.isContent(row=2, str2=r.text))






if __name__ == "__main__":
    # report = r'C:\Users\Administrator\PycharmProjects\pn1\report' + '\\report.html'
    # f = open(report, 'wb')
    # runner = HTMLTestRunner(
    #     f, verbosity=2, title="test", description="测试"
    # )
    # runner.run(LaGou('test_laGou_001'))
    # f.close()
    unittest.main(verbosity=2)