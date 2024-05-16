from django.shortcuts import render
from django.core.paginator import Paginator

#from .utils import get_data
from .models import Quote



def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(quotes, per_page)
    qoute_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': qoute_on_page})
