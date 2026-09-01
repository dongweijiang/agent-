import os

from langchain.chat_models import init_chat_model

from langchain.tools import tool

from dotenv import load_dotenv

from langchain.agents import create_agent

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

GLM_MODEL=init_chat_model(
    base_url=os.getenv("GLM_BASE_URL"),
    api_key=os.getenv("GLM_API_KEY"),
    model='glm-5.3-flash',
    model_provider="openai"
)

@tool
def get_weather(city:str)->str:
    """
    获取天气信息
    """
    return f"{city}的天气是晴天"

Agent=create_agent(model=GLM_MODEL,tools=[get_weather])

response=Agent.invoke(
    {
        'messages':
        [
            SystemMessage(content='你是一个热心的AI助手，你叫做虎哥'),
            HumanMessage(content='你好呀虎哥'),
            AIMessage(content='你好呀，我是虎哥'),
            HumanMessage(content='今天北京的天气怎么样'),
        ]
    }
)

"""
这是直接从response里获取消息，response是一个字典，里面有一个key叫做messages，里面是一个列表，列表里是每一条消息的对象，每个对象都有type和content两个属性，以此来打印。这种打印会把ToolMessage也打印出来
for message in response['messages']:

    print(f"{message.type}: {message.content}")

"""

for message in response['messages']:
    message.pretty_print()  # 这种打印不会把ToolMessage打印出来,并且会先标注消息的类型，然后再打印消息的内容。不过会打印出调用了什么Tool
