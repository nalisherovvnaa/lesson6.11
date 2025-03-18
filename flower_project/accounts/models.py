# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from .models import Post


# class CustomUser(AbstractUser):
#     profile_image = models.ImageField(upload_to='profiles/', default='profiles/default.jpg')

#     class Meta:
#         swappable = 'AUTH_USER_MODEL'

#     groups = models.ManyToManyField(
#         "auth.Group",
#         related_name="customuser_groups",
#         blank=True
#     )
#     user_permissions = models.ManyToManyField(
#         "auth.Permission",
#         related_name="customuser_permissions",
#         blank=True
#     )

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/default.jpg')

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",
        blank=True
    )


class Post(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title