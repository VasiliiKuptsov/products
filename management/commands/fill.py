from django.core.management import BaseCommand
from catalog.models import  Category, Product
from datetime import datetime
class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {"name":"мясо", "description":"hold"}, {"name":"рыба", "description":"hold"}
        ]


        category_for_create = []
        for item in category_list:
            category_for_create.append(Category(**item))

        Category.objects.bulk_create(category_for_create)


        product_list = [
            {"name": "окунь", "description": "морской", "image": "", "category": "рыба", "purchase_price": 800,
            "date_of_creation": "11-10-2023", "date_of_last_modification": "2023-10-11"},
            {"name": "свинина", "description": "мясо", "image": "", "category": "мясо", "purchase_price": 800,
            "date_of_creation": "2023-10-11", "date_of_last_modification": "2023-10-11"}
        ]

        product_for_create = []
        for product in product_list:
            category_name = product.get('category')
            category = Category.objects.get(name=category_name)
            product['category'] = category
            product_for_create.append(Product(**product))

        Product.objects.bulk_create(product_for_create)