import json

my_dict={
    "姓名":'周杰伦',
    'age':18,
    '性别':'男'
}

my_list=[1,'周杰伦',{'1':2,'content':'你好'}]


#json.dumps方法可以把字典/列表转成json，json.load则可以把json转成字典/列表
json_dict=json.dumps(my_dict,ensure_ascii=False)

json_list=json.dumps(my_list,ensure_ascii=False)

print(type(json_dict))

print(json_dict)

print(json_list)