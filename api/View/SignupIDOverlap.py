
from typing import Final
from rest_framework.response   import Response
from rest_framework.request    import Request
from rest_framework.decorators import APIView

from api.Model.Account      import Account

class SignupIDOverlap(APIView):
    def post(self, request: Request):
        data: Final = request.data

        # 데이터 검증

        # ID 중복 체크
        isOverlap = Account.objects.filter(id = data["id"]).exists()
        if isOverlap:
            return Response("아이디 중복!", status=200)

        return Response("사용해도 되는 아이디", status=200)