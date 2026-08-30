import os

from openai import OpenAI
"""
1、获取客户端client对象（OpenAI的类对象）
2、调用模型
3、处理回复结果
"""

#1、获取客户端的client对象：(这里正常来讲要传一个APIKey，但是我的Key已经封装到环境变量里了)
client=OpenAI(
    api_key=os.environ['DEEPSEEK_API_KEY'],
    base_url='https://api.deepseek.com'
)

#2、调用模型
response=client.chat.completions.create(
    model='deepseek-v4-flash',
    messages=
    [
        {'role':'system','content':'你是一个python编程专家，不喜欢说废话.'},
        {'role':'assistant','content':'好的，我是一个编程专家，你可以问我问题了.'},
        { 'role':'user','content':'你好，给我写一个输出打印Hello World的程序代码'}
    ]
)

#3、处理结果
print(response.choices[0].message.content)