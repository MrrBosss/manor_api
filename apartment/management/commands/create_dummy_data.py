import random
from django.core.management.base import BaseCommand
from apartment.models import Apartment, ApartmentShots, Brand, City, District
from faker import Faker
from django.utils import timezone
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

fake = Faker()

class Command(BaseCommand):
    help = 'Generate dummy data for Apartments and their related ApartmentShots'

    def handle(self, *args, **kwargs):
        # Create dummy data for Brands, Cities, and Districts
        brands = [Brand.objects.create(name=fake.company()) for _ in range(5)]
        cities = [City.objects.create(name=fake.city()) for _ in range(3)]
        districts = [District.objects.create(name=fake.city()) for _ in range(10)]

        # Create dummy Apartments
        for _ in range(10):  # Number of dummy apartments to create
            image_url = self.get_apartment_shot_image()
            image_name = f"apartment_{fake.word()}.jpg"
            image_path = self.save_image_from_url(image_url, image_name)

            apartment = Apartment.objects.create(
                name=fake.word(),
                company_name=fake.company(),
                price=round(random.uniform(50.0, 500.0), 2),
                price_per_m=round(random.uniform(5.0, 50.0), 2),
                apartment_sold=random.randint(0, 10),
                total_area=round(random.uniform(50.0, 200.0), 2),
                residential_are=round(random.uniform(30.0, 150.0), 2),
                floor=random.randint(1, 10),
                year_of_delivery=random.randint(2020, 2025),
                house=fake.address(),
                finishing=fake.word(),
                viev_from_window=fake.word(),
                bathroom=random.randint(1, 3),
                type=fake.word(),
                description=fake.text(),
                is_finish=fake.boolean(),
                is_mortgage=fake.boolean(),
                brand=random.choice(brands),
                city=random.choice(cities),
                district=random.choice(districts),
            )

            # Create dummy ApartmentShots for each apartment
            for shot_num in range(1, 3):
                image_url = self.get_apartment_shot_image()
                if image_url:
                    image_name = f"apartment{_ + 1}_shot_{shot_num}.jpg"
                    image_path = self.save_image_from_url(image_url, image_name)
                    if image_path:
                        ApartmentShots.objects.create(
                            apartment=apartment,
                            image=image_path,
                            created_at=timezone.now(),
                        )

            self.stdout.write(self.style.SUCCESS(f'Successfully created Apartment {_ + 1} and its shots.'))

        self.stdout.write(self.style.SUCCESS('Successfully created dummy data for Apartments and ApartmentShots.'))

    def get_apartment_shot_image(self):
        access_key = 'NNpH9MjyQNMfmuBxreAQmnSjzb2cCJk9nWCGFfd7M2M'  # Replace with your Unsplash access key
        url = f'https://api.unsplash.com/photos/random?query=apartment&orientation=landscape'
        headers = {
            'Accept-Version': 'v1',
            'Authorization': f'Client-ID {access_key}'
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return data['urls']['regular']
        else:
            self.stderr.write(f'Error fetching image: {response.text}')
            return ''

    def save_image_from_url(self, url, image_name):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                image_path = f'apartment_shots/{image_name}'
                default_storage.save(image_path, ContentFile(response.content))
                return image_path
            else:
                self.stderr.write(f'Failed to fetch image from URL: {url}')
                return None
        except Exception as e:
            self.stderr.write(f'Failed to save image from URL: {str(e)}')
            return None
