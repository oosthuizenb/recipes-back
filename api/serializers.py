from .models import Recipe, Image
from rest_framework import serializers


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Recipe
        fields = ('id', 'owner', 'title', 'serves', 'ingredients', 'method', 'featured_image')

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'recipe', 'image')
