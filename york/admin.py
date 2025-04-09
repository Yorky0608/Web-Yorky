from django.contrib import admin

from .models import Question, Response, Video

admin.site.register(Question)
admin.site.register(Response)
admin.site.register(Video)