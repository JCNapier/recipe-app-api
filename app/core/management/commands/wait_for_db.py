#built in python module
import time 
#django module we can use to test if db connection is available
from django.db import connections 
#operaitonal error django throws if db is unavailable 
from django.db.utils import OperationalError
#class we build on to create custom command 
from django.core.management.base import BaseCommand 

class Command(BaseCommand):
  """django command to pause execution until databse is available"""

  #handle function run when we use the management command 
  def handle(self, *args, **options):
    self.stdout.write('Waiting for database...')#outputs message to user
    db_conn = None 
    #while db_conn is falsey, try to set db_conn to the database connection. 
      #If django raises operational error we catch it and output our message, and tries again until db is available. 
    while not db_conn:
      try:
        db_conn = connections['default']
      except OperationalError:
        self.stdout.write('Database Unavailable, waiting 1 ssecond...')
        time.sleep(1)
    
    self.stdout.write(self.style.SUCCESS('Database available!'))#style displays message in green. 