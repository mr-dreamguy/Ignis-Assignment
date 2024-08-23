from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "category", "url", "title", "price", "mrp", "weekly_sale", "description", "fit", "fabric", "pattern", "neck", "sleeve", "length", "waistrise", "waistband", "bottomwearlength"]
        extra_kwargs = {"category" : {"read_only" : True}}
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "url", "product"]
        extra_kwargs = {"product" : {"read_only" : True}}
        
class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ["id", "color", "image", "product"]
        extra_kwargs = {"product" : {"read_only" : True}}
        
class VariantDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantData
        fields = ["id", "size", "quantity", "variant"]
        extra_kwargs = {"variant" : {"read_only" : True}}