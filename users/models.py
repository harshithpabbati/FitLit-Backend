from django.db import models
from django.contrib.auth.models import User

GENDER_OPTION = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Prefer not to say')
)


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_OPTION, max_length=1)
    height = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    dob = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "Profiles"
        verbose_name = "Profile"

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name