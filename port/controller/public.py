import json
#新增get_json的方法
def get_json(data):
    data = bytes.decode(data)
    results = json.loads(data)
    #results = json.dumps(data)
    return results
