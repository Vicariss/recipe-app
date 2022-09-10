from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(blank=False, max_length=80)
    description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    instruction = models.TextField(blank=True)
    prep_time = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    category = models.CharField(
        max_length=255, blank=False, default="No category")
    publish_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        # More Meta options:
        # https://docs.djangoproject.com/en/4.1/ref/models/options/
        ordering = ['-prep_time']
