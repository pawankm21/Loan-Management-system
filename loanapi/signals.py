from django.db.models.signals import post_save
from django.dispatch import receiver
from loanapp.models import Loan
from datetime import datetime, time, timedelta
from django.utils import timezone



@receiver(post_save, sender=Loan)
def loan_date_starts(sender,instance,*args,**kwargs):
    if instance.status=='APPROVED':
        instance.date_given=timezone.now

    




