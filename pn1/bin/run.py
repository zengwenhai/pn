import unittest
from utils.operationExcel import OperationExcel
import os
import smtplib
from email.mime.text import MIMEText


class Runner(object):
    def __init__(self):
        self.excel = OperationExcel()

    def getSuite(self):
        """获取要执行的测试套件"""
        suite = unittest.TestLoader().discover(
            start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests'),
            pattern='test_*.py',
            top_level_dir=None
        )
        return suite

    def send_mail(self, to_user, sub, content):
        global send_mail
        global send_user

        send_mail = 'smtp.126.com'
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = send_user
        message['To'] = to_user
        server = smtplib.SMTP()
        server.connect(send_mail)
        server.login('', '')
        server.send(send_user, to_user, message.as_string())
        server.close()

    def main_run(self):
        """批量执行测试用例"""
        unittest.TextTestRunner().run(self.getSuite())


