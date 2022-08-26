from icecream import ic
import pandas as pd

class PandasQuiz01(object):
    def __init__(self) -> None:
        pass
    def quiz1(self):
        df=pd.DataFrame.from_dict(
            {'1':[1,3,5],'2':[2,4,6]},orient='index',columns=['a','b','c'])
        ic(df)
        
        
        
    
    
'''
            Q1. 다음 결과 출력
                세로로 뽑으면 딕셔너리
                a  b  c 
        인  1  1  3  5          가로로 뽑으면 리스트
        덱  2  2  4  6
        스  ic| df1:    a  b  c
                        1  1  3  5
                        2  2  4  6
'''