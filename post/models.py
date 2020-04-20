from django.db import models
from users.models import User
from business.models import Business, Service


class Post(models.Model):
    """
        Post model
    """
    caption = models.CharField(max_length=200)
    like_count = models.IntegerField()
    created_by = models.ForeignKey(Business, on_delete=models.CASCADE)
    service = models.ForeignKey(
        Service, related_name='posts', on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(
        User, verbose_name="liked by these users", related_name="liked_posts")
    media_url = models.CharField(max_length=100)
    media_type = models.CharField(max_length=50)

    @property
    def is_liked(self):
        """ check if post is liked by user making request """
        if self.user in self.liked_by.all():
            return True
        return False

    @classmethod
    def set_user(cls, user):
        """ set user """
        cls.user = user

    def __str__(self):
        """Return appointment details"""
        return self.created_by.name
