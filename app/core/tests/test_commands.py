#imports the mock module, allows us to mock the django get DB funciton 
  #simulates DB being availble 
from unittest.mock import patch 
#allows us to use the call_command function in source code
from django.core.management import call_command 
#import operation error when DB is unavailable 
from django.db.utils import OperationalError 
from django.test import TestCase 

class CommandTests(TestCase): 
  
  def test_wait_for_db_ready(self):
    """Test waiting for db when db is available"""
    with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
      gi.return_value = True 
      call_command('wait_for_db')
      #checks that 'getitem' was called once
      self.assertEqual(gi.call_count, 1)
 
 #patch decorator: removes delay of testing the db with a while loop, essentially passes getitem(gi) as arg to test
  #replaces function of time .sleep, and just returns a True value. 
  @patch('time.sleep', return_value=True)
  def test_wait_for_db(self, ts):
    """Test waiting for db"""
    with patch ('django.db.utils.ConnectionHandler.__getitem__') as gi:
      #side effect: makes it raise operational error 5 times and get success on the 6th time. 
      gi.side_effect = [OperationalError] * 5 + [True]
      call_command('wait_for_db')
      self.assertEqual(gi.call_count, 6)
      #core/management/commands/wait_for_db.py