from port import app,db
from flask import request,jsonify
from port.controller.public import get_json
from port.model.Case import Case
import json
@app.route('/addCase',methods=['POST'])
def addCase():
    try:
        data = request.get_data()
        data = get_json(data)
        case_book = data['case_book']
        port_name = data['port_name']
        case_name = data['case_name']
        url = data['url']
        method = data['method']
        json_data = data['data']
        json_data = json.dumps(json_data)
        Casehandle = Case(case_book, port_name, case_name, url,method,json_data)#,create_time='',del_flg=''
        db.session.add(Casehandle)
        db.session.commit()
        return jsonify("添加成功")
    except Exception as e:
        print(e)
        return ("系统异常")
@app.route('/deleteCase', methods=['POST'])
def deleteCase():
    data = request.get_data()
    data = get_json(data)
    case_book = data['case_book']
    port_name = data['port_name']
    case_name = data['case_name']
    try:
        Casehandle = Case.query.filter(Case.case_book == case_book,Case.port_name == port_name,Case.case_name==case_name).first()
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
        case_book = data['case_book']
        port_name = data['port_name']
        case_name = data['case_name']
        url = data['url']
        method = data['method']
        json_data = data['data']
        json_data = json.dumps(json_data)
        Casehandle = Case.query.filter(Case.case_book ==case_book).first()
        Casehandle.case_book = case_book
        Casehandle.port_name = port_name
        Casehandle.case_name = case_name
        Casehandle.url = url
        Casehandle.method = method
        Casehandle.json_data = json_data
        db.session.commit()
        return ("修改成功")
    except Exception as e:
        print(e)
        return ("系统异常")
@app.route('/queryCase', methods=['POST'])
def queryCase():
    try:
        Casehandle = Case.query.filter(Case.del_flg=='0').all() #Case.del_fl代表未删除
        return jsonify(Casehandle)
    except Exception as e:
        print(e)
        return ("系统异常")