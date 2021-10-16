from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Home(models.Model):
    name = models.CharField(max_length=264, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+8801865632882'. Up to 14 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.name



