from port import db
class User(db.Model):
    __tablename__ = 'b_user'
    id = db.Column(db.Integer,primary_key=True )
    username = db.Column(db.String(10),unique=True,index=True, nullable=False) #解决unique必填属性不好用的问题
    password = db.Column(db.String(16))

    def __init__(self,username,password):
        self.username  = username
        self.password = password
    def __repr__(self):
        return '<User %r>' % self.username
    def __json__(self):
        return ['id', 'username', 'password']
























#from sqlalchemy.orm import class_mapper
    # def to_json(self):
    #     return {
    #         'id': self.id,
    #         'username': self.username,
    #         'password': self.password,
    #     }
    # def as_dict(obj):
    #     # return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    #     # 上面的有缺陷，表字段和属性不一致会有问题
    #     return dict((col.name, getattr(obj, col.name))
    #                 for col in class_mapper(obj.__class__).mapped_table.c)