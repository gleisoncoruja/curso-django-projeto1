from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    serving_unit = models.CharField(max_length=65)
    preparation_steps = models.models.TextField()
    prepartion_steps_is_html = models.BooleanField(defaut=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(defaut=False)
    cover = models.ImageField(upload_to='recippes/covers/%Y/%m/%d')
