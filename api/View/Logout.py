
from datetime import datetime
from typing import Final
from rest_framework.response   import Response
from rest_framework.request    import Request
from rest_framework.decorators import APIView

from api.Model.Account import Account
from api.Functions.getMessageResponse import getMessageResponse

from api.Functions.CleanData import isCleanLogoutData

'''
[ /api/logout, POST ]
Request
header: { }
body: {
    "name": "",
    "email": ""
}

Resopnse
body: {
    message: { msg: "", status: "" }
}
'''
class Logout(APIView):
    def post(self, request: Request) -> Response:
        data: Final = request.data

        # 데이터 검증
        if not isCleanLogoutData(data):
            return getMessageResponse("SAGI_LOGOUT_FAILED", 400)
        
        # 아이디가 있는지 검증
        if not Account.objects.filter(id = data["email"]).exists():
            return getMessageResponse("SAGI_LOGOUT_UNVALIED_EMAIL", 400)

        name, email = data['name'], data['email']
        account = Account.objects.get( name = name, email = email )

        if account.is_login == 0:
            return getMessageResponse("SAGI_LOGOUT_ALREADY", 400)

        _now = datetime.datetime.now()
        account.is_login    = 0
        account.logout_dt   = _now
        account.modified_dt = _now
        
        return getMessageResponse("SAGI_LOGOUT_OK", 400)