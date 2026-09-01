from langchain.chat_models import init_chat_model

from langchain_openai import ChatOpenAI

import os

from dotenv import load_dotenv

load_dotenv()

model=init_chat_model(model='deepseek-v4-flash',api_key=os.getenv('DEEPSEEK_API_KEY'),temperature=0.7,max_tokens=1024)


#对于init_chat_model方法不支持的模型，可以使用ChatOpenAI方法来初始化模型，也可以手动指定base_url和model_provider参数为‘openai’来初始化模型
model2=ChatOpenAI(
    model_name='glm-5.3-flash',
    api_key=os.getenv('GLM_API_KEY'),
    base_url=os.getenv('GLM_BASE_URL'),
)

model3=init_chat_model(model='glm-5.3-flash',
                       api_key=os.getenv('GLM_API_KEY'),
                       base_url=os.getenv('GLM_BASE_URL'),
                       model_provider='openai')

print(type(model))

print(type(model2))

print(type(model3))



