import os
from openai import OpenAI

client=OpenAI(
    api_key=os.environ['DEEPSEEK_API_KEY'],
    base_url='https://api.deepseek.com'
)

response=client.chat.completions.create(
    model='deepseek-v4-flash',
    messages=[
        {'role':'system','content':'你是一个python编程专家，并且话比较多.'},
        {'role':'assistant','content':'好的，我是一个编程专家，你可以问我问题了.'},
        {'role':'user','content':'你好，给我写一个输出打印Hello World的程序代码'}
    ],
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(f'{chunk.choices[0].delta.content}',end='',flush=True)