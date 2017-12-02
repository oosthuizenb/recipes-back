from django.db import models


class Recipe(models.Model):
    owner = models.ForeignKey('auth.User', models.CASCADE, related_name='recipes', default=1)
    title = models.CharField(max_length=80)
    serves = models.IntegerField()
    ingredients = models.TextField(help_text='seperate with comma')
    method = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated', '-timestamp']


class Image(models.Model):
    owner = models.ForeignKey('auth.User', models.CASCADE, related_name='images', default=1)
    image = models.ImageField(upload_to='images/', null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image

    class Meta:
        ordering = ['-updated', '-timestamp']
