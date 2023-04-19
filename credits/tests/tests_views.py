from django.test import TestCase, Client as ClientRequest
from django.urls import reverse
from django.utils import timezone
from commons.models import Client
from credits.models import Bank, Credit


class CreditCreateViewTestCase(TestCase):
    def setUp(self):
        self.request = ClientRequest()
        self.bank = Bank.objects.create(name="Test Bank", address="123 Main St.")
        self.client = Client.objects.create(
            full_name="John Doe",
            birthdate=timezone.now().date(),
            years_old=30,
            email="johndoe@example.com",
            phone="123-456-7890",
            ptype="NTR",
            bank=self.bank
        )

    def test_credit_create_view(self):
        url = reverse("credit_create")
        data = {
            "client": self.client.pk,
            "bank": self.bank.pk,
            "description": "Test description",
            "credit_amount": "200000",
            "min_payment": "100.00",
            "max_payment": "500.00",
            "credit_term": "12",
            "ctype": "AUTO",
        }
        response = self.request.post(url, data)
        self.assertEqual(response.status_code, 302)  # Check for successful redirect
        self.assertEqual(Credit.objects.count(), 1)  # Check that one Credit was created


class CreditDeleteViewTest(TestCase):
    def setUp(self):
        self.request = ClientRequest()
        self.bank = Bank.objects.create(name="Test Bank", address="123 Main St.")
        self.client = Client.objects.create(
            full_name="John Doe",
            birthdate=timezone.now().date(),
            years_old=30,
            email="johndoe@example.com",
            phone="123-456-7890",
            ptype="NTR",
            bank=self.bank
        )
        self.credit = Credit.objects.create(
            client=self.client,
            bank=self.bank,
            description="Test credit",
            credit_amount=200000,
            min_payment=100,
            max_payment=1000,
            credit_term=12,
            ctype='AUTO'
        )
        self.url = reverse('credit_delete', kwargs={'pk': self.credit.pk})

    def test_credit_delete_view(self):
        response = self.request.delete(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Credit.objects.filter(pk=self.credit.pk).exists())
