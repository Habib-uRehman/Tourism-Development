from django.db import models
<<<<<<< HEAD

class touristGUideForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    languages = models.CharField(max_length=100)
    age = models.IntegerField()
=======
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.forms import CharField, DateField
# Create your models here.

class restraunt (models.Model):
    restraunt_name = models.CharField(max_length=100, null=True)
    establisment_date = models.DateField()
    commission_date = models.DateField()
    telex_num = models.IntegerField(null=True)
    telephone_num = models.IntegerField( null=True)
    address = models.TextField(max_length=100, null=True)
    telegraphic_num = models.IntegerField(null=True)

# location

    PROVINCE_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)
    province = models.CharField(max_length=10 , choices=PROVINCE_CHOICES, default='green')
    town = models.CharField(max_length=20 , null=True)
    street = models.CharField(max_length=100, null=True)

    OWNERSHIP_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)


    
>>>>>>> f9f08b041357f759ba9409a043a25b487d8744c4
