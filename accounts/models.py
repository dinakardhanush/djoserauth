from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin , BaseUserManager
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email,password=None,**extra_fields):
        if not email:
            raise ValueError('users must have email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        
        user.save()

        return user

    def create_superuser(self, email,password=None,**extra_fields):
        if not email:
            raise ValueError('users must have email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        
        user.save()

        return user  
    

class UserAccountModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255,default=None)
    bio = models.TextField(default=None)
    registered_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserAccountManager()
    is_brand = models.BooleanField(default=False)
    is_influencer = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    # is_phone_verified = models.BooleanField(default=False)    
    # passresettoken, emailresettoken

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['first_name']

    def get_full_name(self):
        return (self.first_name + " " + self.last_name) # Updated to actual full name
    
    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email


# This is the model for the influencer
# There can be multiple influencer accounts owned by a single user (One-to-Many relationship)
class InfluencerModel(models.Model):
    user = models.ForeignKey(UserAccountModel, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    domain = models.CharField(max_length=150)
    intro_ad_price = models.DecimalField(max_digits=20, decimal_places=2)
    review_ad_price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.account_name} (User ID: {self.user_id})"

# This is the model for the brand
# There can be multiple brand accounts owned by a single user (One-to-Many relationship)
class BrandModel(models.Model):
    user = models.ForeignKey(UserAccountModel, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=300)
    cin = models.CharField(max_length=40)
    gstin = models.CharField(max_length=40)
    address = models.TextField()
    designation = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand_name} (User ID: {self.user_id})"