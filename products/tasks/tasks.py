import os
import json

from django.db import transaction
from celery import shared_task

from products.management.commands.parsing import Command
from products.models import Brand, Category, Size, Product, ProductImage


@shared_task
def perform_parsing():
    command = Command()
    command.handle()

@shared_task
def deserialize_json():
    """
    заполняем данными из json чтобы не писать все ручками
    """

    json_file_path = os.path.join(os.path.dirname(__file__), '..', 'products.json')

    with open(json_file_path) as f:
        data = json.load(f)
        products_data = data.get('products', [])

    with transaction.atomic():
        for product_data in products_data:
            brand_name = product_data.get('brand')
            category_name = product_data.get('category')

            brand, created_brand = Brand.objects.get_or_create(name=brand_name)
            category, created_category = Category.objects.get_or_create(name=category_name)

            if category not in brand.categories.all():
                brand.categories.add(category)

            product = Product.objects.create(
                name=product_data.get('name', ''),
                description=product_data.get('description', ''),
                price=product_data.get('price', 0),
                category=category,
                brand=brand,
                image=product_data.get('image', ''),
                is_sale=product_data.get('is_sale', False),
                gender=product_data.get('gender'),
            )

            sizes = product_data.get('sizes', [])
            for size_title in sizes:
                if size_title:
                    size, created_size = Size.objects.get_or_create(title=size_title.strip())
                    product.sizes.add(size)

            images = product_data.get('images', [])
            for image_url in images:
                if image_url:
                    ProductImage.objects.create(product=product, image=image_url.strip())
