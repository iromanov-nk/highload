import datetime
from mongokit import Document
from mongokit import Connection
from helpers import get_environment

settings = get_environment()
connection = Connection(settings.get('MONGODB_URI'))
pagging = settings.get('PAGINATION_ROW_COUNT')

@connection.register
class UserVisit(Document):
    __database__ = 'highload'
    __collection__ = 'user_visits'
    structure = {
        'time': datetime.datetime,
        'user_id': int,
        'url': basestring
    }

    required_fields = ['user_id', 'url']
    default_values = {
        'time': datetime.datetime.now
    }


def get_page(page):
    queryset = connection[UserVisit.__database__][UserVisit.__collection__].group(
        ['url'],
        {},
        {'count': 1},
        "function(current, result){ result.count++ }"
    )
    return queryset[(page - 1) * pagging: page * pagging]
