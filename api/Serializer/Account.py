
from rest_framework import serializers

from api.Model.Account import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'