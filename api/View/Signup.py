
import os
from typing import Final
from rest_framework.request    import Request
from rest_framework.decorators import APIView

from api.Model.Account import Account
from api.Functions.getMessageResponse import getMessageResponse

from api.Functions.getHashPassword import getHashPassword
from api.Functions.CleanData import isCleanSignData

'''
[ /api/signup, POST ]
Request
header: { }
body: {
    "id": "",
    "pwd": "",
    "email": "",
    "name": ""
}

Resopnse
body: {
    data: {},
    message: { msg: "", status: "" }
}
'''
class Signup(APIView):
    def post(self, request: Request):
        data: Final = request.data

        # 데이터 검증
        if not isCleanSignData(data):
            return getMessageResponse("SAGI_SIGNUP_FAILED", 400)

        # ID, Email, Name 중복 체크
        if Account.objects.filter( id = data['id'] ).exists():
            return getMessageResponse("SAGI_SIGNUP_OVERLAP_ID", 400)
        if Account.objects.filter( email = data['email'] ).exists():
            return getMessageResponse("SAGI_SIGNUP_OVERLAP_EMAIL", 400)
        if Account.objects.filter( name = data['name'] ).exists():
            return getMessageResponse("SAGI_SIGNUP_OVERLAP_NAME", 400)

        id, email, name = data['id'], data['email'], data['name']
        salt = os.urandom(64)
        pwd  = getHashPassword( data['pwd'].encode('ascii'), salt )

        Account.objects.create( id = id, email = email, name = name, pwd = pwd, salt = salt )

        return getMessageResponse("SAGI_SIGNUP_OK", 200)
