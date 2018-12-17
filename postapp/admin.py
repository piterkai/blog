from django.contrib import admin

# Register your models here.
from postapp.models import *

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)