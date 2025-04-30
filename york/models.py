from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


class Question(models.Model):
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'response'

        def __str__(self):
            return f"{self.text}"

# This is an option that I may use.
class Video(models.Model):
    YORK = 'York'
    MINECRAFT = "MC"
    MUSIC = 'Musc'
    CATEGORY_CHOICES = [
        (YORK, 'York'),
        (MINECRAFT, 'Minecraft'),
        (MUSIC, 'Music'),
    ]

    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    category = models.CharField(
        max_length=4,
        choices=CATEGORY_CHOICES,
        default=YORK
    )

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-title']


class Blog(models.Model):
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'post'

        def __str__(self):
            return f"{self.text}"