from django.test import TestCase

from catalog.models import Member

class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Member.objects.create(first_name='Big', last_name='Bob', email_address='BigBob@gmail.com', phone_number='123456', role='r')
        Member.objects.create(first_name='Small', last_name='Bob', email_address='SmallBob@gmail.com', phone_number='123456', role='a')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        
    def test_view_url_exists_for_member(self):
        member = Member.objects.all()
        response = self.client.get('/users/member/'+str(member[0].id))
        self.assertEqual(response.status_code, 200)
        
    def test_add_url_exists_at_desired_location(self):
        response = self.client.get('/users/addMember/')
        self.assertEqual(response.status_code, 200)