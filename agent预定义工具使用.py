from langchain_tavily import TavilySearch

from langchain.agents import create_agent

from langchain.chat_models import init_chat_model

import os

from dotenv import load_dotenv

from langchain_core.messages import HumanMessage

load_dotenv()

search_tool=TavilySearch(
    max_result=5,
    topic='general'
)

GLM_MODEL=init_chat_model(
    api_key=os.getenv('GLM_API_KEY'),
    base_url=os.getenv('GLM_BASE_URL'),
    model='glm-5.3-flash',
    model_provider='openai'
)
'''
一个test
res=search_tool.invoke('你知道鸡你太美是什么梗吗？')

for msg in res['results']:
    print(msg['content'])
'''

Agent=create_agent(model=GLM_MODEL,tools=[search_tool])

response=Agent.invoke(
    {
        'messages':HumanMessage(content='你知道白海豚是什么台风吗？')
    }
)

for msg in response['messages']:
    msg.pretty_print()