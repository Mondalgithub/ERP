from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomManager, Gender, Room, Block, Sharing
# Create your models here.



class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=50)
    email = models.EmailField('email_address', unique=True)
    USN = models.CharField(max_length=11)
    course = models.CharField(max_length=50, default=None, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True, blank=True)
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, default = None, blank=True)
    block_name = models.ForeignKey(Block, on_delete=models.CASCADE, null=True, default =None, blank=True)
    sharing = models.ForeignKey(Sharing, on_delete=models.CASCADE, null=True, default = None, blank=True)
    mother_name = models.CharField(max_length=50, default=None,null=True, blank=True)
    father_name = models.CharField(max_length=50, default=None,null=True, blank=True)
    contact = models.CharField(max_length=10, default=None, blank=True, null=True)
    mother_contact = models.CharField(max_length=10, default=None, null=True, blank=True)
    father_contact = models.CharField(max_length=10, default=None, null=True, blank=True)
    
    
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomManager()
    

    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.email
    


CustomUser()

class LeaveRequest(models.Model):
    name = models.CharField(max_length=100)
    reason = models.TextField()
    contact_details = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {'Accepted' if self.is_accepted else 'Pending'}"