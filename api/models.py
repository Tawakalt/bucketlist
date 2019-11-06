from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.core.exceptions import ValidationError


# Create your models here.

class Category(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=25, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


def validate_cost(value):
    print(value)
    if value > 100.00:
        raise ValidationError("Cost shouldn't be greater than 100")



class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='bucketlists')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cost = models.DecimalField(decimal_places=2, max_digits=5, null=True, validators=[validate_cost])
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)




# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
