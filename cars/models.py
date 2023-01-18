from django.db import models
from _datetime import datetime


# Create your models here.
class Car(models.Model):
    state_choices = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    year_choices = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choices.append((r, r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    title = models.CharField(max_length=255)
    state = models.CharField(max_length=2, choices=state_choices)
    city = models.CharField(max_length=65)
    color = models.CharField(max_length=65)
    model = models.CharField(max_length=65)
    year = models.IntegerField('year', choices=year_choices)
    condition = models.CharField(max_length=65)
    price = models.IntegerField()
    description = models.TextField()
    features = models.CharField(max_length=65, choices=features_choices)
    body_style = models.CharField(max_length=65)
    engine = models.CharField(max_length=65)
    transmission = models.CharField(max_length=65)
    interior = models.CharField(max_length=65)
    miles = models.IntegerField()
    doors = models.ImageField('doors', choices=door_choices)
    passengers = models.SmallIntegerField(default=5)
    vin = models.CharField(max_length=65)
    fuel_type = models.CharField(max_length=65)
    owners = models.CharField(max_length=65)
    is_featured = models.BooleanField(default=False)
    car_photo = models.ImageField(upload_to='media/cars/photos/%Y/%m/%d/', blank=True)
    car_photo_1 = models.ImageField(upload_to='media/cars/photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='media/cars/photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='media/cars/photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='media/cars/photos/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

