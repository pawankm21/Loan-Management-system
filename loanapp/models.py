from os import name
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.db.models.manager import Manager
from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


# models

class Customer(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254,unique=True)
    address = models.CharField(max_length=1000)
    account_number = models.IntegerField(unique=True)

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
    interest_rate = models.DecimalField(max_digits=18, decimal_places=3)
    loan_amount = models.DecimalField(max_digits=18, decimal_places=3)
    tenure = models.IntegerField(verbose_name='tenure in months')
    on_date_issued = models.DateTimeField(blank=True, null=True)
    last_payment = models.DateTimeField(blank=True, null=True,verbose_name='recent payment')
    
    def instalment_amount(self):
        p=self.loan_amount
        i=self.interest_rate
        n=self.tenure
        emi=((p*i)*((i/12+1)*n))/((12*(1+(i/12))*n)-1)
        return round(emi,2)

    def number_of_payments(self):
        number_of_payment=self.payment_set.count()
        return number_of_payment

    def pending_instalments(self):
        difference=(datetime.now()-self.on_date_issued)/timedelta(days=30.4)
        return max(0,int(difference)-self.number_of_payments())
        
    def next_instalment_deadline(self):
        self.last_payment+timedelta(days=1)*30

    def __str__(self):
        return f'{self.customer.name}-{self.tenure}'


class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    loan = models.ForeignKey(Loan, on_delete=models.PROTECT)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=3)
    payment_date = models.DateTimeField(default=timezone.now)
    remarks = models.CharField(max_length=1000)
    @property
    def validate(self):
        if self.loan.status != 'APPROVED':
            raise ValueError("Loan is not approved")
        elif self.loan.instalment_amount() != self.amount_paid:
            raise ValueError(
                f"Please pay exact ₹{self.loan.instalment_amount()}")
        elif self.loan.last_payment is not None and self.payment_date < self.loan.last_payment+timedelta(days=1)*30:
            raise ValueError("Only one payment is possible in a month")

        return True
        
    def __str__(self):
        return f'{self.customer}-{self.payment_date}'


# signals

@receiver(post_save, sender=Payment)
def last_payment_reciever(instance, created, *args, **kwargs):
    print(created)
    if instance.validate:
        Loan.objects.filter(pk=instance.loan.id).update(last_payment=datetime.now())

@receiver(post_save, sender=Loan)
def approved_date_reciever(instance,*args, **kwargs):
    if instance.status=='APPROVED' and instance.on_date_issued==None:
        Loan.objects.filter(pk=instance.id).update(on_date_issued=datetime.now())
    Loan.objects.get(pk=instance.id).pending_instalments()

