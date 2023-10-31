from django.db import models
from django.contrib.auth.models import AbstractUser

USER_ROLE = [
    ('mentee',"Mentee"),
    ("mentor","Mentor"),
    ("admin","Admin")
]
STATUS = [
    ("verified",'Verified'),
    ('not_verified','Non_Veried')
]
class Users(AbstractUser):
    role = models.CharField(choices=USER_ROLE,default='mentee',max_length=20)
    phone  = models.CharField(max_length=20, unique=True)
    status = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = ['email','phone']    
    def __str__(self):
        return self.username
    
class Code(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    code = models.IntegerField()
