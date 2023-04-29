from django.urls import path
from myapp.views import home, calculate_total, tax_rate_page

urlpatterns = [
    path('', home, name='home'),
    path('tax/<int:num>/', calculate_total, name='calculate_total'),
    path('tax/taxrate/', tax_rate_page, name='tax_rate'),
]