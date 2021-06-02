from datetime import date, datetime, timezone
from rest_framework import generics
from loanapp.models import Loan, Customer, Payment, User
from .serializers import LoanSerializer,CustomerSerializer,PaymentSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class LoanList(generics.ListAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class CustomerList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class PaymentList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer


