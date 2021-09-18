from django.test import TestCase
from .models import Profile

class ProfileTestCase(TestCase):
    def setUp(self):
        self.joy=Profile(bio = 'Hello World')

    def test_instance(self):
        self.assertTrue(isinstance(self.joy.Profile))
    
    def test_save_method(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)