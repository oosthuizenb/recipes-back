from django.conf import settings
from django.db import models
import os

class Recipe(models.Model):
    owner = models.ForeignKey('auth.User', models.CASCADE, related_name='recipes', default=1)
    title = models.CharField(max_length=80)
    serves = models.IntegerField()
    ingredients = models.TextField(help_text='seperate with comma')
    method = models.TextField()
    featured_image = models.ImageField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.featured_image.name))
        super(Image, self).delete(*args, **kwargs)

    class Meta:
        ordering = ['-updated', '-timestamp']


class Image(models.Model):
    recipe = models.ForeignKey(Recipe, models.CASCADE, related_name='images', blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        super(Image, self).delete(*args, **kwargs)

    class Meta:
        ordering = ['-updated', '-timestamp']
