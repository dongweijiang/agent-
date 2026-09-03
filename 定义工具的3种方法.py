from langchain_core.tools import tool

from pydantic import BaseModel,Field        #Field是用来给BaseModel中的值附加说明字段的

from typing import Literal      #定义枚举

#1、直接使用tool关键字来传参（不推荐）

@tool(name_or_callable='square_root',description='计算一个数的算术平方根')
def fun1(x:float)->float:
    return x**0.5

#2、定义函数的时候使用注释文档——工具名默认函数名，工具参数默认参数列表，工具作用描述默认文档注释,一般情况下最推荐
@tool
def get_weather(location:str,units:str='celsius',include_forecast:bool=False)->str:
    """
    用于获取当前城市的当前天气.
    Args:
        location:记录需要返回天气的地址
        units:记录温度的单位，分为华氏度和摄氏度，默认是摄氏度
        include_forecast:用于记录是否需要提供天气预报
    """
    temp=22 if units=='celsius' else 72

    result=f'当前{location}的温度是{temp} degree {units[0].upper()}'

    if include_forecast:

        result+='\n未来五天的天气是：晴朗'

    return result

#3、当传入的参数过多的时候，可以使用pydantic来定义一个类专门描述每个参数，最后在装饰器中传参即可。注意，这种方法只推荐在参数过多的时候使用.

class WeatherInput(BaseModel):
    location:str=Field(description='记录需要返回天气的地址')

    uints:Literal['celsius','fahrenheit']=Field(default='celsius',description='记录温度的单位，分为华氏度和摄氏度，默认是摄氏度')

    include_forecast:bool=Field(default=False,description='用于记录是否需要提供天气预报')

@tool(args_schema=WeatherInput)
def get_weather2(location:str,units:str='celsius',include_forecast:bool=False)->str:
    """
    获取当前location的天气
    """
    temp=22 if units=='celsius' else 72

    result=f'当前{location}的温度是{temp} degree {units[0].upper()}'

    if include_forecast:

        result+='\n未来五天的天气是：晴朗'

    return result