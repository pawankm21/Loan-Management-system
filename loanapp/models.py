from os import name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from django.db.models.manager import Manager
from django.utils import timezone
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    income = models.IntegerField()
    address = models.CharField(max_length=1000)
    account_number=models.IntegerField()
    balance=models.DecimalField( max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Loan(models.Model):
    # class ApprovedLoans(models.manager):
    #     def get_queryset(self):
    #         return super().get_queryset() .filter(status='APPROVED')
    # class NewLoans(models.manager):
    #     def get_queryset(self):
    #         return super().get_queryset() .filter(status='NEW')
    # class RejectedLoans(models.manager):
    #     def get_queryset(self):
    #         return super().get_queryset() .filter(status='REJECTED')
    # approved=ApprovedLoans()
    # rejected=RejectedLoans()
    # new=NewLoans()
    STATUS = [
        ('NEW', 'NEW'),
        ('APPROVED', 'APPROVED'),
        ('REJECTED', 'REJECTED'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    agent = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.CharField(choices=STATUS, max_length=200, default='NEW')
    interest_rate = models.DecimalField(max_digits=8, decimal_places=2)
    loan_amount = models.IntegerField()
    tenure_in_months = models.IntegerField()
    date_given = None
    till_date_given = None

    def __str__(self):
        return f'{self.customer.name}-{self.tenure_in_months}'


class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    loan = models.ForeignKey(Loan, on_delete=models.PROTECT)
    amount_paid = models.IntegerField()
    payment_date = models.DateTimeField(default=timezone.now)
    remarks = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.customer}-{self.payment_date}'

