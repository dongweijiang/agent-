import os

from langchain.chat_models import init_chat_model

from dotenv import load_dotenv

load_dotenv()

model_GLM=init_chat_model(
    model='glm-5.3-flash',
    model_provider='openai',
    base_url=os.getenv('GLM_BASE_URL'),
    api_key=os.getenv('GLM_API_KEY')
)
#invoke()是阻塞时调用（非流式）

"""
response=model_GLM.invoke([
    {
        "role": "system",
        "content": "你是一名资深的Python开发工程师，你说话很精炼"
    },
    {
        "role": "user",
        "content": "介绍一下你自己"
    }
])

print(response.content)
"""

#response=model_GLM.invoke('你是谁？')      invoke()方法可以直接传入字符串，这个时候role默认是user

#stream()是流式调用（非阻塞时调用）

response=model_GLM.stream('你是谁？')      #stream()方法可以直接传入字符串，这个时候role默认是user

#stream()方法返回的是一个生成器对象，可以使用for循环来迭代获取模型的输出结果

for chunk in response:

    print(chunk.content,end='',flush=True)