
import re
from typing import Final

def CheckEmail(email: str) -> bool:
    regex: Final = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}([.]\w{2,3})?$'
    return re.search( regex, email )

def CheckPwd(pwd: str) -> bool:
    regex: Final = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    return re.search( regex, pwd )

def CheckInjection(s: str) -> bool:
    regex: Final = '(ALTER|CREATE|DELETE|DROP|EXEC(UTE){0,1}|INSERT( +INTO){0,1}|MERGE|SELECT|UPDATE|UNION( +ALL){0,1})'
    return re.search( regex, s )

def CheckKeys( data: list, keys: list ) -> bool:
    for _ in keys:
        if not ( _ in data ):
            return False
    return True

def CheckTypes( data: list, types: list ) -> bool:
    for i, j in zip(data, types):
        if type(i) != j:
            return False
    return True

# 이메일 체크
def isClearEmail(data: object):
    email: str = data["email"]

    if CheckInjection(email):
        return False

    if not CheckEmail(email):
        return False

    return True

# 페스워드 체크
def isClearPwd(data: object):
    pwd: str = data["pwd"]

    if CheckInjection(pwd):
        return False

    if not CheckPwd(pwd):
        return False

    return True

def isCleanSignData( data: object ):
    # 키 값이 정상적으로 왔는지
    if not CheckKeys( list( data.keys() ), ["email", "pwd", "name", "id"] ):
        return False
    
    # 값들의 자료형이 잘 왔는지
    datas = data["email"], data["pwd"], data["name"], data["id"]
    if not CheckTypes( datas, [ str, str, str, str ] ):
        return False

    if not isClearEmail(data):
        return False
    
    if not isClearPwd(data):
        return False

    if CheckInjection(data["name"]):
        return False

    if CheckInjection(data["id"]):
        return False

    return True

def isCleanLoginData( data: object ):
    # 키 값이 정상적으로 왔는지
    if not CheckKeys( list( data.keys() ), ["id", "pwd"] ):
        return False
    
    # 값들의 자료형이 잘 왔는지
    datas = data["id"], data["pwd"]
    if not CheckTypes( datas, [ str, str ] ):
        return False

    if CheckInjection(data["id"]):
        return False
    
    if not isClearPwd(data):
        return False
    
    return True