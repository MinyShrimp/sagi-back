
from logging import getLogger
from typing import Final
from rest_framework.response   import Response
from rest_framework.request    import Request
from rest_framework.decorators import APIView

'''
[ /api/test, POST ]
Request
header: { }
body: {}

Resopnse
body: {
    message: { msg: "", status: "" }
}
'''

logger = getLogger("sagi")

class Test(APIView):
    def post(self, request: Request) -> Response:
        data: Final = request.data

        logger.info('test')
        
        return Response("test", status = 200)