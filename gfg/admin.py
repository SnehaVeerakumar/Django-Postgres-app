from django.contrib import admin
from .models import GeeksforGeeks
 
@admin.register(GeeksforGeeks)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
GeeksforGeeks._meta.get_fields()]
