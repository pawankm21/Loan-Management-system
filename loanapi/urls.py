from django.urls import path

from .views import LoanList, LoanDetail,CustomerList,CustomerDetail, PaymentDetail, PaymentList,PaymentDetail

app_name = 'loanapi'
urlpatterns = [
    path('api/loan/', LoanList.as_view(), name='loancreate'),
    path('api/loan/<int:pk>/', LoanDetail.as_view(), name="loandetailcreate"),
    path('api/customer/', CustomerList.as_view(),name='customercreate'),
    path('api/customer/<int:pk>', CustomerDetail.as_view(), name='customercreate'),
    path('api/payment/', PaymentList.as_view(), name='customercreate'),
    path('api/payment/<int:pk>', PaymentDetail.as_view(), name='customercreate'),
  
]


