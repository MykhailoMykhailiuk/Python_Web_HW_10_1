from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .forms import AuthorForm, QuoteForm
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


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:root')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})


def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:root')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})