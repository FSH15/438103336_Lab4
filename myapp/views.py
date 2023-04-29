from django.shortcuts import render
from django.http import HttpResponse
TAX_RATE = 0.15

def home(request):
    return render(request, 'home.html')

def calculate_total(request, num=None):
    if num is None:
        return HttpResponse('<h1>Please enter a number to calculate tax</h1>')
    else:
        total = round(float(num) * (1 + TAX_RATE), 2)
        return HttpResponse(f'<h1>The total price after tax is {total}</h1>')

def tax_rate_page(request):
    context = {'tax_rate': TAX_RATE * 100}
    return render(request, 'tax_rate.html', context)

