import random
from django.core.management.base import BaseCommand
from rent_apartment.models import RentApartment, RentApartmentShots
from apartment.models import Brand, City, District, Category
from faker import Faker
from django.utils import timezone
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

fake = Faker()

class Command(BaseCommand):
    help = 'Generate dummy data for RentApartments and their related RentApartmentShots'

    def handle(self, *args, **kwargs):
        # Create dummy data for Brands, Cities, Districts, and Categories
        brands = [Brand.objects.create(name=fake.company()) for _ in range(5)]
        cities = [City.objects.create(name=fake.city()) for _ in range(3)]
        districts = [District.objects.create(name=fake.city()) for _ in range(10)]
        categories = [Category.objects.create(name=fake.word()) for _ in range(5)]

        # Create dummy RentApartments
        for _ in range(10):  # Number of dummy rent apartments to create
            image_url = self.get_rent_apartment_shot_image()
            tenant_image_url = self.get_rent_apartment_shot_image()  # Use same image API for tenant image
            image_name = f"rent_apartment_{fake.word()}.jpg"
            tenant_image_name = f"tenant_{fake.word()}.jpg"
            image_path = self.save_image_from_url(image_url, image_name)
            tenant_image_path = self.save_image_from_url(tenant_image_url, tenant_image_name) if tenant_image_url else None

            rent_apartment = RentApartment.objects.create(
                name=fake.word(),
                price_per_m=round(random.uniform(1.0, 50.0), 2),
                apartment=random.randint(1, 5),
                tenant_name=fake.name(),
                tenant_image=tenant_image_path,
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
                brand=random.choice(brands),
                city=random.choice(cities),
                district=random.choice(districts),
                category=random.choice(categories),  # Added category
            )

            # Create dummy RentApartmentShots for each rent apartment
            for shot_num in range(1, 3):
                image_url = self.get_rent_apartment_shot_image()
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

        self.stdout.write(self.style.SUCCESS('Successfully created dummy data for RentApartments and RentApartmentShots.'))

    def get_rent_apartment_shot_image(self):
        access_key = ''  # Replace with your Unsplash access key
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
                image_path = f'rent_apartment_shots/{image_name}'
                default_storage.save(image_path, ContentFile(response.content))
                return image_path
            else:
                self.stderr.write(f'Failed to fetch image from URL: {url}')
                return None
        except Exception as e:
            self.stderr.write(f'Failed to save image from URL: {str(e)}')
            return None
