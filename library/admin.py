from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

class UserModel(UserAdmin):
    pass
admin.site.register(CustomUser,UserModel)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Publication)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Issue)

