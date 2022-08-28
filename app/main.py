import os
import string
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService
from app.services.user import UserService
from app.services.grade import GradeService
from app.services.score import ScoreService
from app.services.pandas_quiz import PandasQuiz01
from app.services.pandas02 import PandasQuiz02
from app.services.pandas03 import PandasQuiz03

def print_menu():
    print("0. 전체프로그램 종료")
    print("1. 계산기 프로그램")
    print("2. 로그인 프로그램")#입력받은 아이디와 비번 콘솔에 출력하기
    print("3. 성적표 프로그램1")
    print("4. 성적표 프로그램2")
    print("5. pandas quiz")
    print("6. pandas quiz2")
    print("7. pandas quiz3")
    menu=input('메뉴선택')
    return menu

def main(): #메소드
    
    while 1:
        menu=print_menu()
        if menu=='0':
            print('전체 프로그램을 종료합니다')
            break
        elif menu=='1':
            calculatorservice=CalculatorService()
            first=int(input('첫번째값:'))
            second=int(input('두번째값:'))
            calculatorservice.calculate(first,second)

        elif menu=='2':
            userservice=UserService()
            id=input('ID:')
            password=input('PASSWORD:')
            userservice.user(id,password)       

        elif menu=='3':
            gradeservice=GradeService()
            name=input('학생이름:')
            print('과목의 점수를 입력하세요')
            a,b,c=map(int,input().split())
            average=(a+b+c)/3
            if 90<=average:
                print('A')
            elif 80<=average:
                print('B')
            elif 70<=average:
                print('C')
            elif 60<=average:
                print('D')  
            elif 50<=average:
                print('E')
            else :
                print('F')  
            
        elif menu=='4':
            scoreservice=ScoreService()
            name=input('학생이름:')
            korean=int(input('국어점수'))
            eng=int(input('영어점수'))
            math=int(input('수학점수'))
            credit=scoreservice.get_grade(name,korean,eng,math)
            print(f'이름:{name},학점:{credit}')
            
        elif menu=='5':
            quiz=PandasQuiz01()
            while 1:
                quiz_number = input('퀴즈번호 선택. 종료는 0 : ')
                if quiz_number =='0':
                    break
                elif quiz_number=='1':
                    quiz.quiz1()
                    
        elif menu=='6':
            quiz2=PandasQuiz02()
            while 2:
                secon_quiz=input('퀴즈번호 선택. 종료는 0:')
                if secon_quiz == '0':
                    break
                elif secon_quiz=='1':
                    quiz2.quiz2()
                    
        elif menu=='7':
            quiz2=PandasQuiz03()
            while 2:
                secon_quiz=input('퀴즈번호 선택. 종료는 0:')
                if secon_quiz == '0':
                    break
                elif secon_quiz=='1':
                    quiz2.quiz3()
                
                    
            

if __name__ == '__main__' :
    main()
    

