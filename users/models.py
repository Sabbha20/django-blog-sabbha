from io import BytesIO
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
from django.core.files.storage import default_storage

GENDER_CATEGORY = (
    ('U','Undefined'),
    ('F','Female'),
    ('M','Male'),
    ('T','Transgender')
                    )
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birthdate = models.DateField(null=True,blank=True)
    gender = models.CharField(choices=GENDER_CATEGORY,max_length=2)
    bio = models.CharField(max_length=160,null=True,blank=True)
    photo = models.ImageField(upload_to='pics', default=os.path.join('pics', 'avatar.png'))
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # img = Image.open(self.photo.path)
        
        # if img.height > 200 or img.width > 200:
        #     img.thumbnail((200,200))
        #     img.save(self.photo.path)
        
        memfile = BytesIO()
        img = Image.open(self.photo)
        if img.height > 1000 or img.width > 1000:
            output_size = (200, 200)
            img.thumbnail(output_size, Image.ANTIALIAS)
            img.save(memfile, 'JPEG', quality = 95)
            default_storage.save(self.photo.name, memfile)
            memfile.close()
            img.close()
            
            
            
            