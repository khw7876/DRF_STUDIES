from rest_framework import serializers
from product.models import Product as ProductModel


class ProductSerializer(serializers.ModelSerializer):
    # product = serializers.SerializerMethodField()
    # def get_product(self, obj):
    #     return obj.user.username
    
    class Meta:
        model = ProductModel
        fields = ["user", "name", "thumbnail", "description", 
                  "created", "exposure_start_date", "exposure_end_date"
        ]