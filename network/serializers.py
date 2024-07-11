from rest_framework import serializers
from .models import NetworkNode, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt',)

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        network_node = NetworkNode.objects.create(**validated_data)
        for product_data in products_data:
            product, created = Product.objects.get_or_create(**product_data)
            network_node.products.add(product)
        network_node.clean()  # Validate before saving
        network_node.save()
        return network_node

    def update(self, instance, validated_data):
        products_data = validated_data.pop('products')
        instance = super().update(instance, validated_data)
        instance.products.clear()
        for product_data in products_data:
            product, created = Product.objects.get_or_create(**product_data)
            instance.products.add(product)
        instance.clean()  # Validate before saving
        instance.save()
        return instance
