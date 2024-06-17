from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .grpc import send_news


class NewsPost(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    author = models.ForeignKey(User, models.CASCADE)
    body = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="news")


class Comment(models.Model):
    author = models.ForeignKey(User, models.CASCADE)
    post = models.ForeignKey(
        NewsPost, models.CASCADE, null=False, blank=False, related_name="comments"
    )
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=NewsPost, weak=False)
def news_saved(sender: type[NewsPost], instance: NewsPost, **kwargs):
    send_news(
        instance.title, instance.author.username, url="", img=instance.image.read()
    )
