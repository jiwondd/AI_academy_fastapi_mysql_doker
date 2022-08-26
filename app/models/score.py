class Score(object):
    def __init__(self,name,kor,eng,math):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        
    def input_name(self):
        return self.name
    def input_kor(self):
        return self.kor
    def input_eng(self):
        return self.eng
    def input_math(self):
        return self.math
    def set_avg(self):
        self.avg=(self.kor+self.eng+self.math)/3
    def get_avg(self):
        return self.avg
    
    