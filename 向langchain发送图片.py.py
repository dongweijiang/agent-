import os

from langchain.tools import tool

from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

from dotenv import load_dotenv

from langchain.agents import create_agent

from langchain.chat_models import init_chat_model

#这个upload_picture是自定义的函数
from base64_upload import upload_picture

load_dotenv()

DEEPSEEK_MODEL=init_chat_model(
    base_url=os.getenv('DEEPSEEK_BASE_URL'),
    api_key=os.getenv('DEEPSEEK_API_KEY'),
    model='deepseek-v4-flash-vision-exp',
    model_provider='openai'
)

GLM_MODEL=init_chat_model(
    base_url=os.getenv('GLM_BASE_URL'),
    api_key=os.getenv('GLM_API_KEY'),
    model='glm-5.3-flash',
    model_provider='openai'
)

Agent=create_agent(model=DEEPSEEK_MODEL)

"""
使用流式输出的方式解析网络图片

messages=HumanMessage(content=[
            {'type':'image',
            'url':'https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241022/emyrja/dog_and_girl.jpeg'},
            {'type':'text', 'text':'帮我分析一下这张图片'}
    ])


response=Agent.stream(
    {
        'messages':[messages]
    },
    stream_mode='messages'
)

for chunk,meta in response:
    if chunk.content:
        print(chunk.content,end='',flush=True)
"""

#一下是使用非流式方式解析本地图片
image_base64=upload_picture(r'C:\Users\35171\Pictures\Screenshots\屏幕截图 2025-11-30 233200.png')

messages=HumanMessage(
    content=[
        {'type':'image','base64':image_base64,'mime_type':'image/png'},
        {'type':'text','text':'给我讲讲这张PPT里的内容是什么，简要概括一下。'}
    ]
)

response=Agent.invoke(
    {
        'messages':[messages]
    },
)

for msg in response['messages']:
    #print(msg.content)     这里打印content由于传的时候把base64码一起传上去了，所以会把那一坨base64的码也打印出来 
    #print('-'*23)

   #使用pretty_print也会把base64码一起打出来。可以采用下面的方法
    msg.pretty_print()
    """
    只拿AI回复的方法:
    法1:
    if msg.__class__.__name__=='AIMessage':
        msg.pretty_print()

    法2:
    if msg.__class__.__name__=='AIMessage' and msg.content:
        print(msg.content)
    """