from django_countries.fields import CountryField
from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
from django_resized import ResizedImageField


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    #is_premium = models.BooleanField(default=False)


    def __str__(self):
        return self.email

    @property
    def profile_completion_percentage(self):
        complete = 0
        if self.first_name:
            complete += 5
        if self.last_name:
            complete += 5

        if self.profile.profile_pic:
            complete += 15

        if self.profile.phone_number:
            complete += 10
        
        return complete

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255, blank=True)
    e_mail = models.CharField(max_length=255, blank=True)
    profile_pic = ResizedImageField(size=[300, 300], quality=100, default="profile-pics/default.jpg", upload_to="profile-pics")
    sub_expires_on = models.DateTimeField(blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.email

