from django.contrib import admin
from .models import Loan, Customer, Payment, User


# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('customer',
                    'loan',
                    'amount_paid',
                    'payment_date',
                    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
    )


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'agent',
        'status',
        'loan_amount',
        'on_date_approved',
    )
