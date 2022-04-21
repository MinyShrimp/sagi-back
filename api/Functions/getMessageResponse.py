
from rest_framework.response import Response
from api.Model.Message       import Message
from api.Serializer.Message  import MessageSerializer

def getMessage(code: str):
    return MessageSerializer(Message.getByCode(code)).data

def getMessageResponse(code: str, status: int):
    return Response(getMessage(code), status = status)