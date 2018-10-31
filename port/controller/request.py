import requests
import json
from port import app
from flask import request,jsonify
from port.controller.public import get_json
from port.model.Cases import Cases
from port.model.Api import Api
from port.controller.assertion import  assertion
@app.route('/ask',methods=['POST','GET','PUT','DELETE'])
def ask():
    try:
        data = request.get_data()
        data = get_json(data)
        id = data['id']
        caseName = data['case_name']
        projectId = data['project_id']
        apiName = data['api_name']
        case = Cases.query.filter_by(id=id, case_name=caseName, project_id=projectId).first()
        caseId = case.id
        Method = case.method
        Url = case.url
        api = Api.query.filter_by(id=caseId, api_name=apiName).first()
        json_data = api.parameter_json
        header_data = api.header
        if Method == 'POST':
            response = requests.post( Url ,data = json_data,headers = json.loads(header_data))#,headers = json.loads(header_data)
            if response.status_code == 200:
                text = json.loads(response.text)#转换成dict类型
                results = assertion(response.text,id).assertion()
                if results == {"断言对比成功！":"0000"}:
                    return jsonify({"result": results,"response": text})
                elif results == "无断言":
                    return jsonify({"result": "无断言","response": text})
                else:
                    return jsonify({"result": results,"response": text})
            else:
                return ("返回异常\n异常码:"+str(response.status_code)+"\n返回内容\n"+str(response.text))
        elif Method == 'GET':
            response = requests.get(Url,params=json.loads(json_data))#数据库存储的json_data为字符串类型 需要转化一下
            if response.status_code == 200:
                text = json.loads(response.text)
                results = assertion(response.text, id).assertion()
                if results == {"断言对比成功！": "0000"}:
                    return jsonify({"result": results, "response": text})
                elif results == "无断言":
                    return jsonify({"result": "无断言", "response": text})
                else:
                    return jsonify({"result": results, "response": text})
            else:
                return ("返回异常，异常码:"+str(response.status_code))
    except Exception as e:
        print(e)
        return jsonify("系统异常")