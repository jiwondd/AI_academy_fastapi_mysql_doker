import pandas as pd
from icecream import ic

class PandasQuiz02(object):
    def __init__(self) -> None:
        pass
    def quiz2(self):
        df2=pd.DataFrame.from_dict({'1':[1,2,3],'2':[4,5,6],'3':[7,8,9],'4':[10,11,12],
         },orient='index',columns=['A','B','C'])
        ic(df2)
        
'''         
    Q2. 다음 결과 출력
        A   B   C
    1   1   2   3
    2   4   5   6
    3   7   8   9
    4  10  11  12
    ic| df2:     A   B   C
                1   1   2   3
                2   4   5   6
                3   7   8   9
                4  10  11  12
    '''