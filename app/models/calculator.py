class Calculator(object):
    def __init__(self, first, second):
        self.first=first
        self.second=second #속성
        #생성자
    
    def sum(self):   #메소드
        return self.first+self.second
    def subtract(self): 
        return self.first-self.second  
    def multiply(self): 
        return self.first*self.second 
    def divide(self): 
        return self.first/self.second   

