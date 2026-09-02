import os

from dotenv import load_dotenv

from langchain_core.messages import HumanMessage

from langchain.chat_models import init_chat_model

from langchain.agents import create_agent

from base64_upload import upload_picture

load_dotenv()

GLM_MODEL=init_chat_model(
    base_url=os.getenv('GLM_BASE_URL'),
    api_key=os.getenv('GLM_API_KEY'),
    model='glm-5.3-flash',
    model_provider='openai'
)

Agent=create_agent(model=GLM_MODEL)

Web_Messages=HumanMessage(
    [
        {'type':'image','url':r'https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241022/emyrja/dog_and_girl.jpeg'},
        {'type':'text','text':'简要地给我介绍一下这张图片'}
    ]
)

image_base64=upload_picture(os.getenv('EXAMPLE_LOCAL_PICTURE_PATH'))

Local_Messages=HumanMessage(
    [
        {'type':'image','base64':image_base64,'mime_type':'image/png'},
        {'type':'text','text':'给我简单讲讲这一页PPT主要讲了什么内容'}
    ]
)



"""
#这里是流式输出网站图片的评价
Web_response=Agent.stream(
    {
        'messages':[Web_Messages]
    },
    stream_mode='messages'
)

for msg,meta in Web_response:
    if msg.content:
        print(f'{msg.content}',end='',flush=True)
"""

"""
#这里是非流式输出本地图片的评价
"""

Local_response=Agent.invoke(
    {
        'messages':[Local_Messages]
    }
)

for msg in Local_response['messages']:
    #使用pretty_print会把base64码一起打出来。可以采用下面的方法
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