import datetime
from mongokit import Document
from mongokit import Connection
from helpers import get_environment

settings = get_environment()
connection = Connection(settings.get('MONGODB_URI'))


@connection.register
class UserVisit(Document):
    __database__ = 'highload'
    __collection__ = 'user_visits'
    use_dot_notation = True
    structure = {
        'time': datetime.datetime,
        'user_id': int,
        'url': basestring
    }

    required_fields = ['user_id', 'url']
    default_values = {
        'time': datetime.datetime.now
    }