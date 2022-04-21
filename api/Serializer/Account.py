
from rest_framework import serializers
from api.Model.Account import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class AccountLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [ "id", "pwd", "salt" ]