from django.db import models
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(blank=True)

    profile_pic = models.ImageField(upload_to="profile-pic/", blank=True)

    def __str__(self):

        return self.user.username


# Create Profile when creating a User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save Profile when saving a User
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


#creating a choice table to allow be landlords or tenants
class Landlord_tenant(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    choice=models.IntegerField()


#List of all houses models
class House(models.Model):
    house_name=models.CharField(max_length=15)
    landing_pic=models.ImageField(upload_to="profile-pic/", blank=False)
    room_one=models.ImageField(upload_to="profile-pic/", blank=False)
    room_two=models.ImageField(upload_to="profile-pic/", blank=False)
    room_three=models.ImageField(upload_to="profile-pic/", blank=False)
    room_three=models.ImageField(upload_to="profile-pic/", blank=False)
    room_four=models.ImageField(upload_to="profile-pic/", blank=False)
    room_five=models.ImageField(upload_to="profile-pic/", blank=False)
    roomsix=models.ImageField(upload_to="profile-pic/", blank=False)
    room_seven=models.ImageField(upload_to="profile-pic/", blank=False)
    room_eigth=models.ImageField(upload_to="profile-pic/", blank=False)
    room_nine=models.ImageField(upload_to="profile-pic/", blank=False)
    room_ten=models.ImageField(upload_to="profile-pic/", blank=False)
    room_eleven=models.ImageField(upload_to="profile-pic/", blank=False)
    room_twelve=models.ImageField(upload_to="profile-pic/", blank=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
