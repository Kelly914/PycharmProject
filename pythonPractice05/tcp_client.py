# -*- coding:utf-8 -*-
'''
=============================================================
                                                           
    File:tcp_client.py                                         
    Time:2022/6/30 上午10:14                                    
    IDE:PyCharm                                     
    Project:day03_pm                                 
    environment:virtualenv                                   
                                                           
=============================================================   
                                                           
    Author:Barranzi                                         
    email:anweichao@yutianedu.com                           
    github:https://github.com/La0bALanG                     
    Barranzi's Blog:https://barranzi.com                    
    requirement:(Please describle your requirement here) -->
                                                           
=============================================================
'''

# Packages and Modules import statements
# --------------------------------------
from socket import *

# codings
# --------------------------------------

class TCP_Client(object):
    '''
    TCP客户端套接字对象
    '''

    def __init__(self):
        self.__sockfd = socket()

    @property
    def sockfd(self):
        return self.__sockfd

    def __connects(self):
        self.__sockfd.connect(('10.176.133.170',12120))

    def connects(self):
        self.__connects()

    def __SendAndRecv(self):

        while True:

            data = input('请输入您需要发送的内容>>>:')

            if not data:
                break

            self.__sockfd.send(data.encode())
            msg = self.__sockfd.recv(1024)
            print('从服务端接受到一条响应消息：{}'.format(msg.decode()))
        self.__sockfd.close()

    def SendAndRecv(self):
        self.__SendAndRecv()

def test():
    tcp_client = TCP_Client()
    tcp_client.connects()
    tcp_client.SendAndRecv()

# run test UseCase if current modules is main
if __name__ == '__main__':
    test()
