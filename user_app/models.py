from django.db import models
from django.utils import timezone
from user_app.manager import UserManager
from django.contrib.auth.models import User,AbstractBaseUser,AbstractUser
from django.contrib.auth.models import PermissionsMixin
from complain_app.models import Organization,Department
# Create your models here.
class CustomUser(AbstractUser):

    options = (
        ('user', 'user'),
        ('staff', 'staff'),
        ('admin', 'admin'),
    )
    email = models.CharField(max_length=150,unique=True)
    phone = models.CharField(max_length=15,unique=True)
    otp = models.CharField(max_length=6,default='12345')
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS=[]
    objects = UserManager()
    user_type = models.CharField(max_length=150, default='user', choices=options)
    username = None
    class Meta:
        db_table = 'user'



class StaffUser(models.Model):
        fk_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        fk_organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
        fk_department = models.ForeignKey(Department, on_delete=models.CASCADE)
        name = models.CharField(max_length=100)
        address = models.CharField(max_length=100)
        designation = models.CharField(max_length=100)
        image = models.ImageField(upload_to='staff_image/', null=True, blank=True)
        employee_id = models.CharField(max_length=100)
        work_location = models.CharField(max_length=100)

        class Meta:
            verbose_name_plural = "Staff Users"
            db_table = "staff_user"