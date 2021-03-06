from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse 

#framework tools from rest 
  #test client to use request to API and check response 
from rest_framework.test import APIClient
from rest_framework import status 


#creates constant URL for all tests
  #creates user create url
CREATE_USER_URL = reverse('user:create')

#helper function for creating a user to be called in tests. 
#**param indicates a dynamic list being passed 
def create_user(**params):
  return get_user_model().objects.create_user(**params)

#public api is NOT an authenticated api
class PublicUserApiTests(TestCase):
  """Test the users API (public)"""

  def setUp(self): 
    self.client = APIClient()

  def test_create_valid_user_success(self):
    """Test creating user with valid payload is successful"""
    payload = {
      'email': 'test@music.com',
      'password': 'testpass', 
      'name': 'Test name'
    }

    response = self.client.post(CREATE_USER_URL, payload)

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    user = get_user_model().objects.get(**response.data)
    self.assertTrue(user.check_password(payload['password']))

    self.assertNotIn('password', response.data)

  def test_user_already_exists(self):
    """Test creating a user that already exists fails"""
    payload = {'email': 'test@music.com', 'password': 'testpass'}
    create_user(**payload)

    response = self.client.post(CREATE_USER_URL, payload)

    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_password_too_short(self):
    """Test that the password must be more than 5 characters"""
    payload = {'email': 'test@music.com', 'password': 'pw', 'name': 'Test',} 
    response = self.client.post(CREATE_USER_URL, payload)

    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    user_exists = get_user_model().objects.filter(
      email = payload['email']
    ).exists()

    self.assertFalse(user_exists)