from port.model.User import  User
from port.model.Category import Category
from port.controller.public import get_json
from port import app,db
from flask import request,jsonify

@app.route('/add',methods=['POST'])
def adduser():
     data = request.get_data()
     #data = get_json(data)
     print(data)
     # title = data['title']
     # content = data['text']
     # category = Category(title,content)
     # db.session.add(category)
     # db.session.commit()
     return (data)
@app.route('/update',methods=['POST'])
def update():
     result = Category.query.filter(Category.title == '测试2').first()
     result.content = 'conten11111'
     db.session.commit()
     return ("修改成功")
@app.route('/delete',methods=['GET','POST'])
def delete():
    result = Category.query.filter(Category.title == '测试2').first()
    db.session.delete(result)
    db.session.commit()
    print("调用删除成功")
    return ("删除成功")
@app.route('/test',methods=['GET','POST','DELETE','PUT'])
def test():
    data = request.get_data()
    print(data)
    #data = get_json(data)
    #print(data)
    return (jsonify({"age":"22"}))
#登陆模块
@app.route('/login',methods=['POST'])
def login():
     if request.method == 'POST':
         try:
            data = request.get_data()
            data = get_json(data)
            user_name = data['username']
            pass_word = data['password']
            user = User.query.filter_by(username=user_name,password=pass_word).first()
            if user.username==user_name and user.password == pass_word:
                return jsonify({"code":"0000","msg":"登陆成功"})
            elif user.username==user_name and user.password != pass_word:
                return ("密码不正确")
         except Exception as e:
             return jsonify({"code": "202", "msg": "用户不存在"})
#注册模块
@app.route('/register',methods=['POST'])
def register():
    if request.method == 'POST':
        try:
            data = request.get_data()
            data = get_json(data)
            user_name = data['username']
            pass_word = data['password']
            if(user_name=='' or pass_word==''):
                return jsonify({"code":"201","msg":"用户名或密码不能为空"})
            elif(User.query.filter_by(username=user_name).first()):
                return jsonify({"code":"202","msg":"当前用户已经注册"})
            else:
                reg = User(user_name, pass_word)
                db.session.add(reg)
                db.session.commit()
                user = User.query.filter_by(username=user_name, password=pass_word).first()
                if user.username == user_name and user.password == pass_word:
                    return jsonify({"code": "0000", "msg": "注册成功"})
                else:
                    return ("注册失败")
        except Exception as e:
            print(e)
            return jsonify({"code": "202", "msg": "系统异常"})