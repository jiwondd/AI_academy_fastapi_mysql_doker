import pandas as pd
from icecream import ic
import numpy as np

class PandasQuiz03(object):
    def __init__(self) -> None:
        pass
    def quiz3(self) -> None :
        df3 = pd.DataFrame.from_dict({'0':np.random.randint(10,100,size=3),
                                    '1':np.random.randint(10,100,size=3) },
                               orient='index',columns=['0','1','2'])
        ic(df3)  
        
'''
 Q3 두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic| df3:     0   1   2
                 0  95  25  74
                 1  44  24  97
'''