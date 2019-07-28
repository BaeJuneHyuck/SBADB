from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import QuerySet


class MyEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, QuerySet):
            return tuple(o)
        elif hasattr(o, 'as_dict'):
            return o.as_dict()
        return super().default(o)