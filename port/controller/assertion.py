from port.model.Assertion import Assertion
from flask import json
from port.controller.common import common
class assertion():
     def __init__(self, response, parentId):
         """初始化参数属性"""
         self.response = response
         self.parentId = parentId
     def assertion(self):
         respinit = json.dumps(self.response)
         respinit = json.loads(respinit)
         assertion =Assertion.query.filter_by(parent_id=self.parentId).all()
         type =[]
         expectationJson1 = []
         expectationJson2 = []
         sql=[]
         operator = []
         try:
             for i in range(len(assertion)):
                 type.append(assertion[i].type)
                 if assertion[i].type == "INCLUDE":
                     expectationJson1.append(assertion[i].expectation_json)
                 else:
                     sql.append(assertion[i].sql)
                     operator.append(assertion[i].operator)
                     expectationJson2.append(assertion[i].expectation_json)
             exp1 = json.loads(expectationJson1[0])
         except IndexError as err:
             return ("无断言")
         if len(type):
             for i in range(len(type)):
                 if type[i] == "INCLUDE":
                     results = common.cmp_dict(exp1,json.loads(respinit))
                     if results==None:
                         print({"断言对比成功！":"0000"})
                         return ({"断言对比成功！":"0000"})
                     else:
                         print("断言结果对比失败："+results)
                         return ("断言结果对比失败："+results)
                 if type[i] == "SQL":
                     print("******")

if __name__ == "__main__":
    test = assertion({"111": "bob"},1)
    test.assertion()