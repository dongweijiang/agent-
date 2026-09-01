"""
所谓的余弦相似度算法其实就是计算两个向量的夹角的余弦值，余弦越接近1，说明两个向量越相似。余弦相似度的计算公式为：
cos(θ) = (A·B) / (||A|| * ||B||
"""

import numpy as np

def dot_cal(vec_a:list,vec_b:list)->float:
    """
    计算两个向量的点积
    :param vec_a: 向量A
    :param vec_b: 向量B
    :return: 点积结果
    """
    sum=0
    for a,b in zip(vec_a,vec_b):
        sum+=a*b
    return sum

def norm_cal(vec:list)->float:
    """
    计算向量的模
    :param vec: 向量
    :return: 模结果
    """
    result_squar=0
    for v in vec:
        result_squar+=v*v
    return np.sqrt(result_squar)

if __name__=="__main__":
    vec_a=[1,2,3]
    vec_b=[4,5,6]
    dot_result=dot_cal(vec_a,vec_b)
    norm_a=norm_cal(vec_a)
    norm_b=norm_cal(vec_b)
    cos_theta=dot_result/(norm_a*norm_b)
    print(f"向量A:{vec_a},向量B:{vec_b},点积结果:{dot_result},向量A模:{norm_a},向量B模:{norm_b},余弦相似度:{cos_theta}")