from rest_framework import serializers
from .models import FundHouse, MutualFund, UserPortfolio


class FundHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundHouse
        fields = '__all__'


class MutualFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = MutualFund
        fields = '__all__'


class UserPortfolioSerializer(serializers.ModelSerializer):
    mutual_fund = MutualFundSerializer(read_only=True)
    current_value = serializers.SerializerMethodField()
    investment_value = serializers.SerializerMethodField()
    gain_loss = serializers.SerializerMethodField()

    class Meta:
        model = UserPortfolio
        fields = '__all__'
        read_only_fields = ('purchase_date', 'purchase_nav')

    def get_current_value(self, obj):
        return obj.current_value

    def get_investment_value(self, obj):
        return obj.investment_value

    def get_gain_loss(self, obj):
        return obj.gain_loss