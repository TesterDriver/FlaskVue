# _*_ coding: utf-8 _*_

#调试模式是否开启
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
#session必须要设置key
SECRET_KEY='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#mysql数据库连接信息,这里改为自己的账号  mysql+pymysql兼容python3的写法  否则报错no mudule name MySql
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/dome1"