from django.db import models
#extends django user model functionality 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin

class UserManager(BaseUserManager):
  
  #extra fields takes what arguments aside from self that are passed in,
    #and creates new fields for them in the model. 
  #self.normalize_email is a function to lowercase all emails 
  def create_user(self, email, password=None, **extra_fields):
    """Creates and saves a new user"""
    if not email:
      raise ValueError('Users must have an email address')
    user = self.model(email=self.normalize_email(email), **extra_fields)
    #set password is built in django functionality that encrypts the password passed in. 
    user.set_password(password)
    #self.db is required for using multiple databases. 
    user.save(using=self._db)

    return user 

  def create_superuser(self, email, password):
    """Creates and saves a new super user"""
    user = self.create_user(email, password)
    user.is_staff = True 
    user.is_superuser = True
    user.save(using=self._db)

    return user 

  #Provides access to built django USER functionality to build upon
class User(AbstractBaseUser, PermissionsMixin):
  """Custom user model that supports using email instead of username"""
  #define fields of our database model. 
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserManager()

  #allows us to use an email address for a user name
  USERNAME_FIELD = 'email'

  #Add AUTH_USER_MODEL to settings.py