  #TestCase is a built in class in Django that has helper functions to help test code. 
from django.test import TestCase 
  #get user model is a built in django function
from django.contrib.auth import get_user_model 


class ModelTests(TestCase): 

  def test_create_user_with_email_successful(self):
    """Test creating a new user with an email is successful"""
    email = 'test@selflovereflection.com'
    password = 'Testpass123'
    user = get_user_model().objects.create_user(
      email=email, 
      password=password
    )

    self.assertEqual(user.email, email)
    #check password is included in the Django user model and checks for a correct password. 
    self.assertTrue(user.check_password(password))

  def test_new_user_email_normalized(self):
    """Test the email for a new user us normalized"""
    email = 'test@SELFLOVEREFLECTION.com'
    user = get_user_model().objects.create_user(email, 'test123')

    self.assertEqual(user.email, email.lower())

  def test_new_user_invlaid_email(self): 
    """Test creating user with no email raises error"""
    #This test will only pass if this error is raised. 
    with self.assertRaises(ValueError):
      get_user_model().objects.create_user(None, 'test123')

  def test_create_new_superuser(self):
    """Creating a new superuser"""
    user = get_user_model().objects.create_superuser(
      'test@selflovereflection.com',
      'test123'
    )

    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)

