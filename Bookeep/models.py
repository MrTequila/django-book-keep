from django.db import models
from django.contrib.auth.models import User


# User profile, to keep books he read.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username


# Book class, with start and finish date, to keep track how long each book was read.
class Book(models.Model):
    user = models.ForeignKey('UserProfile', default=1, null=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    pages = models.IntegerField()
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    time_read = 0

    def __str__(self):
        return self.title
