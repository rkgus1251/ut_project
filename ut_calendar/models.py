from django.db import models


class Date(models.Model) :
    date = models.DateTimeField()
    subject = models.CharField(max_length=100)
    content = models.TextField()
