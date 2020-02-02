from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# model to save data to db
class Search(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    search_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.from_location}-{self.to_location}"

