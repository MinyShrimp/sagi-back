
from datetime import datetime
from typing import Final
from rest_framework.response   import Response
from rest_framework.request    import Request
from rest_framework.decorators import APIView

from api.Model.Account import Account
from api.Functions.getMessageResponse import getMessage, getMessageResponse

from api.Functions.getHashPassword import getHashPassword
from api.Functions.CleanData import isCleanLoginData
from api.Serializer.Account import AccountLoginSerializer

'''
[ /api/login, POST ]
Request
header: { }
body: {
    "id": "",
    "pwd": ""
}

Resopnse
body: {
    data: {
        "name": "",
        "email": "",
    },
    message: { msg: "", status: "" }
}
'''
class Login(APIView):
    def post(self, request: Request) -> Response:
        data: Final = request.data

        # 데이터 검증
        if not isCleanLoginData(data):
            return getMessageResponse("SAGI_LOGIN_FAILED", 400)
        
        # 아이디가 있는지 검증
        if not Account.objects.filter(id = data["id"]).exists():
            return getMessageResponse("SAGI_LOGIN_UNVALIED_ID", 400)

        id, pwd = data['id'], data['pwd']
        account = Account.objects.get( id = id, pwd = pwd )
        
        salt = account.salt
        _pwd = getHashPassword( pwd.encode('ascii'), salt )
        if account.pwd != _pwd:
            return getMessageResponse("SAGI_LOGIN_UNVALIED_PWD", 400)
        
        if account.is_login == 1:
            return getMessageResponse("SAGI_LOGIN_ALREADY", 400)

        _now = datetime.datetime.now()

        account.is_login    = 1
        account.login_dt    = _now
        account.modified_dt = _now

        serializer = {
            "data": AccountLoginSerializer( account ).data,
            "msg": getMessage("SAGI_LOGIN_OK")
        }
        
        return Response(serializer, status = 200)