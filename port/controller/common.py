class common():
    #对比dict格式参数
    def cmp_dict(src_data, dst_data):#断言：src_data    resp：dst_data
        try:
            assert type(src_data) == type(dst_data), "type: '{}' != '{}'".format(type(src_data), type(dst_data))
            if isinstance(src_data, dict):
                try:
                    for key in src_data:
                        assert key in dst_data
                        return common.cmp_dict(src_data[key], dst_data[key])
                except AssertionError as err1:
                    return (str(err1))
            elif isinstance(src_data, list):
                for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
                    return common.cmp_dict(src_list, dst_list)
            else:
                assert src_data == dst_data, "value '{}' != '{}'".format(src_data, dst_data)
        except AssertionError as err:
            return (str(err))

if __name__ == "__main__":
    xx = {"111": "gjx"}
    yy = {"111": "bob", "23456": {"22222": 9999, "33333": "0000", "list": ["111", "3333", "4444"]}}
    test = common()
    common.cmp_dict(xx,yy)
