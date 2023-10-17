from django.test import SimpleTestCase
from django.urls import reverse, resolve
from webadmin.views import index, rooms,teams,users, test_example, SplitIds, ReplaceCommas


class TestExamples(SimpleTestCase):


    #URLs
    def test_index(self):

        url = reverse("index")   
        self.assertEquals(resolve(url).func, index)

    def test_rooms(self):

        url = reverse("rooms")   
        self.assertEquals(resolve(url).func, rooms)

    def test_teams(self):

        url = reverse("teams")   
        self.assertEquals(resolve(url).func, teams)

    def test_users(self):

        url = reverse("users")   
        self.assertEquals(resolve(url).func, users)

    def test_example(self):

        url = reverse("example")   
        self.assertEquals(resolve(url).func, test_example)

    #Methods
    def test_SplitIds(self):

        result = SplitIds("1,2,3,4,5")
        item = [{"id" : 1,}, { "id" : 2, }, { "id" : 3, }, { "id" : 4, }, { "id" : 5, }]

        self.assertEquals(result,item) 
    
    def test_ReplaceCommas(self):
        
        result = ReplaceCommas("1,2,3,4,5,")
        item = "1,2,3,4,5"

        self.assertEquals(result,item)