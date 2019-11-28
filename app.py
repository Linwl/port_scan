#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:linwl
@file: app.py.py
@time: 2019/11/28
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import socket
import datetime


def exTask(ip, port):
    TCP_sock = None
    try:
        TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        TCP_sock.settimeout(0.1)
        result = TCP_sock.connect_ex((ip, port))
        if result == 0:
            return '{0} port {1} is open!'.format(ip, port)
        else:
            pass
    except Exception as e:
        return "连接ip<{0}>异常:{1}".format(ip, e)
    finally:
        TCP_sock.close()


def start(ip: str):
    """
    开始
    :param ip:
    :return:
    """
    ports = []
    for i in range(65535):
        ports.append(i)
    print('开始扫描主机<{0}>上的<{1}>个端口'.format(ip, len(ports)))
    executor = ThreadPoolExecutor(max_workers=100)
    st = datetime.datetime.now()
    all_task = []
    for port in ports:
        all_task.append(executor.submit(exTask, ip, port))
    for future in as_completed(all_task):
        data = future.result()
        if data is not None:
            print(data)
    et = datetime.datetime.now()
    print("扫描主机<{0}>的端口已完成!".format(ip))
    print("总耗时{0}秒!".format((et - st).seconds))


if __name__ == '__main__':
    ip = "58.60.9.100"
    start(ip)
