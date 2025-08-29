from django.core.management.base import BaseCommand
from shopeazy.models import User, Product

class Command(BaseCommand):
    help = 'Populate the database with sample users and products'

    def handle(self, *args, **options):
        self.stdout.write('Starting database population...')
        
        # Populate Users
        self.populate_users()
        
        # Populate Products
        self.populate_products()
        
        self.stdout.write(
            self.style.SUCCESS('Database population completed successfully!')
        )

    def populate_users(self):
        users_data = [
            {
                'userid': 'U001',
                'fname': 'John',
                'lname': 'Doe',
                'email': 'john.doe@email.com',
                'address': '123 Main St, New York, NY 10001',
                'phoneno': '5551234567',
                'password': 'password123',
                'type': 'C'
            },
            {
                'userid': 'U002',
                'fname': 'Jane',
                'lname': 'Smith',
                'email': 'jane.smith@email.com',
                'address': '456 Oak Ave, Los Angeles, CA 90210',
                'phoneno': '5559876543',
                'password': 'password123',
                'type': 'C'
            },
            {
                'userid': 'U003',
                'fname': 'Mike',
                'lname': 'Johnson',
                'email': 'mike.johnson@email.com',
                'address': '789 Pine Rd, Chicago, IL 60601',
                'phoneno': '5554567890',
                'password': 'password123',
                'type': 'C'
            },
            {
                'userid': 'U004',
                'fname': 'Sarah',
                'lname': 'Wilson',
                'email': 'sarah.wilson@email.com',
                'address': '321 Elm St, Miami, FL 33101',
                'phoneno': '5557890123',
                'password': 'password123',
                'type': 'C'
            },
            {
                'userid': 'U005',
                'fname': 'David',
                'lname': 'Brown',
                'email': 'david.brown@email.com',
                'address': '654 Maple Dr, Seattle, WA 98101',
                'phoneno': '5553210987',
                'password': 'password123',
                'type': 'C'
            },
            {
                'userid': 'ADMIN',
                'fname': 'Admin',
                'lname': 'User',
                'email': 'admin@shopeazy.com',
                'address': 'Admin Address',
                'phoneno': '5550000000',
                'password': 'admin123',
                'type': 'A'
            }
        ]

        User.objects.all().delete()
        for user_data in users_data:
            try:
                User.objects.create(**user_data)
                self.stdout.write(f'Created user: {user_data["fname"]} {user_data["lname"]}')
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating user {user_data["fname"]}: {e}'))

    def populate_products(self):
        products_data = [
            {
                'productid': 1,
                'pname': 'iPhone 14 Pro',
                'price': 999,
                'category': 'Electronics',
                'specifications': '6.1-inch display, A16 Bionic chip, 48MP camera',
                'image': 'images/apple.jpeg',
                'rating': 4.8
            },
            {
                'productid': 2,
                'pname': 'Samsung Galaxy S23',
                'price': 899,
                'category': 'Electronics',
                'specifications': '6.1-inch display, Snapdragon 8 Gen 2, 50MP camera',
                'image': 'images/101.jpeg',
                'rating': 4.6
            },
            {
                'productid': 3,
                'pname': 'MacBook Pro 14"',
                'price': 1999,
                'category': 'Electronics',
                'specifications': '14-inch Retina display, M2 Pro chip, 16GB RAM',
                'image': 'images/102.jpeg',
                'rating': 4.9
            },
            {
                'productid': 4,
                'pname': 'Dell XPS 13',
                'price': 1299,
                'category': 'Electronics',
                'specifications': '13.4-inch InfinityEdge display, Intel i7, 16GB RAM',
                'image': 'images/103.jpeg',
                'rating': 4.5
            },
            {
                'productid': 5,
                'pname': 'Sony WH-1000XM4',
                'price': 349,
                'category': 'Electronics',
                'specifications': 'Wireless noise-canceling headphones, 30-hour battery',
                'image': 'images/104.jpeg',
                'rating': 4.7
            },
            {
                'productid': 6,
                'pname': 'Apple Watch Series 8',
                'price': 399,
                'category': 'Electronics',
                'specifications': '45mm display, GPS, heart rate monitor',
                'image': 'images/105.jpeg',
                'rating': 4.6
            },
            {
                'productid': 7,
                'pname': 'Nike Air Max 270',
                'price': 150,
                'category': 'Fashion',
                'specifications': 'Comfortable running shoes, breathable mesh',
                'image': 'images/106.jpeg',
                'rating': 4.4
            },
            {
                'productid': 8,
                'pname': 'Adidas Ultraboost 22',
                'price': 180,
                'category': 'Fashion',
                'specifications': 'Responsive cushioning, energy return',
                'image': 'images/107.jpeg',
                'rating': 4.5
            },
            {
                'productid': 9,
                'pname': 'Levi\'s 501 Jeans',
                'price': 89,
                'category': 'Fashion',
                'specifications': 'Classic straight fit, 100% cotton denim',
                'image': 'images/108.jpeg',
                'rating': 4.3
            },
            {
                'productid': 10,
                'pname': 'Ray-Ban Aviator',
                'price': 154,
                'category': 'Fashion',
                'specifications': 'Classic aviator sunglasses, UV protection',
                'image': 'images/109.jpeg',
                'rating': 4.4
            },
            {
                'productid': 11,
                'pname': 'Canon EOS R6',
                'price': 2499,
                'category': 'Electronics',
                'specifications': '20.1MP full-frame mirrorless camera, 4K video',
                'image': 'images/110.jpeg',
                'rating': 4.8
            },
            {
                'productid': 12,
                'pname': 'Sony A7 III',
                'price': 1999,
                'category': 'Electronics',
                'specifications': '24.2MP full-frame mirrorless, 5-axis stabilization',
                'image': 'images/111.jpeg',
                'rating': 4.7
            },
            {
                'productid': 13,
                'pname': 'iPad Air',
                'price': 599,
                'category': 'Electronics',
                'specifications': '10.9-inch Liquid Retina display, M1 chip',
                'image': 'images/112.jpeg',
                'rating': 4.6
            },
            {
                'productid': 14,
                'pname': 'Samsung Galaxy Tab S8',
                'price': 699,
                'category': 'Electronics',
                'specifications': '11-inch display, Snapdragon 8 Gen 1, S Pen included',
                'image': 'images/113.jpeg',
                'rating': 4.5
            },
            {
                'productid': 15,
                'pname': 'Bose QuietComfort 45',
                'price': 329,
                'category': 'Electronics',
                'specifications': 'Premium noise-canceling headphones, 24-hour battery',
                'image': 'images/114.jpeg',
                'rating': 4.6
            },
            {
                'productid': 16,
                'pname': 'Nike Dri-FIT T-Shirt',
                'price': 35,
                'category': 'Fashion',
                'specifications': 'Moisture-wicking fabric, comfortable fit',
                'image': 'images/115.jpeg',
                'rating': 4.2
            },
            {
                'productid': 17,
                'pname': 'Adidas Track Jacket',
                'price': 65,
                'category': 'Fashion',
                'specifications': 'Lightweight, breathable, zip-up design',
                'image': 'images/116.jpeg',
                'rating': 4.3
            },
            {
                'productid': 18,
                'pname': 'Under Armour Shorts',
                'price': 45,
                'category': 'Fashion',
                'specifications': 'Compression fit, moisture-wicking technology',
                'image': 'images/117.jpeg',
                'rating': 4.1
            },
            {
                'productid': 19,
                'pname': 'Puma Running Shoes',
                'price': 120,
                'category': 'Fashion',
                'specifications': 'Lightweight design, responsive cushioning',
                'image': 'images/118.jpeg',
                'rating': 4.3
            },
            {
                'productid': 20,
                'pname': 'New Balance 990v5',
                'price': 185,
                'category': 'Fashion',
                'specifications': 'Premium comfort, ENCAP midsole technology',
                'image': 'images/119.jpeg',
                'rating': 4.4
            },
            {
                'productid': 21,
                'pname': 'ASICS Gel-Kayano 28',
                'price': 160,
                'category': 'Fashion',
                'specifications': 'Stability running shoes, GEL technology',
                'image': 'images/120.jpeg',
                'rating': 4.5
            }
        ]

        Product.objects.all().delete()
        for product_data in products_data:
            try:
                Product.objects.create(**product_data)
                self.stdout.write(f'Created product: {product_data["pname"]}')
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating product {product_data["pname"]}: {e}'))
