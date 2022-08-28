import numpy as np
import pandas as pd
import random
import string
from icecream import ic
    
def id(chr_size) -> str: return ''.join([random.choice(string.ascii_letters) for i in range(chr_size)])

def quiz32_df_grade(self) -> str:
    data = np.random.randint(0, 101, (10, 4))
    idx = [self.id(5) for i in range(10)]
    col = ['국어', '영어', '수학', '사회']

    df_list = pd.DataFrame(data, idx, col)
    ic(df_list)

    df_dict = pd.DataFrame.from_dict(dict(zip(idx, data)), orient='index', columns=col)
    ic(df_dict)
    return None