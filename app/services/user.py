from app.models.user import User
class UserService(object):
    def __init__(self) -> None:
        # self.calculator=Calculator() #로컬변수, 전역변수
        pass
    
    def user(self,id,password):
        user=User(id,password) #지역변수
        print(f'ID:{user.id}')
        print(f'PASSWORD:{user.password}')