'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-11-12 22:24:24
@LastEditTime: 2019-11-12 22:51:16
@LastEditors: Please set LastEditors
'''
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from django.conf import settings
from fdfs_client.client import Fdfs_client


@deconstructible
class FastDFSStorage(Storage):

    def __init__(self, base_url=None, conf=None):
        if base_url is None:
            base_url = settings.FDFS_URL
        self.base_url = base_url
        if conf is None:
            conf = settings.FDFS_CLIENT_CONF
        self.client_conf = conf

    def _open(self, name, mode='rb'):
        """
        它将被 Storage.open() 调用，前者才是存储类用来打开文件的真正机制，
        这个方法必须要返回一个 文件 对象。
        :param name:
        :param mode:
        :return:
        """
        return open(name, mode)

    def _save(self, name, content):
        """
        被Storage.save()调用，name是传入的文件名，
        content是Django接收到的文件内容，该方法需要将content文件内容保存。
        Django会将该方法的返回值保存到数据库中对应的文件字段，
        也就是说该方法应该返回要保存在数据库中的文件名称信息
        :param name: 文件名
        :param content:  文件数据
        :return: 存储到数据库中的文件名
        """
        client = Fdfs_client(self.client_conf)
        ret = client.upload_by_buffer(content.read())
        if ret.get("Status") != "Upload successed.":
            raise Exception("upload file failed")
        file_name = ret.get("Remote file_id")
        return file_name

    def exists(self, name):
        """
        判断文件是否存在，FastDFS可以自行解决文件的重名问题
        所以此处返回False，告诉Django上传的都是新文件
        :param name:
        :return:
        """
        return False

    def url(self, name):
        """
        返回文件的完整URL路径
        :param name:
        :return:
        """
        return self.base_url + name
