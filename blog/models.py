from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(default='default.jpg', upload_to='post_image', null=True)

    def __str__(self):
        return self.title

