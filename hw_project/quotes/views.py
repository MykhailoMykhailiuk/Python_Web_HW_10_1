from django.shortcuts import render
from django.core.paginator import Paginator

from .utils import get_data


def main(request, page=1):
    db = get_data()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    qoute_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': qoute_on_page})
