from app.models.calculator import Calculator
class CalculatorService(object):
    def __init__(self) -> None:
        # self.calculator=Calculator() #로컬변수, 전역변수
        pass
    
    def calculate(self,first,second):
        calculator=Calculator(first,second) #지역변수
        print(f'첫번째수:{calculator.first}')
        print(f'두번째수:{calculator.second}')
        print(f'{calculator.first}+{calculator.second}={calculator.sum()}')
        print(f'{calculator.first}-{calculator.second}={calculator.subtract()}')
        print(f'{calculator.first}*{calculator.second}={calculator.multiply()}')
        print(f'{calculator.first}/{calculator.second}={calculator.divide()}')