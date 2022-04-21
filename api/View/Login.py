
import os, datetime
from typing import Final
from rest_framework.request    import Request
from rest_framework.decorators import APIView

from api.Model.Account import Account
# from api.Serializer.Account import AccountLoginSerializer
from api.Functions.getMessageResponse import getMessageResponse

from api.Functions.getHashPassword import getHashPassword
from api.Functions.CleanData import isCleanLoginData, isCleanSignData

'''
[ /api/signup, POST ]
Request
header: { }
body: {
    "id": "",
    "pwd": ""
}

Resopnse
body: {
    data: {},
    message: { msg: "", status: "" }
}
'''
class Login(APIView):
    def post(self, request: Request):
        data: Final = request.data

        # 데이터 검증
        if not isCleanLoginData(data):
            return getMessageResponse("SAGI_LOGIN_FAILED", 400)

        id, pwd = data['id'], data['pwd']
        account = Account.objects.get( id = id, pwd = pwd )
        
        salt = account.salt
        _pwd = getHashPassword( pwd.encode('ascii'), salt )
        if account.pwd != _pwd:
            return getMessageResponse("SAGI_LOGIN_UNVALIED_PWD", 400)

        _now = datetime.datetime.now()

        account.is_login    = 1
        account.login_dt    = _now
        account.modified_dt = _now
        
        return getMessageResponse("SAGI_LOGIN_OK", 200)