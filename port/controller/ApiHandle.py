from port import app,db
from flask import request,jsonify
from port.controller.public import get_json
from port.model.Api import Api
@app.route('/addApi',methods=['POST'])
def addApi():
    try:
        data = request.get_data()
        data = get_json(data)
        api_name = data['apiName']
        case_id = data['caseId']
        parameter_type = data['parameterType']
        header = data['header']
        parameter_json = data['parameterJson']
        Apihandle = Api( api_name, parameter_type,case_id, header,parameter_json)
        db.session.add(Apihandle)
        db.session.commit()
        return jsonify("添加api成功")
    except Exception as e:
        print(e)
        return ("系统异常")
