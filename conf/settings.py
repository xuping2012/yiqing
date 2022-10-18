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
MYSQL_HOST = '192.168.2.178'
MYSQL_PORT = 3306
MYSQL_DB_USER = 'root'
MYSQL_DB_PASSWORD = 'xxxx'
MYSQL_DB_NAME = 'xxxxdb'
