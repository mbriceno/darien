from django.test import TestCase
from datetime import date
from .models import Client
from credits.models import Bank


class ClientBankModelTest(TestCase):

    def setUp(self):
        self.bank = Bank.objects.create(name='Bank of America', btype='PRV', address='123 Main St.')
        self.client = Client.objects.create(full_name='John Doe', birthdate=date(2000, 1, 1), years_old=22,
                                             nationality='American', address='456 Maple St.', email='jdoe@example.com',
                                             phone='555-1234', ptype='NTR', bank=self.bank)

    def test_bank_str(self):
        self.assertEqual(str(self.bank), 'Bank of America')

    def test_client_str(self):
        self.assertEqual(str(self.client), 'John Doe')

    def test_client_age_calculation(self):
        today = date.today()
        expected_age = today.year - self.client.birthdate.year - ((today.month, today.day) < (self.client.birthdate.month, self.client.birthdate.day))
        self.assertEqual(self.client.years_old, expected_age)

    def test_client_birthdate_index(self):
        qs = Client.objects.filter(birthdate=date(2000, 1, 1))
        self.assertIn(self.client, qs)


    def test_client_nationality_blank_null(self):
        client_no_nat = Client.objects.create(full_name='Jane Smith', birthdate=date(2001, 2, 2), years_old=21,
                                               address='789 Oak St.', email='jsmith@example.com', ptype='JRD', bank=self.bank)
        self.assertEqual(client_no_nat.nationality, None)
