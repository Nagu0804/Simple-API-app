from django.contrib import admin
from .models import UserTable, EmployeeTable, AttendanceTable

# Register UserTable model
admin.site.register(UserTable)

# Register EmployeeTable model
admin.site.register(EmployeeTable)

# Register AttendanceTable model
admin.site.register(AttendanceTable)