import requests
import json
from port import app
from flask import request,jsonify
from port.controller.public import get_json
from port.model.Case import Case
from port.model.Cases import Cases
@app.route('/ask',methods=['POST','GET','PUT','DELETE'])
def ask():
    try:
        # data = request.get_data()
        # data = get_json(data)
        # caseBook = data['case_book']
        # portame = data['port_name']
        # case = Case.query.filter_by(case_book=caseBook, port_name=portame).first()
        # Method=case.method
        # json_data=case.json_data
        # Url=case.url
        data = request.get_data()
        data = get_json(data)
        Id = data['id']
        caseName = data['case_name']
        projectId = data['proect_id']
        case = Cases.query.filter_by(id=Id, case_name=caseName, proect_id=projectId).first()
        print(case.method)
        Method = case.method
        json_data = case.json_data
        Url = case.url
        if Method == 'POST':
            headers = {'content-type': 'application/json','x-userid':'1'}
            response = requests.post( Url ,data = json_data,headers=headers)
            if response.status_code == 200:
                text = json.loads(response.text)
                return jsonify(text)
            else:
                return ("返回异常，异常码:"+str(response.status_code)+str(response.text))
        elif Method == 'GET':
            response = requests.get(Url,params=json.loads(json_data))#数据库存储的json_data为字符串类型 需要转化一下
            print(response.status_code)
            if response.status_code == 200:
                text = json.loads(response.text)
                return jsonify(text)
            else:
                return ("返回异常，异常码:"+str(response.status_code))
        elif request.method == 'DELETE':
            url = 'http://127.0.0.1:5000/test'
            print("进入delete")
            response = requests.delete(url)
            if response.status_code == 200:
                return ('delete成功')
        elif request.method == 'PUT':
            url = 'http://127.0.0.1:5000/test'
            print("进入PUT")
            response = requests.put(url)
            if response.status_code == 200:
                return ('delete成功')
    except Exception as e:
        print(e)
        return jsonify("系统异常")