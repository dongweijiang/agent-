import os

from dotenv import load_dotenv

from base64_upload import upload_picture

from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

from langchain.chat_models import init_chat_model

from langchain.agents import create_agent

import threading

load_dotenv()

mutex=threading.Lock() #这里采用互斥锁的双线程方法实现Agent的一个程序的两次调用，保证不会后输出的覆盖先输出的

separator_print=threading.Event()

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
        {'type':'text','text':'给我讲解一下这张PPT'}
    ]
)

def run_invoke():

    mutex.acquire()

    for msg in Agent.invoke(
    {
        'messages':[Web_Message]
    }
    )['messages']:
        
        if msg.__class__.__name__=='AIMessage':

            msg.pretty_print()

    if not separator_print.is_set():

        print('='*28)
        print('下面打印本地图片的结果')
        print('='*28)

        separator_print.set()

    mutex.release()

def run_stream():

    mutex.acquire()

    for local_msg,meta in Agent.stream(
    {
        'messages':[Local_Message]
    },

    stream_mode='messages'
    ):
        if local_msg.content:

            print(f'{local_msg.content}',end='',flush=True)

        if not separator_print.is_set():

            print('='*28)
            print('下面打印网络图片的结果')
            print('='*28)

            separator_print.set()

    mutex.release()

if __name__=='__main__':
    t1=threading.Thread(target=run_invoke)

    t2=threading.Thread(target=run_stream)

    t1.start()

    t2.start()

    t1.join()

    t2.join()