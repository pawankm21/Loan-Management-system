from os import name
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.db.models.manager import Manager
from django.utils import timezone
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver


# models

class Customer(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=1000)
    account_number = models.IntegerField()

    def __str__(self):
        return self.name


class Loan(models.Model):
    STATUS = [
        ('NEW', 'NEW'),
        ('APPROVED', 'APPROVED'),
        ('REJECTED', 'REJECTED'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    agent = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.CharField(choices=STATUS, max_length=200, default='NEW')
    interest_rate = models.DecimalField(max_digits=12, decimal_places=3)
    loan_amount = models.IntegerField()
    tenure = models.IntegerField()
    on_date_approved = models.DateTimeField(blank=True, null=True)
    last_payment = models.DateTimeField(blank=True, null=True)
    

    def __str__(self):
        return f'{self.customer.name}-{self.tenure_in_months}'


class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    loan = models.ForeignKey(Loan, on_delete=models.PROTECT)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=3)
    payment_date = models.DateTimeField(default=timezone.now)
    remarks = models.CharField(max_length=1000)
 
    def __str__(self):
        return f'{self.customer}-{self.payment_date}'


# signals

