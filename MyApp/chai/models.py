from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# write database model for varieties of chai 
class ChaiVariety(models.Model):
    # declare an enum to store types of chai
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)  
    description = models.TextField()
    
    # add this to display name of chai
    def __str__(self):
        return self.name

    