import os

from dotenv import load_dotenv

from base64_upload import upload_picture

from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

from langchain.chat_models import init_chat_model

from langchain.agents import create_agent

load_dotenv()

GLM_MODEL=init_chat_model(
    base_url=os.getenv('GLM_BASE_URL'),
    api_key=os.getenv('GLM_API_KEY'),
    model='glm-5.3-flash',
    model_provider='openai'
)

Agent=create_agent(GLM_MODEL)

Web_Message=HumanMessage(
    [
        {'type':'image','url':os.getenv('EXAMPLE_WEB_PIECTURE_PATH')},
        {'type':'text','text':'给我描述一下这张照片'}
    ]
)

image_base64=upload_picture(os.getenv('EXAMPLE_LOCAL_PICTURE_PATH'))

Local_Message=HumanMessage(
    [
        {'type':'image','base64':image_base64,'mime_type':'image/png'},
        {'type':'text','text':'给我描述一下这张照片'}
    ]
)

for msg in Agent.invoke(
    {
        'messages':[Web_Message]
    }
)['messages']:
    if msg.__class__.__name__=='AIMessage':
        msg.pretty_print()

print('-'*23)

for local_msg,meta in Agent.stream(
    {
        'messages':[Local_Message]
    },
    stream_mode='messages'
):
    if msg.content:
        print(f'{local_msg.content}',end='',flush=True)
