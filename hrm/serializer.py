from rest_framework import serializers
from hrm.models import Users
class UsersSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(required = False)
    name = serializers.CharField(required = False)
    ranking = serializers.FloatField(required = False)

    class Meta:
        model = Users
        # fields = ('employee_id', 'name')
        fields = '__all__' 
