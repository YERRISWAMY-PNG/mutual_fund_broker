import requests
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from .models import FundHouse, MutualFund, UserPortfolio
from .serializers import FundHouseSerializer, MutualFundSerializer, UserPortfolioSerializer


class FundHouseListView(generics.ListAPIView):
    queryset = FundHouse.objects.all()
    serializer_class = FundHouseSerializer
    permission_classes = [IsAuthenticated]


class MutualFundListView(generics.ListAPIView):
    serializer_class = MutualFundSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        fund_house_id = self.request.query_params.get('fund_house')
        queryset = MutualFund.objects.filter(is_open_ended=True)

        if fund_house_id:
            queryset = queryset.filter(fund_house_id=fund_house_id)

        return queryset

    def list(self, request, *args, **kwargs):
        # First check if we have data in DB
        queryset = self.get_queryset()

        if not queryset.exists():
            # Fetch from RapidAPI if no data in DB
            fund_house_id = request.query_params.get('fund_house')
            if fund_house_id:
                try:
                    fund_house = FundHouse.objects.get(id=fund_house_id)
                    self.fetch_mutual_funds_from_api(fund_house)
                    queryset = self.get_queryset()
                except FundHouse.DoesNotExist:
                    return Response(
                        {'error': 'Fund house not found'},
                        status=status.HTTP_404_NOT_FOUND
                    )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def fetch_mutual_funds_from_api(self, fund_house):
        url = settings.RAPIDAPI_MF_URL
        headers = {
            'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
            'X-RapidAPI-Host': settings.RAPIDAPI_HOST
        }
        params = {'fund_house': fund_house.name}

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()

            for item in data:
                # Only save open-ended funds
                if item.get('scheme_type', '').lower() == 'open-ended':
                    MutualFund.objects.update_or_create(
                        scheme_code=item['scheme_code'],
                        defaults={
                            'scheme_name': item['scheme_name'],
                            'fund_house': fund_house,
                            'is_open_ended': True,
                            'nav': item.get('nav'),
                            'date': item.get('date')
                        }
                    )


class UserPortfolioListView(generics.ListCreateAPIView):
    serializer_class = UserPortfolioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserPortfolio.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserPortfolioDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserPortfolioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserPortfolio.objects.filter(user=self.request.user)