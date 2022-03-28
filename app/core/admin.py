#import django default user admin, to support custom user admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#converts strings to human readable text, so it gets passed through the translation engine.
  #Translation engin converts code to other languages
from django.utils.translation import gettext as _
from core import models 


class UserAdmin(BaseUserAdmin):
  #this will list user by email and name, but order them by id
  ordering = ['id']
  list_display = ['email', 'name']
  #None in this case is the title of the section of the form/page
  fieldsets = (
      (None, {'fields': ('email', 'password')}),
      (_('Person Info'), {'fields': ('name',)}), #must add comma for single field i.e. ('name',) or it will break
      (_('Permissions'),
        {'fields': ('is_active', 'is_staff', 'is_superuser')}
      ),
      (_('Important dates'), {'fields': ('last_login',)})
  )
  add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'password1', 'password2')
    }),
  )

admin.site.register(models.User, UserAdmin)

