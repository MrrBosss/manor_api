import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from apartment.models import Brand, City, District
from rent_apartment.models import RentApartment, RentApartmentShots

fake = Faker()

class Command(BaseCommand):
    help = 'Generate dummy data for RentApartment and related RentApartmentShots'

    def handle(self, *args, **kwargs):
        for _ in range(10):  # Number of dummy apartments to create
            image_url = self.get_apartment_shot_image()
            image_name = f"rent_apartment_{fake.word()}.jpg"
            image_path = self.save_image_from_url(image_url, image_name)

            # Create dummy RentApartment
            rent_apartment = RentApartment.objects.create(
                name=fake.company(),
                price_per_m=round(random.uniform(1.0, 50.0), 2),
                apartment=random.randint(1, 10),
                tenant_name=fake.name(),
                tenant_image=image_path,
                company=fake.company(),
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
                created_at=timezone.now(),
                brand=self.get_random_brand(),
                city=self.get_random_city(),
                district=self.get_random_district(),
            )
            # self.stdout.write(self.style.SUCCESS(f'Created RentApartment: {rent_apartment.name}'))

            # Create dummy RentApartmentShots for each apartment
            for shot_num in range(1, 3):  # Number of shots per apartment
                image_url = self.get_apartment_shot_image()
                if image_url:
                    image_name = f"rent_apartment{_ + 1}_shot_{shot_num}.jpg"
                    image_path = self.save_image_from_url(image_url, image_name)
                    if image_path:
                        RentApartmentShots.objects.create(
                            rent_apartment=rent_apartment,
                            image=image_path,
                            created_at=timezone.now(),
                        )

            self.stdout.write(self.style.SUCCESS(f'Successfully created RentApartment {_ + 1} and its shots.'))

        self.stdout.write(self.style.SUCCESS('Successfully created 10 dummy RentApartment instances with shots.'))

    
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

    def get_random_brand(self):
        return Brand.objects.order_by('?').first()

    def get_random_city(self):
        return City.objects.order_by('?').first()

    def get_random_district(self):
        return District.objects.order_by('?').first()
