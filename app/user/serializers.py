from django.contrib.auth import get_user_model 

from rest_framework import serializers 


class UserSerializer(serializers.ModelSerializer):
  """Serializer for the users object"""

  class Meta: 
    model = get_user_model()
    #class variable that points to serializer 
    fields = ('email', 'password', 'name')  
    #sets extra restrictions for desired fiels, in this case 'password'
    extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

  def create(self, validated_data):
    #validated data is the JSON response being passed to create a user. 
      #**validated_data unpackages JSON
    """Create a new user with encrypted password and return it"""
    return get_user_model().objects.create_user(**validated_data)