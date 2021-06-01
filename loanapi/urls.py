from django.urls import path
from .views import LoanList, LoanDetail

app_name = 'loanapi'
urlpatterns = [
    path('', LoanList.as_view(), name='listcreate'),
    path('<int:pk>/', LoanDetail.as_view(), name="detailcreate"),
]
