from django.urls import path
from .views import (
    FundHouseListView,
    MutualFundListView,
    UserPortfolioListView,
    UserPortfolioDetailView
)

urlpatterns = [
    path('fund-houses/', FundHouseListView.as_view(), name='fund-houses'),
    path('mutual-funds/', MutualFundListView.as_view(), name='mutual-funds'),
    path('portfolio/', UserPortfolioListView.as_view(), name='portfolio-list'),
    path('portfolio/<int:pk>/', UserPortfolioDetailView.as_view(), name='portfolio-detail'),
]