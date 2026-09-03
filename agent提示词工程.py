"""
# 身份
- 你是一个科幻作家，根据用户的要求创建一个太空之都。

# 指令
- 请务必以JSON格式输出，不要加任何markdown样式。

# 示例：
user: 月球的首都是什么？
assistant:
{
    "name": "月华市（Lunaria）",
    "location": "位于月球正面赤道附近的静海基地遗址之上，依托巨大的穹顶与地下网络建成",
    "vibe": "冷冽、高效、革新",
    "economy": "氦-3能源开采、量子通信枢纽、尖端生物圈农业"
}
"""

import os

from dotenv import load_dotenv

from base64_upload import upload_picture

from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

from langchain.chat_models import init_chat_model

from langchain.agents import create_agent

import json

from pydantic import BaseModel

load_dotenv()

GLM_MODEL=init_chat_model(
    base_url=os.getenv('GLM_BASE_URL'),
    api_key=os.getenv('GLM_API_KEY'),
    model='glm-5.3-flash',
    model_provider='openai'
)
#通过定义回复的格式实现格式控制

class CapitalInfo(BaseModel):
    name:str

    location:str

    vibe:str

    economy:str

    def __str__(self):
        return f'名字是{self.name},地址在{self.location},特点是{self.vibe},经济是{self.economy}.'

Agent=create_agent(
    model=GLM_MODEL,
    system_prompt='你是一个科幻作家，根据用户的要求创建一个太空之都。',
    response_format=CapitalInfo
)

response=Agent.invoke(
    {
        'messages':[
            HumanMessage(content='月球的首都是什么？'),
            AIMessage(content="""{
            "name": "月华市（Lunaria）",
            "location": "位于月球正面赤道附近的静海基地遗址之上，依托巨大的穹顶与地下网络建成",
            "vibe": "冷冽、高效、革新",
            "economy": "氦-3能源开采、量子通信枢纽、尖端生物圈农业"
            }"""),
            HumanMessage(content='金星的首都是什么？')
        ]
    }
)

Lunar_Info=response['structured_response']

print(Lunar_Info)



#这是通过提示词提示来获取信息
'''
Agent=create_agent(GLM_MODEL,system_prompt='你是一个科幻作家，根据用户的要求创建一个太空之都。请务必以JSON格式输出，不要加任何markdown样式。')

response=Agent.invoke(
    {
        'messages':[
            HumanMessage(content='月球的首都是什么？'),
            AIMessage(content="""{
            "name": "月华市（Lunaria）",
            "location": "位于月球正面赤道附近的静海基地遗址之上，依托巨大的穹顶与地下网络建成",
            "vibe": "冷冽、高效、革新",
            "economy": "氦-3能源开采、量子通信枢纽、尖端生物圈农业"
            }"""),
            HumanMessage(content='金星的首都是什么？')
        ]
    }
)


json_response=response['messages'][-1].content

print(type(json_response))

print('-'*23)

my_response=json.loads(json_response)

print(type(my_response))

print('-'*23)

for k,v in my_response.items():
    print(f'{k}:{v}')
'''
