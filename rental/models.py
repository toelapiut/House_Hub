from django.db import models
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='rider_profile', unique=True)
    picture = models.ImageField(upload_to='user_pics/', blank=True)
    phone =models.CharField(max_length=30,blank=True)
    bio = models.CharField(max_length=500, blank=True)
    username=models.CharField(max_length=12,blank=True)


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)


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
    user=models.ForeignKey(User,on_delete=models.CASCADE)

#house photo models
class Room(models.Model):
    room_pic=models.ImageField(upload_to="profile-pic/", blank=False)
    house=models.ForeignKey(House,on_delete=models.CASCADE)


class Comment(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    comment_content = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_post_comments(cls,post_id):

        post_comments = Comment.objects.filter(post=post_id)

        return post_comments



class Post(models.Model):
    post_comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return post_comment


class Like(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    likes_number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_post_likes(cls,post_id):

        post_likes = Like.objects.filter(post=post_id)

        return post_likes

    @classmethod
    def num_likes(cls,post_id):

        post = Like.objects.filter(post=post_id)
        found_likes = post.aggregate(Sum('likes_number')).get('likes_number__sum',0)

        return found_likes

