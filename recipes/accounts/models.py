from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from PIL import Image

class Profile(models.Model):
    '''
    Choices for 'user_group' to identify users as either 
        basic user or Manager who has additional access rights
    User_discount : may apply to get discount, if ordered over certain 
        amount total. 
    '''
    USER_TYPE = [
        ('U', 'User'),
        ('M', 'Manager')
    ]
    
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='images/users', default = 'default.jpg')
    user_group = models.CharField(max_length=1, default = 'U', choices=USER_TYPE)
    user_discount = models.PositiveSmallIntegerField(default = 0);
    
    # Override the save method of the model
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.pic.path) # Open image
        
        # resize image
        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size) # Resize image
            img.save(self.pic.path) # Save it again and override the larger image
    

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