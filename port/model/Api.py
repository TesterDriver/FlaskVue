from port import db
#from datetime import datetime
class Api(db.Model):
    __tablename__ = 'b_api'
    id = db.Column(db.Integer,primary_key=True,unique=True,)
    api_name = db.Column(db.String(255),index=True, nullable=False)#接口名称
    case_id = db.Column(db.String(16),index=True, nullable=False) #(案例集id)解决unique必填属性不好用的问题 unique=True,
    Parameter_type = db.Column(db.String(32),index=True, nullable=False)#参数类型
    header = db.Column(db.String(255),index=True, nullable=False)#头信息
    parameter_json = db.Column(db.String(700),index=True, nullable=False)#请求报文
    def __init__(self,api_name,case_id,Parameter_type,header,parameter_json):
        self.api_name = api_name
        self.case_id  = case_id
        self.Parameter_type = Parameter_type
        self.header = header
        self.parameter_json = parameter_json
    def __repr__(self):
        return '<User %r>' % self.case_name
    def __json__(self):
        return ['id', 'api_name', 'case_id','Parameter_type',
                'header','parameter_json']