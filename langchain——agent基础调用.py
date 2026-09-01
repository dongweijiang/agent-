import os

from dotenv import load_dotenv

from langchain.agents import create_agent

from langchain.chat_models import init_chat_model

load_dotenv()

model_GLM=init_chat_model(
    base_url=os.getenv('GLM_BASE_URL'),
    model='glm-5.3-flash',
    api_key=os.getenv('GLM_API_KEY'),
    model_provider='openai'
)

agent=create_agent(model_GLM)

#agent.invoke()方法返回的是一个字典，字典里的"messages"键对应的值是一个列表，列表里的每个元素都是一个对象实例，对应有类属性的type和content，分别表示角色和内容

response=agent.invoke(
{
    'messages':
    [
        {
            'role':'system',
            'content':'你是一名资深的Python开发工程师，你说话很精炼，不喜欢说废话'
        },
        {
            'role':'user',
            'content':'介绍一下你自己'
        }
    ]
}
)

for msg in response["messages"]:
    
    print(f"角色:{msg.type}, 内容:{msg.content}")


#agent.stream()方法返回的是一个生成器对象,返回的是一个二元的生成器，第一个参数是片段，第二个是元数据，可以使用for循环来迭代获取模型的输出结果
#另外，agent.stream()方法在调用的时候应该传两个参数，第一个参数是一个字典，字典里有一个键"messages"，对应的值是一个列表，列表里的每个元素都是一个对象实例，对应有类属性的type和content，分别表示角色和内容；第二个参数是stream_mode，表示流式模式

"""
response=agent.stream(
{    
    'messages':
    [
        {
            'role':'system',
            'content':'你是一名资深的Python开发工程师，你说话很精炼，不喜欢说废话'
        },
        {
            'role':'user',
            'content':'介绍一下你自己'
        }
    ]
},
    stream_mode='messages'
)

for chunk, metadata in response:
    if chunk.content:
        print(f"{chunk.content}",end='',flush=True)

"""
