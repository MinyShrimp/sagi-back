
from django.db import models
from api.Code import MSG_STATUS

class Message(models.Model):
    msg    = models.CharField(max_length = 100)
    status = models.CharField(max_length = 100)

    @staticmethod
    def getByCode(code: str):
        return Message(msg=MSG_STATUS[code], status=code)