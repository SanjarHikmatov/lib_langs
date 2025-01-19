from django.core.validators import MinValueValidator
from django.db import models

from django.contrib.auth.models import User


class Book(models.Model):
    class File_Formats(models.TextChoices):
        pdf = 'PDF',
        epub = 'Epub',
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    pages = models.PositiveSmallIntegerField(validators=[MinValueValidator(20)])
    published_date = models.DateField(auto_now=True)

    ebook_version = models.FileField(upload_to='files/ebook')
    file_format = models.CharField(max_length=50, choices=File_Formats.choices)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    sell_location = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)


