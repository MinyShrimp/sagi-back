
import os
from typing import Final
from rest_framework.response   import Response
from rest_framework.request    import Request
from rest_framework.decorators import APIView

from api.Model.Account import Account

from api.Functions.getHashPassword import getHashPassword

class Signup(APIView):
    def post(self, request: Request):
        data: Final = request.data

        # 데이터 검증

        # ID, Email 중복 체크

        id, email, name = data['id'], data['email'], data['name']
        salt = os.urandom(64)
        pwd  = getHashPassword( data['pwd'].encode('ascii'), salt )

        Account.objects.create( id = id, email = email, name = name, pwd = pwd, salt = salt )

        return Response({ "msg": "good", "code": "SIGNUP_OK" }, status=200)