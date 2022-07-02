# -*- coding:utf-8 -*-
'''
=============================================================
                                                           
    File:udp_client.py                                         
    Time:2022/6/30 上午10:36                                    
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

class UDP_Client(object):

    def __init__(self):
        self.__sockfd = socket(AF_INET,SOCK_DGRAM)
        self.addr = ('10.176.133.170',12128)

    @property
    def sockfd(self):
        return self.__sockfd

    def SendAndRecvfrom(self):

        while True:
            data = input('请输入：')

            if not data:
                break

            self.__sockfd.sendto(data.encode(),self.addr)
            msg,addr = self.__sockfd.recvfrom(1024)
            print('收到服务器消息：{}'.format(msg))
        self.__sockfd.close()

def test():

    udp_client = UDP_Client()
    udp_client.SendAndRecvfrom()


# run test UseCase if current modules is main
if __name__ == '__main__':
    test()
