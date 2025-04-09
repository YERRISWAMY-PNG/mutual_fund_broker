from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import FundHouse, MutualFund, UserPortfolio

User = get_user_model()


class MutualFundTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            username='testuser'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.fund_house = FundHouse.objects.create(
            name='Test Fund House',
            code='TFH'
        )

        self.mutual_fund = MutualFund.objects.create(
            scheme_code='TEST123',
            scheme_name='Test Fund',
            fund_house=self.fund_house,
            is_open_ended=True,
            nav=100.50
        )

    def test_get_fund_houses(self):
        url = reverse('fund-houses')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_mutual_funds(self):
        url = reverse('mutual-funds') + f'?fund_house={self.fund_house.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_portfolio_operations(self):
        # Create
        url = reverse('portfolio-list')
        data = {
            'mutual_fund': self.mutual_fund.id,
            'units': 10,
            'purchase_nav': 100.50
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # List
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # Detail
        detail_url = reverse('portfolio-detail', kwargs={'pk': response.data[0]['id']})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(response.data['units']), 10.0)

        # Update
        update_data = {'units': 15}
        response = self.client.patch(detail_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(response.data['units']), 15.0)

        # Delete
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)