from django.db import models
from accounts.models import User


class Date(models.Model) :

    class TypeChoices(models.TextChoices) :
        A = "초음파"
        B = "자궁경부암"
        C = "질염"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    subject = models.CharField('질병', max_length=5, choices=TypeChoices.choices)
    content = models.TextField()
