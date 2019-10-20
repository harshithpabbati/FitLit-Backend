from django.db import models
from django.contrib.auth.models import User


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(null=True)
    calcium = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    carbs = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    cholesterol = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    monounsaturated = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    polyunsaturated = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    saturated = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    fat = models.DecimalField(max_digits=5, decimal_places=3,null=True, blank=True)
    trans = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    iron = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    fiber = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    folate = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    potassium = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    magnesium = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    sodium = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    energy = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    niacin = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    phosphorus = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    protein = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    riboflavin = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    sugars = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    thiamin = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    vitaminE = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    vitaminA = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    vitaminB12 = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    vitaminB6 = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    vitaminC = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    vitaminD = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    vitaminK = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return user.first_name