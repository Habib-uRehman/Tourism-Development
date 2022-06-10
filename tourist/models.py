from asyncio.windows_events import NULL
import datetime
import numbers
from django.db import models
from pyexpat import model
from django.contrib.auth.models import AbstractBaseUser
from django.forms import CharField, DateField
from multiselectfield import MultiSelectField


class touristguideform(models.Model):
    guide_name = models.CharField(max_length=30 , null=True)
    business_address = models.CharField(max_length=100 , null=True)
    residential_address = models.CharField(max_length=100 , null=True)
    year_of_establishment = models.DateField(default=datetime.date.today)
    telephone_number = models.IntegerField(null=True)
    residential_number = models.IntegerField(null=True)
    telegraphic_address = models.CharField(max_length=100 , null=True)
    educational_qualifications = models.CharField(max_length=30 , null=True)
    year_of_experiance = models.IntegerField(null=True)
    number_of_languages = models.IntegerField(null=True)
    no_training = models.BooleanField(default=False)
    # training_Institute_Name = models.CharField(max_length=30 , null=True)
    # start_Date = models.DateField(default=datetime.date.today)
    # end_Date = models.DateField(default=datetime.date.today)
    bank_name = models.CharField(max_length=30 , null=True)
    reference_letter = models.FileField(default=NULL,upload_to='documents/%Y/%m/%d') 
    capital_invested = models.IntegerField(null=True)
    capital_investment_statement = models.FileField(default=NULL,upload_to='documents/%Y/%m/%d')

    EXTRA = (
    ('Whether any other activities are proposed to be undertaken? If so, in what fields?','Whether any other activities are proposed to be undertaken? If so, in what fields?'),
    ('Please state if you or your partner, if anyone have been convicted of an offence, if so please give details.', 'Please state if you or your partner, if anyone have been convicted of an offence, if so please give details.'),
    ('I/we hereby solemnly declare that all the particulars give above are correct','I/we hereby solemnly declare that all the particulars give above are correct'),
    ('I/we hereby solemnly declare that if a licence is granted to me/us, I/We will abide by the Travel Agencies Act, 1976 and the Rules made their under the terms of the licence granted to me/us, and the code of conduct.','I/we hereby solemnly declare that if a licence is granted to me/us, I/We will abide by the Travel Agencies Act, 1976 and the Rules made their under the terms of the licence granted to me/us, and the code of conduct.'),
)
    terms = MultiSelectField(choices=EXTRA , null=True) 

    def __str__(self):
        return self.guide_name


# class auditors(models.Model):
#     name_of_auditors = models.CharField(max_length=30, null=True)
#     address = models.CharField(max_length=100 , null=True)

# class staff(models.Model):
#     staff_category = models.CharField(max_length=30 , null=True)
#     purpose = models.CharField(max_length=30 , null=True)
#     qualification = models.CharField(max_length=30 , null=True)
#     year_of_experiance = models.IntegerField(null=True)


