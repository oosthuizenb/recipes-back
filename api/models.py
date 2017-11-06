from django.db import models

# Create your models here.
class Recipe(models.Model):
    owner = models.ForeignKey('auth.User', related_name='recipes', default=1)
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
