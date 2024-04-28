from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Discount(models.Model):
    description = models.TextField(blank=True, null=True)
    value = models.DecimalField(max_digits=3, decimal_places=2,
                                validators=[MinValueValidator(0, message="Discount can not be lower than zero"),
                                            MaxValueValidator(1, message="Discount can not be higher than 100")]
                                )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_at = models.DateTimeField(default=timezone.now)
    end_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{int(self.value * 100)} % - {self.description[:5]}..."
