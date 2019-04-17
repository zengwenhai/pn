import os

def data_dir(data='data', filename=None):
    """
    查找文件路径
    :param data: 文件夹名称
    :param filename: 文件名
    :return:
    """
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), data, filename)

print(data_dir('data', 'data.xls'))