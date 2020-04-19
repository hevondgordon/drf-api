from django.db import models
from users.models import User
from business.models import Business, Service


class Post(models.Model):
    """
        Post model
    """
    caption = models.CharField(max_length=200)
    like_count = models.IntegerField()
    is_liked = models.BooleanField(default=False)
    created_by = models.ForeignKey(Business, on_delete=models.CASCADE)
    service = models.ForeignKey(
        Service, related_name='posts', on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(
        User, verbose_name="liked by these users", related_name="liked_posts")
    media_url = models.CharField(max_length=100)
    media_type = models.CharField(max_length=50)

    def __str__(self):
        """Return appointment details"""
        return self.created_by.name
