from openai import OpenAI

import os

import json

client=OpenAI(
    base_url='https://api.deepseek.com',
    api_key=os.environ['DEEPSEEK_API_KEY']
)

schema = ['日期', '股票名称', '开盘价', '收盘价', '成交量']\

#拿到content:example['content']
examples_data = [       # 示例数据
    {
        "content": "2023-01-10，股市震荡。股票强大科技A股今日开盘价100人民币，一度飙升至105人民币，随后回落至98人民币，最终以102人民币收盘，成交量达到520000。",
        "answers": {
            "日期": "2023-01-10",
            "股票名称": "强大科技A股",
            "开盘价": "100人民币",
            "收盘价": "102人民币",
            "成交量": "520000"
        }
    },
    {
        "content": "2024-05-16，股市利好。股票英伟达美股今日开盘价105美元，一度飙升至109美元，随后回落至100美元，最终以116美元收盘，成交量达到3560000。",
        "answers": {
            "日期": "2024-05-16",
            "股票名称": "英伟达美股",
            "开盘价": "105美元",
            "收盘价": "116美元",
            "成交量": "3560000"
        }
    }
]
questions = [       # 提问问题
    "2025-06-16，股市利好。股票传智教育A股今日开盘价66人民币，一度飙升至70人民币，随后回落至65人民币，最终以68人民币收盘，成交量达到123000。",
    "2025-06-06，股市利好。股票黑马程序员A股今日开盘价200人民币，一度飙升至211人民币，随后回落至201人民币，最终以206人民币收盘。"
]


"""
[
    {"role": "system",      "content": f"你帮我完成信息抽取，我给你句子，你抽取{schema}信息，按JSON字符串输出，如果某些信息不存在，用'原文未提及'表示，请参考如下示例："},
    
    {"role": "user",        "content": "2023-01-10，股市震荡。股票强大科技A股今日开盘价100人民币，一度飙升至105人民币，随后回落至98人民币，最终以102人民币收盘，成交量达到520000。"},
    {"role": "assistant",   "content": '{"日期":"2023-01-10","股票名称":"强大科技A股","开盘价":"100人民币","收盘价":"102人民币","成交量":"520000"}'},
    {"role": "user",        "content": "2024-05-16，股市利好。股票英伟达美股今日开盘价105美元，一度飙升至109美元，随后回落至100美元，最终以116美元收盘，成交量达到3560000。"},
    {"role": "assistant",   "content": '{"日期":"2024-05-16","股票名称":"英伟达美股","开盘价":"105美元","收盘价":"116美元","成交量":"3560000"}'},
    
    {"role": "user",        "content": f"按照上述示例，现在抽取这个句子的信息：{要抽取的句子文本}"}]}
]
"""

my_list=[]

messages = [
    {"role": "system", "content": f"你帮我完成信息抽取，我给你句子，你抽取{schema}信息，按JSON字符串输出，如果某些信息不存在，用'原文未提及'表示，请参考如下示例："}
]

for example in examples_data:
    messages.append({'role':'user','content':example['content']})
    #先把example_data中的answer转化成json再发给ai
    messages.append({'role':'assistant','content':json.dumps(example['answers'],ensure_ascii=False)})

for question in questions:
    response=client.chat.completions.create(
        model='deepseek-v4-flash',
        messages=messages+[{'role':'user','content':f"按照上述示例，现在抽取这个句子的信息：{question}"}]
    )
    json_str=response.choices[0].message.content

    print(type(json_str))

    #将AI返回的json字符串转成python字典存进list中
    my_list.append(json.loads(json_str))

    #只是打印一下返回的json字符串。比起python字典的区别在于json打印出来是用双引号引起来的，而字典等则是单引号
    print(json_str)
    
    print('*'*23)

print('-'*23)

for dict in my_list:
    print(dict)
