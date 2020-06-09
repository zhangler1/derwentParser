import re

def judgeBeToJiangSU(judgeob:str)->bool:
    pattern=re.compile(r"jiangsu|Nanjing|Nanking|Wuxi|Xuzhou|Hsuchow|Changzhou|Suzhou|Soochow|Nantong|Lianyungang|Huai'an|Yancheng|Yangzhou|Yangchow|Zhenjiang|Taizhou|Suqian|univ Southeast",flags=re.I)
    if re.search(pattern,judgeob):
        return True
    else:
        return False

