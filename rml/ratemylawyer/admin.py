from django.contrib import admin
from .models import Lawyer
from .models import Comment

# Register your models here.
admin.site.register(Lawyer)
admin.site.register(Comment)