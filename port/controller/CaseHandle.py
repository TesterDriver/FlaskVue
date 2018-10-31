from port import app,db
from flask import request,jsonify
from port.controller.public import get_json
from port.model.Cases import Cases
@app.route('/addCase',methods=['POST'])
def addCase():
    try:
        data = request.get_data()
        data = get_json(data)
        case_name = data['caseName']
        project_id = data['projectId']
        url = data['url']
        method = data['method']
        Casehandle = Cases( case_name, project_id, url,method)#,create_time='',del_flg=''
        db.session.add(Casehandle)
        db.session.commit()
        return jsonify("添加案例成功")
    except Exception as e:
        print(e)
        return ("系统异常")
@app.route('/deleteCase', methods=['POST'])
def deleteCase():
    data = request.get_data()
    data = get_json(data)
    case_name = data['caseName']
    id = data['id']
    try:
        Casehandle = Cases.query.filter(Cases.id == id,Cases.case_name == case_name).first()
        print(Casehandle.method)
        Casehandle.del_flg= 1
        db.session.commit()
        return ("删除成功")
    except Exception as e:
        print(e)
        return ("系统异常")


@app.route('/updateCase', methods=['POST'])
def updateCase():
    try:
        data = request.get_data()
        data = get_json(data)
        id = data['id']
        case_name = data['caseName']
        project_id = data['projectId']
        url = data['url']
        method = data['method']
        Casehandle = Cases.query.filter(Cases.id ==id).first()
        Casehandle.case_name = case_name
        Casehandle.project_id = project_id
        Casehandle.url = url
        Casehandle.method = method
        db.session.commit()
        return ("修改成功")
    except Exception as e:
        print(e)
        return ("系统异常")
@app.route('/queryCase', methods=['POST'])
def queryCase():
    try:
        Casehandle = Cases.query.filter(Cases.del_flg=='0').all() #Case.del_fl代表未删除
        return jsonify(Casehandle)
    except Exception as e:
        print(e)
        return ("系统异常")