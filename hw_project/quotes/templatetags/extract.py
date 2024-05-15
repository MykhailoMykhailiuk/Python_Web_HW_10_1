from bson.objectid import ObjectId

from django import template

from ..utils import get_data

register = template.Library()


def get_author(id_):
    db = get_data()
    author = db.authors.find_one({'_id': ObjectId(id_)})
    return author['full_name']


register.filter('author', get_author)