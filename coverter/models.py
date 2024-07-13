from django.core.validators import MinValueValidator
from django.db import models


class Rate(models.Model):
    class Name(models.TextChoices):
        RUB = "RUB", "Рубли"
        USD = "USD", "Доллары"
        KZT = "KZT", "Тенге"

    short_name = models.CharField(max_length=3, verbose_name="Short Name", choices=Name.choices)
    rate_to_usd = models.FloatField(verbose_name="Rate To USD", validators=[MinValueValidator(0)])
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name = "Rate To USD"
        verbose_name_plural = "Rates To USD"
