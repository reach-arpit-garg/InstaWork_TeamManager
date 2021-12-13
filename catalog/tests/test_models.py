from django.test import TestCase

from catalog.models import Member

class MemberModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Member.objects.create(first_name='Big', last_name='Bob', email_address='BigBob@gmail.com', phone_number='123456', role='r')
        Member.objects.create(first_name='Small', last_name='Bob', email_address='SmallBob@gmail.com', phone_number='123456', role='a')
        
    def test_first_name_value(self):
        member = Member.objects.all()
        field_value = member[0].first_name
        self.assertEqual(field_value, 'Big')
        
    def test_last_name_value(self):
        member = Member.objects.all()
        field_value = member[0].last_name
        self.assertEqual(field_value, 'Bob')

    def test_email_address_value(self):
        member = Member.objects.all()
        field_value = member[0].email_address
        self.assertEqual(field_value, 'BigBob@gmail.com')
        
    def test_phone_number_value(self):
        member = Member.objects.all()
        field_value = member[0].phone_number
        self.assertEqual(field_value, '123456')
        
    def test_role_value(self):
        member = Member.objects.all()
        field_value = member[0].role
        self.assertEqual(field_value, 'r')

    def test_first_name_label(self):
        member = Member.objects.all()
        field_label = member[0]._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')
        
    def test_last_name_label(self):
        member = Member.objects.all()
        field_label = member[0]._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_email_address_label(self):
        member = Member.objects.all()
        field_label = member[0]._meta.get_field('email_address').verbose_name
        self.assertEqual(field_label, 'email address')
        
    def test_phone_number_label(self):
        member = Member.objects.all()
        field_label = member[0]._meta.get_field('phone_number').verbose_name
        self.assertEqual(field_label, 'phone number')
        
    def test_role_label(self):
        member = Member.objects.all()
        field_label = member[0]._meta.get_field('role').verbose_name
        self.assertEqual(field_label, 'role')

    def test_object_name_is_id(self):
        member = Member.objects.all()
        expected_object_name = f'{member[0].id}'
        self.assertEqual(str(member[0]), expected_object_name)
        
    def test_object_count(self):
        num_member = Member.objects.all().count()
        self.assertEqual(2, num_member)
        
    def test_objects_are_unique(self):
        member = Member.objects.all()
        self.assertNotEqual(member[0].id, member[1].id)