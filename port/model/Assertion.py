from port import db
class Assertion(db.Model):
    __tablename__ = 'b_assertion'
    id = db.Column(db.Integer,primary_key=True,unique=True,)
    assertion_name = db.Column(db.String(255),index=True, nullable=False)#断言名称
    parent_id = db.Column(db.String(16),index=True, nullable=False) #(api的id值)解决unique必填属性不好用的问题 unique=True,
    type = db.Column(db.String(32))#校验类型
    expectation_json = db.Column(db.String(700))#预期值
    operator = db.Column(db.String(700)) #运算符
    data_source_id = db.Column(db.String(8)) #数据源
    sql = db.Column(db.String(700)) #断言sql
    def __init__(self,assertion_name,parent_id,type,expectation_json,operator,data_source_id,sql):
        self.assertion_name = assertion_name
        self.parent_id  = parent_id
        self.type = type
        self.expectation_json = expectation_json
        self.operator = operator
        self.data_source_id = data_source_id
        self.sql = sql
    def __repr__(self):
        return '<User %r>' % self.assertion_name
    def __json__(self):
        return ['id', 'assertion_name', 'parent_id','type',
                'expectation_json','operator','data_source_id','sql']