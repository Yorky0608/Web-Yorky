from django.contrib import admin

from .models import Question, Response, Video, Blog, Post

admin.site.register(Question)
admin.site.register(Response)
admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Video)