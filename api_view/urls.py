from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserList, UserDetail, EmployeeList, EmployeeDetail, AttendanceList, AttendanceDetail, home


urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('attendance/', AttendanceList.as_view(), name='attendance-list'),
    path('attendance/<int:pk>/', AttendanceDetail.as_view(), name='attendance-detail'),
    path("status/", home),
]


