# -*- coding:utf-8 -*-
'''
=============================================================
                                                           
    File:udp_server.py                                         
    Time:2022/6/30 10:29                                    
    IDE:PyCharm                                     
    Project:Big_Data_documents_and_codes                                 
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

class UDP_Server(object):

    def __init__(self):
        self.__sockfd = socket(AF_INET, SOCK_DGRAM)

    @property
    def sockfd(self):
        return self.__sockfd

    def __prepare(self):
        self.__sockfd.bind(('0.0.0.0',12128))

    def prepare(self):
        self.__prepare()

    def __connects(self):

        while True:

            print('等待连接...')
            print()

            data,addr = self.__sockfd.recvfrom(1024)

            if not data:
                break

            print('收到来自IP地址：{}的UDP客户端发来的一条无连接的消息：{}'.format(addr[0],data.decode()))
            n = self.__sockfd.sendto('收到消息'.encode(),addr)
            print('本次发送{}字节的消息'.format(n))
        self.__sockfd.close()

    def connects(self):
        self.__connects()

def test():

    udp_server = UDP_Server()
    udp_server.prepare()
    udp_server.connects()

# run test UseCase if current modules is main
if __name__ == '__main__':
    test()
