from django.db.models import fields
from rest_framework import serializers
from loanapp.models import Loan,Payment,Customer,User

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model =Loan
        fields=[
            'id',
            'customer',
            'agent',
            'status',
            'interest_rate', 
            'date_given',
            'till_date_given',
            'loan_amount',
            'tenure_in_months',
            'objects' ,
        ]

