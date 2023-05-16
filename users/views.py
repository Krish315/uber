from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import*
from users.serializers import*

class GetStudentsView(APIView):

    def get(self, request):
     def post(self,request): 
        params = request.data
        print("params", params)
        return Response("message","Done")
     
        print("req", request.Get)
        name = request.Get.get("my name")
        print("name", name)
        if name:
            instance=Student.objects.filter(first_name=name)
        else:
            instance=Student.objects.all()            
        
        serializers = Student(instance,many=True)
        return Response(serializers.data)