from django.core.validators import MinLengthValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Hero(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,
                            validators=[MinLengthValidator(1)])
    page_url = models.URLField()
    desc = models.TextField(blank=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
                'pk': self.pk,
                'name': self.name,
                'photo_url': self.photo.url,
                'page_url': self.page_url
            }