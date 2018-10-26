from port import db
#from datetime import datetime
class Initialization(db.Model):
    __tablename__ = 'b_initialization'
    id = db.Column(db.Integer,primary_key=True,unique=True,)
    parent_id = db.Column(db.String(255),index=True, nullable=False)
    set_up = db.Column(db.String(700),index=True, nullable=False) #解决unique必填属性不好用的问题 unique=True,
    teardown = db.Column(db.String(700),index=True, nullable=False)
    def __init__(self,parent_id,set_up,teardown):
        self.parent_id = parent_id
        self.set_up  = set_up
        self.teardown = teardown
    def __repr__(self):
        return '<User %r>' % self.parent_id
    def __json__(self):
        return ['id', 'parent_id', 'set_up','teardown']