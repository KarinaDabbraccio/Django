from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    '''
    Choices for 'user_group' to identify users as 
    either basic user or Manager who has additional access rights
    '''
    USER_TYPE = [
        ('U', 'User'),
        ('M', 'Manager')
    ]
    
    username = models.OneToOneField(User, default='U', on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='images/users', null=True, default = 'null')
    user_group = models.CharField(max_length=1, choices=USER_TYPE)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(username=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    
    '''
    Displays info in admin page
    '''
    def __str__(self) -> str:
        return '{username} - {user_type}'.format(username=self.username, user_type=self.user_group)