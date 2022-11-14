from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class OrganizationUser(models.Model):

    LEADER = 'LR'
    MEMBER = 'MEM'
    INTERN = 'IN'
    ORGUSER_POSITION_CHOICES = [
        (LEADER, 'Lead'),
        (MEMBER, 'member'),
        (INTERN, 'intern'),
    ]
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(
        max_length=3, choices=ORGUSER_POSITION_CHOICES, default=MEMBER
    )
    leader = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    role = models.CharField(max_length=999) # list of responsibilities stores as json string

class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    subportfolio = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
