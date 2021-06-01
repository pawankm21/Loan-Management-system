from datetime import date, datetime, timezone
from rest_framework import generics
from loanapp.models import Loan, Customer, Payment, User
from .serializers import LoanSerializer


class LoanList(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
