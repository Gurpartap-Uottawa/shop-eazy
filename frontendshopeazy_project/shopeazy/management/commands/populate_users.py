from django.core.management.base import BaseCommand
from shopeazy.models import User

class Command(BaseCommand):
    help = 'Populate the database with sample users'

    def handle(self, *args, **options):
        # Sample user data
        users_data = [
            {
                'userid': 'U001',
                'fname': 'John',
                'lname': 'Doe',
                'email': 'john.doe@email.com',
                'address': '123 Main St, New York, NY 10001',
                'phoneno': '5551234567',
                'password': 'password123',
                'type': 'C'  # Customer
            },
            {
                'userid': 'U002',
                'fname': 'Jane',
                'lname': 'Smith',
                'email': 'jane.smith@email.com',
                'address': '456 Oak Ave, Los Angeles, CA 90210',
                'phoneno': '5559876543',
                'password': 'password123',
                'type': 'C'  # Customer
            },
            {
                'userid': 'U003',
                'fname': 'Mike',
                'lname': 'Johnson',
                'email': 'mike.johnson@email.com',
                'address': '789 Pine Rd, Chicago, IL 60601',
                'phoneno': '5554567890',
                'password': 'password123',
                'type': 'C'  # Customer
            },
            {
                'userid': 'U004',
                'fname': 'Sarah',
                'lname': 'Wilson',
                'email': 'sarah.wilson@email.com',
                'address': '321 Elm St, Miami, FL 33101',
                'phoneno': '5557890123',
                'password': 'password123',
                'type': 'C'  # Customer
            },
            {
                'userid': 'U005',
                'fname': 'David',
                'lname': 'Brown',
                'email': 'david.brown@email.com',
                'address': '654 Maple Dr, Seattle, WA 98101',
                'phoneno': '5553210987',
                'password': 'password123',
                'type': 'C'  # Customer
            },
            {
                'userid': 'ADMIN',
                'fname': 'Admin',
                'lname': 'User',
                'email': 'admin@shopeazy.com',
                'address': 'Admin Address',
                'phoneno': '5550000000',
                'password': 'admin123',
                'type': 'A'  # Admin
            }
        ]

        # Clear existing users
        User.objects.all().delete()
        self.stdout.write('Cleared existing users...')

        # Create new users
        created_count = 0
        for user_data in users_data:
            try:
                user = User.objects.create(**user_data)
                created_count += 1
                self.stdout.write(f'Created user: {user.fname} {user.lname}')
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating user {user_data["fname"]}: {e}'))

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} users!')
        )
