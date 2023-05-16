from rest_framework import serializers
from users.models import(Student,Order)
class student(serializers.ModelSerializers):
    class Meta:
        models=Student
        fields = '__all__';


class Order(serializers.ModelSerializers):
    class Meta:
        models=Order
        fields = '__all__';