#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 22:59
# @Blog    : http://www.cnblogs.com/uncleyong
# @Gitee   : https://gitee.com/uncleyong
# @QQ交流群 : 652122175
# @公众号   : 全栈测试笔记

import os


# 获取项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 定义日志文件的路径
LOG_PATH = os.path.join(BASE_PATH,'log/log.txt')


# project env
HOST_INFO = {
	'dev':'http://127.0.0.1:5000',
	'test':'http://127.0.0.1:5000',
	'preProduct':'http://127.0.0.1:5000'
}


# mysql数据库的连接信息
MYSQL_HOST = '192.168.2.78'
MYSQL_PORT = 3306
MYSQL_DB_USER = 'root'
MYSQL_DB_PASSWORD = 'vagrant'
MYSQL_DB_NAME = 'covid'