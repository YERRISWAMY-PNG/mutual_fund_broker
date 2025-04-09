from django.db import models
from users.models import User


class FundHouse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class MutualFund(models.Model):
    scheme_code = models.CharField(max_length=20, unique=True)
    scheme_name = models.CharField(max_length=255)
    fund_house = models.ForeignKey(FundHouse, on_delete=models.CASCADE)
    is_open_ended = models.BooleanField(default=True)
    nav = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.scheme_name} ({self.scheme_code})"


class UserPortfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mutual_fund = models.ForeignKey(MutualFund, on_delete=models.CASCADE)
    units = models.DecimalField(max_digits=15, decimal_places=4)
    purchase_date = models.DateField(auto_now_add=True)
    purchase_nav = models.DecimalField(max_digits=10, decimal_places=4)

    @property
    def current_value(self):
        if self.mutual_fund.nav:
            return round(float(self.units) * float(self.mutual_fund.nav), 2)
        return None

    @property
    def investment_value(self):
        return round(float(self.units) * float(self.purchase_nav), 2)

    @property
    def gain_loss(self):
        if self.current_value:
            return round(self.current_value - self.investment_value, 2)
        return None

    def __str__(self):
        return f"{self.user.username} - {self.mutual_fund.scheme_name}"