from django.db.models import fields
from rest_framework import serializers
from loanapp.models import Loan, Payment, Customer, User


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = [
            'id',
            'customer',
            'agent',
            'status',
            'interest_rate',
            'on_date_issued',
            'loan_amount',
            'tenure',
            'last_payment',
        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'name',
            'email',
            'address',
            'account_number'
        
        ]
