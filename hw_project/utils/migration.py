import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")
django.setup()

from quotes.models import Author, Tag, Quote
from quotes.utils import get_data

db = get_data()

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        full_name=author['full_name'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not exist_quote:
        author = db.authors.find_one({'_id': quote['author']})
        a = Author.objects.get(full_name=author['full_name'])
        q = Quote.objects.create(
            quote=quote['quote'],
            author=a
        )
        for tag in tags:
            q.tags.add(tag)


