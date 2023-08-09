from rest_framework import generics
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from .models import UserTable, AttendanceTable, EmployeeTable
from django.contrib.auth.models import User
from .serializer import UserSerializer, EmployeeSerializer, AttendanceSerializer



def home(request):
    return JsonResponse({"status": "up"})


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class EmployeeList(generics.ListCreateAPIView):
    queryset = EmployeeTable.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeTable.objects.all()
    serializer_class = EmployeeSerializer


class AttendanceList(generics.ListCreateAPIView):
    queryset = AttendanceTable.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceTable.objects.all()
    serializer_class = AttendanceSerializer