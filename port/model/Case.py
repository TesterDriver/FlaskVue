from port import db
from datetime import datetime
import time
# mysql 日期设置默认值必须使用timestamp类型
from sqlalchemy.sql.sqltypes import TIMESTAMP
# func用来生成数据库函数代码，跟踪进源代码看一***释就明白了
from sqlalchemy.sql import func
class Case(db.Model):
    #print(time.strftime("%Y-%m-%d", datetime.now().time()))
    __tablename__ = 'b_case'
    id = db.Column(db.Integer,primary_key=True,unique=True,)
    case_book = db.Column(db.String(10),index=True, nullable=False) #解决unique必填属性不好用的问题 unique=True,
    port_name = db.Column(db.String(16),index=True, nullable=False)
    case_name = db.Column(db.String(16),index=True, nullable=False)
    url = db.Column(db.String(100),index=True, nullable=False)
    method = db.Column(db.String(10),nullable=False)
    json_data = db.Column(db.String(700),index=True, nullable=False) #
    #create_time = db.Column(TIMESTAMP,default=func.now() ,index=True, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now, index=True, nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now,index=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now().date(),index=True, nullable=False)
    time = db.Column(db.DateTime, default=datetime.now().time(),index=True, nullable=False)
    del_flg = db.Column(db.String(5),default = 0,index=True, nullable=False)

    def __init__(self,case_book,port_name,case_name,url,method,json_data):#,create_time,del_flg
        self.case_book  = case_book
        self.port_name = port_name
        self.case_name = case_name
        self.url = url
        self.method = method
        self.json_data = json_data
        #self.create_time = create_time 时间的初始化可能导致数据库存值一直为0000 00：00：00
        #self.del_flg = del_flg
    def __repr__(self):
        return '<User %r>' % self.case_book
    def __json__(self):
        return ['id', 'case_book', 'port_name','case_name',
                'url','method','json_data','create_time',
                'update_time','date','time','del_flg']