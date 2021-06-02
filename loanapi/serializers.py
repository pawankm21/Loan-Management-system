from django.db import models
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
                  'loan_amount',
                  'tenure',
                  'on_date_issued',
                  'last_payment', 
                  'instalment_amount',
                  'pending_instalments',
                  'number_of_payments'
                  ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
