
from typing import Final
from rest_framework.response   import Response
from rest_framework.request    import Request
from rest_framework.decorators import APIView

from api.Model.Account      import Account
from api.Serializer.Account import AccountSerializer

class Signup(APIView):
    def post(self, request: Request):
        data: Final = request.data

        print(data)

        # Account.objects.create(  )

        return Response()