from django.urls import path
from loanapp import views
from django.views.generic import TemplateView
urlpatterns = [
    path('',TemplateView.as_view(template_name="loanapp/index.html")),
]
