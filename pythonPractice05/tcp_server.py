# -*- coding:utf-8 -*-
'''
=============================================================
                                                           
    File:tcp_server.py                                         
    Time:2022/6/30 9:43                                    
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

class TCP_Server(object):
    '''
    创建TCP服务端编程模型
    '''

    def __init__(self):
        self.__sockfd = socket(AF_INET,SOCK_STREAM)

    @property
    def sockfd(self):
        return self.__sockfd

    def __prepare(self):
        '''
        绑定IP地址，设置监听队列
        :return:
        '''

        self.__sockfd.bind(('0.0.0.0',12120))
        self.__sockfd.listen(5)

    def prepare(self):
        self.__prepare()

    def __connects(self):

        while True:
            print('等待连接建立...')

            print()

            try:
                connfd,addr = self.__sockfd.accept()
            except Exception as e:
                print('连接建立失败！尝试重新建立连接')
                continue

            while True:

                data = connfd.recv(1024)

                if not data: # 判断接收的消息是否为空
                    break

                print('收到来自IP地址：{}的客户端发送来的一条数据：{}'.format(addr[0],data.decode()))

                n = connfd.send('receive your message!'.encode())
                print('本次向客户端发送了{}字节的数据！'.format(n))
            connfd.close()
        self.__sockfd.close()

    def connects(self):
        self.__connects()

def test():
    tcp_server = TCP_Server()
    tcp_server.prepare()
    tcp_server.connects()


# run test UseCase if current modules is main
if __name__ == '__main__':
    test()
