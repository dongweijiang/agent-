import os

from langchain.chat_models import init_chat_model

from dotenv import load_dotenv

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from langchain.agents import create_agent

from langchain.tools import tool

load_dotenv()

@tool
def get_weather(city:str)->str:
    """
    获取天气信息
    """
    return f"{city}的天气是晴天"

GLM_MODEL=init_chat_model(
    base_url=os.getenv("GLM_BASE_URL"),
    api_key=os.getenv("GLM_API_KEY"),
    model='glm-5.3-flash',
    model_provider="openai"
)

Agent=create_agent(model=GLM_MODEL,tools=[get_weather])


response=Agent.invoke(
    {
        'messages':
        [
            SystemMessage('你是一个天气查询小助手，你叫做虎哥，家住东北，你很幽默，喜欢开玩笑'),
            HumanMessage(content='你好，呀虎哥'),
            AIMessage(content='你好呀，我是虎哥，我家里住东北那嘎达，你找我有啥事不儿？'),
            HumanMessage(content='哎呀，虎哥！幸会幸会，我老家是广东那边的，这不，最近流行什么北漂，我原本想去北京的，结果最后也到了咱吉林。话说今天咱这天气咋样啊？'),
        ]
    }
)

for message in response['messages']:
    message.pretty.print()

"""



#流式输出版本：

response=Agent.stream(
    {
        'messages':
        [
            SystemMessage('你是一个天气查询小助手，你叫做虎哥，家住东北，你很幽默，喜欢开玩笑'),
            HumanMessage(content='你好，呀虎哥'),
            AIMessage(content='你好呀，我是虎哥，我家里住东北那嘎达，你找我有啥事不儿？'),
            HumanMessage(content='哎呀，虎哥！幸会幸会，我老家是广东那边的，这不，最近流行什么北漂，我原本想去北京的，结果最后也到了咱吉林。话说今天咱这天气咋样啊？'),
        ]
    },
    stream_mode='messages'
)

for chunk,meta in response:
    if chunk.content:

        print(chunk.content,end='',flush=True)

        
   #流式输出别用pretty_print(),这个方法会导致每一段返回的片段的内容都带有美化效果，看起来效果就是每一段内容都换行了，导致输出的内容不连贯，建议使用print()方法来输出流式返回的内容
        chunk.pretty_print()
"""

