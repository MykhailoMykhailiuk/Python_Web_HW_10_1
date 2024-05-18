from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Quote, Author


def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(quotes, per_page)
    qoute_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': qoute_on_page})


def author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'quotes/author.html', context={'author': author})
