# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
#import SQLAlchemy
#import pymysql


#创建项目对象
app = Flask(__name__)
# -*- coding: utf-8 -*-


app = Flask(__name__)
CORS(app)
#import  os
#print (os.environ.keys())
#print (os.environ.get('FLASKR_SETTINGS'))
#加载配置文件内容
app.config.from_object('port.setting')     #模块下的setting文件名，不用加py后缀
app.config.from_envvar('FLASKR_SETTINGS')   #环境变量，指向配置文件setting的路径

#创建数据库对象
db = SQLAlchemy(app)

from port.model import User,Category,Case,Projects,Cases,Api,Initialization,DataSource,Assertion

from port.controller import login
from port.controller import request
from port.controller import CaseHandle
from port.controller import ApiHandle
# json encoding 用于数据库取值转换成json格式的方法
from port.controller.AlchemyEncoder import AlchemyEncoder as AlchemyEncoder
app.json_encoder = AlchemyEncoder