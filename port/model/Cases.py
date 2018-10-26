from port import db
class Cases(db.Model):
    __tablename__ = 'b_cases'
    id = db.Column(db.Integer,primary_key=True,unique=True,)
    case_name = db.Column(db.String(255),index=True, nullable=False) #(案例集名称)解决unique必填属性不好用的问题 unique=True,
    project_id = db.Column(db.String(32),index=True, nullable=False)#项目id
    url = db.Column(db.String(255),index=True, nullable=False)#接口地址
    method = db.Column(db.String(32),index=True, nullable=False)#接口方法

    def __init__(self,case_name,project_id,url,method):
        self.case_name  = case_name
        self.project_id = project_id
        self.url = url
        self.method = method
    def __repr__(self):
        return '<User %r>' % self.case_name
    def __json__(self):
        return ['id', 'case_name', 'project_id','url',
                'method']