from django.test import TestCase
#Allows us to make test requests to our application in unit tests 
from django.test import Client 
from django.contrib.auth import get_user_model 
#Helper function 'reverse' allows urls to be generated for
  #django admin page.
from django.urls import reverse 

class AdminSiteTests(TestCase):

  #Test set-up to be run before every test
  def setUp(self):
      self.client = Client()
      self.admin_user = get_user_model().objects.create_superuser(
        email='admin@selflovereflection.com', 
        password='password123'
      )

      #'force_login' is a Client helper method that logs a user in with django authentication. 
        #don't have to manually log a user in.
      self.client.force_login(self.admin_user)
      self.user = get_user_model().objects.create_user(
        email = 'joker@gotham.com', 
        password = 'test123',
        name = 'Test user full name'
      )

  def test_users_listed(self):
    """Test that user are listed on user page"""
    #generates a url for our list user page in the app 'core'
      #allows for the test to work for any url because of reverse funciton. 
    url = reverse('admin:core_user_changelist')
    response = self.client.get(url)

    #assertContains is a django specific assertion that check it contains specific items.
      #also checks that response was 200, and looks into output/content of response.
    self.assertContains(response, self.user.name)
    self.assertContains(response, self.user.email)

    #must go to admin.py file to update contents.

  def test_user_change_page(self): 
    """The user edit page works"""
    url = reverse('admin:core_user_change', args = [self.user.id])
    #url = /admin/core/user/:user_id
    response = self.client.get(url)

    self.assertEqual(response.status_code, 200)
    #need to update field sets in admin.py to match our custom model, not the default model

  def test_create_user_page(self): 
    """Test the create user page works"""
    url = reverse('admin:core_user_add')
    response = self.client.get(url)

    self.assertEqual(response.status_code, 200)