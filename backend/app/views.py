from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
import json
from pathlib import Path

class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Category.objects.all()

class CategoryItemView(CategoryListView):
    def get_queryset(self):
        return Category.objects.filter(id=self.kwargs['cat_id'])
    
class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):        
        return Product.objects.all()
    
class CategoryProductView(ProductListView):
    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['cat_id'])   
    
class ProductItemView(ProductListView):
    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs['prod_id'])    
    
class ImageListView(generics.ListAPIView):
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):        
        return Image.objects.all()

class ImageProductView(ImageListView):
    def get_queryset(self):        
        return Image.objects.filter(product=self.kwargs['prod_id'])

class VariantListView(generics.ListAPIView):
    serializer_class = VariantSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):        
        return Variant.objects.all()
    
class VariantProductView(VariantListView):
    def get_queryset(self):
        return Variant.objects.filter(product=self.kwargs['prod_id'])
    
class VariantDataListView(generics.ListAPIView):
    serializer_class = VariantDataSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):        
        return VariantData.objects.all()
    
class VariantDataVariantView(VariantDataListView):    
    def get_queryset(self):        
        return VariantData.objects.filter(variant=self.kwargs['var_id'])    

def start(request):
    file = Path.open('data.jsonl', encoding="utf-8")
    for line in file:
        data = json.loads(line)
        name = data.get("parent", None)
        
        catObj = Category.objects.filter(name=name)
        if not catObj.exists():
            catObj = Category.objects.create(name=name)
        else:
            catObj = Category.objects.filter(name=name)[0]
        
        prodObj = Product.objects.filter(url=data.get("url", None))
        if not prodObj.exists():
            prodObj = Product.objects.create(
                category=catObj, 
                url=data.get("url", None), 
                title=data.get("title", None),
                price = data.get("price", None),
                mrp = data.get("mrp", None),
                weekly_sale = data.get("weekly_sale", None),
                description = data.get("description", None),
                fit = data.get("fit", None),
                fabric = data.get("fabric", None),
                pattern = data.get("pattern", None),
                neck = data.get("neck", None),
                sleeve = data.get("sleeve", None),
                length = data.get("length", None),
                waistrise = data.get("waistrise", None),
                waistband = data.get("waistband", None),
                bottomwearlength = data.get("bottomwearlength", None)
                )
        else:
            prodObj = prodObj[0]
        
        for image in data.get("images", None):
            if not Image.objects.filter(url=image, product=prodObj).exists():
                Image.objects.create(url=image, product=prodObj)
            
        for variant in data.get("variants", None):
            varObj = Variant.objects.filter(
                color=variant["color"], 
                image=variant["image"], 
                product=prodObj
            )
            
            if not varObj.exists():
                varObj = Variant.objects.create(
                    color=variant["color"],
                    image=variant["image"], 
                    product=prodObj
                )
            else:
                varObj = varObj[0]
            
            for i in range(0, len(variant.get("size", None))):
                varData = VariantData.objects.filter(
                    size=variant["size"][i],
                    quantity=variant["quantity"][i],
                    variant=varObj
                )
                
                if not varData.exists():
                    VariantData.objects.create(
                        size=variant["size"][i],
                        quantity=variant["quantity"][i],
                        variant=varObj
                    )
    
    return HttpResponse("Date Read")