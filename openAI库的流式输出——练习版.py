import os

from openai import OpenAI

client=OpenAI(
    api_key=os.environ['DEEPSEEK_API_KEY'],
    base_url='https://api.deepseek.com'
)

response=client.chat.completions.create(
    model='deepseek-v4-flash',
    messages=[
        {'role':'system','content':'你是一个python语言高手，负责帮我写代码'},
        {'role':'assistant','content':'你好，有什么可以帮到你?'},
        {'role':'user','content':'帮我写一个python的代码，实现打印从1到5'}
    ],
    stream=True
)

#非流式版本：
#print(response.choices[0].messages.content)

for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content,end='',flush=True)

