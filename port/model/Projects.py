from port import db
from datetime import datetime
class Projects(db.Model):
    __tablename__ = 'b_projects'
    id = db.Column(db.Integer,primary_key=True,unique=True,)
    project_name = db.Column(db.String(255),index=True, nullable=False) #解决unique必填属性不好用的问题 unique=True,
    protocol_type = db.Column(db.String(32),index=True, nullable=False)
    create_person = db.Column(db.String(32),index=True, nullable=False)
    coded_system = db.Column(db.String(32),index=True, nullable=False)
    project_introduction = db.Column(db.String(700),nullable=False)
    chained_address = db.Column(db.String(255),index=True, nullable=False)
    port = db.Column(db.String(16),index=True, nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now,index=True, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.now().date(),index=True, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now().time(),index=True, nullable=False)

    def __init__(self,project_name,protocol_type,create_person,coded_system,project_introduction,chained_address,port,update_time,create_date,create_time):
        self.project_name  = project_name
        self.protocol_type = protocol_type
        self.create_person = create_person
        self.coded_system = coded_system
        self.project_introduction = project_introduction
        self.chained_address = chained_address
        self.port = port
        self.update_time=update_time
        self.create_date=create_date
        self.create_time = create_time
    def __repr__(self):
        return '<User %r>' % self.project_name
    def __json__(self):
        return ['id', 'project_name', 'protocol_type','create_person',
                'coded_system','project_introduction','chained_address','port','update_time',
                'create_date','create_time']