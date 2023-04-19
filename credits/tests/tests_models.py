from django.test import TestCase
from commons.models import Client
from credits.models import Bank, Credit


class CreditModelTest(TestCase):
    def setUp(self):
        self.bank = Bank.objects.create(name='Bank of America', btype='PRV')
        self.client = Client.objects.create(
            full_name='John Doe', birthdate='2000-01-01', years_old=23, nationality='USA', 
            address='123 Main St', email='johndoe@example.com', phone='555-1234', ptype='NTR', bank=self.bank)
        self.credit = Credit.objects.create(
            client=self.client, bank=self.bank, description='Car loan', 
            min_payment=1000, max_payment=2000, credit_term=60, ctype='AUTO')

    def test_credit_str(self):
        expected_str = "{} {}".format(self.client, self.bank)
        self.assertEqual(str(self.credit), expected_str)
