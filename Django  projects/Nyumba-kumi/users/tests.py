from django.test import TestCase
from .models import Neighbourhood, Business

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
          self.new_neighbourhood = Neighbourhood( name='west', location='langata', health_dept= '911', police_dept= '911', logo= 'random.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighbourhood, Neighbourhood))

    def tearDown(self):
      Neighbourhood.objects.filter(id=1).delete()

    def test_create_neighbourhd(self):
        self.new_neighbourhood.create_neighbourhd()
        self.assertTrue(len(Neighbourhood.objects.all())>0)

    def test_delete_neighbourhd(self):
        self.new_neighbourhood.delete_neighbourhd(1)
        self.assertTrue(len(Neighbourhood.objects.all()) == 0)

    def test_find_neighbourhd(self):
        self.new_neighbourhood.create_neighbourhd()
        self.assertTrue(len(Neighbourhood.objects.filter(id=1)) == 1)

    def test_update_neighbourhd(self):
        self.new_neighbourhood.create_neighbourhd()
        pass

class BusinessTestClass(TestCase):
    def setUp(self):
          self.new_business = Business( name='smokie pasua', description='street food', Neighbourhood=1, owner= 1, email= 'smokiepasua@gmail.com', logo= 'random.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business, Business))

    def tearDown(self):
        Business.objects.filter(id=1).delete()

    def test_create_business(self):
        self.new_business.create_busn()
        self.assertTrue(len(Business.objects.all())>0)

    def test_delete_business(self):
        self.new_business.delete_busn(1)
        self.assertTrue(len(Business.objects.all()) == 0)

    def test_find_business(self):
        self.new_business.create_busn()
        self.assertTrue(len(Business.objects.filter(id=1)) == 1)

    def test_update_business(self):
        pass
      