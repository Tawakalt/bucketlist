from .models import Bucketlist
from django.core.exceptions import ValidationError


def validate_cost(self):
        if self.cost > 100:
            return ValidationError("Cost shouldn't be greater than 100")
