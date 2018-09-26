from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.TextField(unique=True)
    user_id = models.TextField(unique=True)

    def __str__(self):
        return self.user_name
