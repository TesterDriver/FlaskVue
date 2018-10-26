from port import db
class DataSource(db.Model):
    __tablename__ = 'b_data_source'
    id = db.Column(db.Integer,primary_key=True,unique=True,)
    data_source_name = db.Column(db.String(255),index=True, nullable=False)#数据源名称
    url = db.Column(db.String(16),index=True, nullable=False) #(数据库地址)解决unique必填属性不好用的问题 unique=True,
    user_name = db.Column(db.String(32))#数据库用户名
    pass_word = db.Column(db.String(700))#数据库密码
    database_type = db.Column(db.String(700)) #数据库类型
    def __init__(self,data_source_name,url,user_name,pass_word,database_type):
        self.data_source_name = data_source_name
        self.url  = url
        self.user_name = user_name
        self.pass_word = pass_word
        self.database_type = database_type
    def __repr__(self):
        return '<User %r>' % self.data_source_name
    def __json__(self):
        return ['id', 'data_source_name', 'url','user_name',
                'pass_word','database_type']