from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # return super().has_add_permission(request)
        return True

    def has_change_permission(self, request, obj = ...):
        # return super().has_change_permission(request, obj)
        return True
    

admin.site.register(User, UserAdmin)

