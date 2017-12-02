from .models import Recipe, Image
from rest_framework import serializers


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Recipe
        fields = ('id', 'owner', 'title', 'serves', 'ingredients', 'method')

class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Image
        fields = ('id', 'owner', 'image')
