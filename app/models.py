from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'


class Recipe(models.Model):
    name = models.CharField(blank=False, max_length=80)
    description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    instruction =  models.TextField(blank=True)
    prep_time = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    publish_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads/', blank=True)
    category = models.ForeignKey(Category, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        # More Meta options:
        # https://docs.djangoproject.com/en/4.1/ref/models/options/
        ordering = ['-prep_time']
        db_table = "recipe"

